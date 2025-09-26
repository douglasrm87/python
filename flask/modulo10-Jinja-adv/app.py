''''
A importação from flask import g em Flask permite que você acesse o objeto g, que é usado para armazenar dados específicos de cada requisição. Ele atua como um espaço temporário para guardar informações que precisam ser compartilhadas entre diferentes funções dentro do processamento de uma única requisição. 
O que é 'g' em Flask?
Armazenamento Temporário:
g é usado para armazenar dados que são relevantes apenas para a requisição atual.
Compartilhamento entre Funções:
Ele permite que diferentes partes do seu código Flask acessem e modifiquem os mesmos dados dentro de uma única requisição.
Limpeza Automática:
Ao final de cada requisição, o conteúdo de g é automaticamente limpo, garantindo que dados de requisições anteriores não interfiram em novas requisições. 

Rodar - python app.py
Acesse - http://127.0.0.1:5000/
# Usuário e senha padrão não são definidos no código.
# Você deve registrar um novo usuário acessando /register e criando seu próprio login e senha.

Já criei:
    usuário: admin 
    senha:12345
'''

from flask import Flask, render_template, request, redirect, url_for, session    
from flask import g  # Import g to use it for storing the database connection
import sqlite3

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'

DATABASE = 'database.db'
'''
 
 
O objeto g é uma variável global do Flask usada para armazenar dados durante o ciclo de vida de uma requisição.
getattr verifica se já existe uma conexão aberta.
Se não existir, cria uma nova conexão e salva em g para evitar múltiplas conexões.
row_factory facilita o acesso aos dados retornados pelo banco.
Se quiser explicações mais detalhadas sobre algum ponto, só pedir!
'''
def get_db():
    db = getattr(g, '_database', None)  # Usa o objeto 'g' para recuperar a conexão do banco de dados, se já existir. Se não existir, retorna None.
    if db is None:  # Verifica se a conexão ainda não foi criada.
        db = g._database = sqlite3.connect(DATABASE) # Cria uma nova conexão com o banco de dados e armazena em 'g._database' para reutilização.
        db.row_factory = sqlite3.Row # Configura a conexão para retornar linhas como objetos do tipo 'Row', permitindo acesso por nome de coluna.
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
            session["user_nome"] = user["username"]
            return redirect(url_for("index"))
        else:
            return "<h1>Login inválido</h1><p>Por favor, verifique suas credenciais e tente novamente.</p>"
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
            return "<h1>Usuário já existe.</h1>"

    return render_template("register.html")

''' 
✅ Resultado:
Cada produto terá um botão "Remover"
Só aparece para usuários logados
Ao clicar, é feita uma confirmação
Depois, o produto é excluído do banco de dados
'''

@app.route("/delete/<int:id>", methods=["POST"])
def delete_product(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    db = get_db()
    db.execute("DELETE FROM products WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db() # Initialize the database, cria as tabelas se não existirem
    app.run(host='127.0.0.1', port=8081,debug=True, use_reloader=True)