from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

'''
Com banco de dados e arquivo
usuário - admin
senha - 12345
python app.py
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    transactions = db.relationship('Transaction', backref='user', lazy=True)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)  # 'deposit' or 'withdrawal'
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash('Registration successful')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/deposit', methods=['POST'])
@login_required
def deposit():
    amount = float(request.form['amount'])
    if amount <= 0:
        flash('Amount must be positive')
        return redirect(url_for('dashboard'))
    
    current_user.balance += amount
    transaction = Transaction(amount=amount, transaction_type='deposit', user_id=current_user.id)
    db.session.add(transaction)
    db.session.commit()
    flash(f'Successfully deposited ${amount:.2f}')
    return redirect(url_for('dashboard'))

@app.route('/withdraw', methods=['POST'])
@login_required
def withdraw():
    amount = float(request.form['amount'])
    if amount <= 0:
        flash('Amount must be positive')
        return redirect(url_for('dashboard'))
    
    if amount > current_user.balance:
        flash('Insufficient funds')
        return redirect(url_for('dashboard'))
    
    current_user.balance -= amount
    transaction = Transaction(amount=amount, transaction_type='withdrawal', user_id=current_user.id)
    db.session.add(transaction)
    db.session.commit()
    flash(f'Successfully withdrawn ${amount:.2f}')
    return redirect(url_for('dashboard'))

@app.route('/transactions')
@login_required
def transactions():
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.timestamp.desc()).all()
    return render_template('transactions.html', transactions=transactions)

@app.route('/export_transactions')
@login_required
def export_transactions():
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.timestamp.desc()).all()
    
    filename = f'transactions_{current_user.username}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    filepath = f'static/exports/{filename}'
    
    # Ensure exports directory exists
    import os
    os.makedirs('static/exports', exist_ok=True)
    
    with open(filepath, 'w') as f:
        f.write(f"Transaction History for {current_user.username}\n")
        f.write("=" * 50 + "\n\n")
        for t in transactions:
            f.write(f"Date: {t.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Type: {t.transaction_type}\n")
            f.write(f"Amount: ${t.amount:.2f}\n")
            f.write("-" * 30 + "\n")
    
    return redirect(url_for('static', filename=f'exports/{filename}'))

@app.route('/import_transactions', methods=['POST'])
@login_required
def import_transactions():
    if 'file' not in request.files:
        flash('No file provided')
        return redirect(url_for('transactions'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('transactions'))
    
    try:
        content = file.read().decode('utf-8').split('\n')
        current_transaction = {}
        imported_count = 0
        
        for line in content:
            line = line.strip()
            if line.startswith('Date:'):
                if current_transaction and len(current_transaction) == 3:
                    # Process complete transaction
                    transaction = Transaction(
                        amount=float(current_transaction['amount'].replace('$', '')),
                        transaction_type=current_transaction['type'],
                        timestamp=datetime.strptime(current_transaction['date'], '%Y-%m-%d %H:%M:%S'),
                        user_id=current_user.id
                    )
                    db.session.add(transaction)
                    imported_count += 1
                current_transaction = {'date': line[6:].strip()}
            elif line.startswith('Type:'):
                current_transaction['type'] = line[6:].strip()
            elif line.startswith('Amount:'):
                current_transaction['amount'] = line[8:].strip()
        
        # Process last transaction if complete
        if current_transaction and len(current_transaction) == 3:
            transaction = Transaction(
                amount=float(current_transaction['amount'].replace('$', '')),
                transaction_type=current_transaction['type'],
                timestamp=datetime.strptime(current_transaction['date'], '%Y-%m-%d %H:%M:%S'),
                user_id=current_user.id
            )
            db.session.add(transaction)
            imported_count += 1
        
        db.session.commit()
        flash(f'Successfully imported {imported_count} transactions')
    except Exception as e:
        flash(f'Error importing transactions: {str(e)}')
    
    return redirect(url_for('transactions'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)