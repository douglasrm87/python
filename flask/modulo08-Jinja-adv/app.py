from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                preco REAL,
                promocao INTEGER
            )
        ''')
        db.commit()

@app.route("/")
def index():
    db = get_db()
    produtos = db.execute("SELECT * FROM products").fetchall()
    return render_template("index.html", produtos=produtos)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username=? AND password=?", (usuario, senha)).fetchone()
        if user:
            session["user_id"] = user["id"]
            return redirect(url_for("index"))
        else:
            return "Login inválido"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/add", methods=["GET", "POST"])
def add_product():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        nome = request.form["nome"]
        preco = float(request.form["preco"])
        promocao = 1 if "promocao" in request.form else 0

        db = get_db()
        db.execute("INSERT INTO products (nome, preco, promocao) VALUES (?, ?, ?)", (nome, preco, promocao))
        db.commit()
        return redirect(url_for("index"))
    return render_template("add_product.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["usuario"]
        password = request.form["senha"]
        
        db = get_db()
        try:
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            db.commit()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            return "Usuário já existe."
    
    return render_template("register.html")


if __name__ == "__main__":
    init_db()
    app.run(host='127.0.0.1', port=8081,debug=True, use_reloader=True)