from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# Evitará o erroRuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
app.secret_key = 'segredo_super_secreto'  # Recomendado usar variável de ambiente

# Usuários simulados
usuarios = {
    "admin": "1234",
    "garcom": "mesa01"
    #usuario - admin, senha 1234.
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario in usuarios and usuarios[usuario] == senha:
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:
            erro = 'Usuário ou senha inválidos.'
    return render_template('login.html', erro=erro)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', usuario=session['usuario'])

@app.route('/mesas')
def mesas():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('mesas.html')

@app.route('/pedido')
def pedido():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('pedido.html')

@app.route('/pedidos')
def pedidos():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    pedidos = [
        {'id': 101, 'mesa': 'Mesa 1', 'garcom': 'João', 'status': 'Aberto'},
        {'id': 102, 'mesa': 'Mesa 2', 'garcom': 'Ana', 'status': 'Fechado'}
    ]
    return render_template('pedidos.html', pedidos=pedidos)

if __name__ == '__main__':
    app.run(debug=True)
