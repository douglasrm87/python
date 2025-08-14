from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para a sessão

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''A função flash() é frequentemente usada com a função get_flashed_messages() para exibir mensagens dinamicamente nos modelos. 
A função flash() adiciona uma mensagem à sessão do usuário, que pode ser recuperada posteriormente.
A função get_flashed_messages() é usada para recuperar essas mensagens e exibi-las no template.
Aqui, estamos apenas verificando se o usuário e a senha estão corretos.
Se estiverem, uma mensagem de sucesso é exibida. Caso contrário, uma mensagem de erro é exibida.            '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            # Mensagem de sucesso
            flash('Login bem-sucedido!', 'success')
        else:
            flash('Credenciais inválidas. Tente novamente.', 'error')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)