# app.py

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# Rota principal redireciona para o login
@app.route('/')
def index():
    return redirect(url_for('login'))

# Rota de Login
@app.route('/login')
def login():
    return render_template('login.html')

# --- SPRINT 1 ---
@app.route('/mapa-mesas')
def mapa_mesas():
    # O mapa de mesas se torna a tela principal após o login
    return render_template('sprint3_mapa_mesas.html')

@app.route('/pedidos/mesa/<int:id_mesa>')
def fazer_pedido(id_mesa):
    return render_template('sprint1_pedidos.html', id_mesa=id_mesa)

@app.route('/cozinha')
def cozinha():
    return render_template('sprint1_kds.html')

@app.route('/caixa')
def caixa():
    return render_template('sprint1_caixa.html')

@app.route('/esqueciasenha')
def esqueciasenha():
    return render_template('esqueciasenha.html')

# --- SPRINT 2 ---
@app.route('/relatorios')
def relatorios():
    return render_template('sprint2_relatorios.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)