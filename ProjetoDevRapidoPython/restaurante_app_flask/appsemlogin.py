#
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/mesas')
def mesas():
    return render_template('mesas.html')

@app.route('/pedido')
def pedido():
    return render_template('pedido.html')

@app.route('/pedidos')
def pedidos():
    pedidos = [
        {'id': 101, 'mesa': 'Mesa 1', 'garcom': 'João', 'status': 'Aberto'},
        {'id': 102, 'mesa': 'Mesa 2', 'garcom': 'Ana', 'status': 'Fechado'}
    ]
    return render_template('pedidos.html', pedidos=pedidos)

if __name__ == '__main__':
    app.run(debug=True)
