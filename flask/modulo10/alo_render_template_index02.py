from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Douglas Rocha Mendes'} 
    return render_template('index02.html', title='Tela Conta Corrente', user=user)

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True, use_reloader=True)