'''

https://didatica.tech/tudo-sobre-o-framework-flask-para-iniciantes/


Em resumo:
__name__ é uma variável Python que indica o nome do módulo atual.
Em Flask, __name__ é usado para fornecer ao framework informações sobre a localização do seu aplicativo, permitindo que ele encontre recursos como modelos e arquivos estáticos.
Quando um script é executado diretamente, __name__ vale ` 'main' `.
Essa informação é usada pelo Flask para configurar a aplicação corretamente. 
Neste exemplo, __name__ == "__main__" verifica se o script está sendo executado diretamente. Se for o caso, a função app.run(debug=True) inicia o servidor de desenvolvimento do Flask. O argumento debug=True ativa o modo de depuração, que é útil para desenvolvimento, mas não deve ser usado em produção. 

'''
from flask import Flask, render_template
app = Flask(__name__)

#Exemplo slide Flask Application
#https://vigilant-space-eureka-599vgvpxwrfvqxj-5000.app.github.dev/
@app.route('/')
def raiz():
    print ("Nome do programa:", __name__)
    return '<h1>Hello World' + 'Programa Principal: </p>' + __name__

#Exemplo slide Flask Application
#https://vigilant-space-eureka-599vgvpxwrfvqxj-5000.app.github.dev/alo
@app.route('/alo')
def hello_world():
    return 'hello world'

#Exemplo slide Flask Variables
#https://vigilant-space-eureka-599vgvpxwrfvqxj-5000.app.github.dev/nome/Douglas
@app.route('/nome/<mNome>')
def apresentarNome(mNome):
    return '<h1>Bom dia Sr(a) %s '  %mNome + '!</h1>'

#Exemplo slide Flask - Templates
#https://vigilant-space-eureka-599vgvpxwrfvqxj-5000.app.github.dev/nome/Douglas
@app.route('/nomehtml/<mNome>')
def apresentarNomeHTML(mNome):
    return render_template('introducao01_flask.html', name = mNome) 

#Exemplo slide Flask - Message Flashing

if __name__ == '__main__':
    app.run()