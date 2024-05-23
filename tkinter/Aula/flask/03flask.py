from flask import render_template
from flask import Flask
app = Flask("Conta Corrente")
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Douglas Rocha Mendes'}
    return render_template('index.html', title='Tela Conta Corrente', user=user)
@app.route('/login')
def login():
    return "<h1>Vamos realizar seu login. </h1>"