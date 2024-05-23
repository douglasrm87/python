from flask import Flask, request,render_template # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Nova rota
def main():
    resultado = 'Entre as notas na URL'    
    primeira = request.args.get('av1')
    segunda = request.args.get('av2')
    media = 0
    if primeira and segunda:
        primeira = float(primeira)
        segunda = float(segunda)
        print ("Nota 01:",primeira)
        print ("Nota 02:",segunda)
        media = (primeira + segunda) / 2
        if media >= 60:
            resultado = 'Aprovado'
        elif media >= 40:
            resultado = 'Recuperação - Realizar AV3'
        else:
            resultado = 'Reprovado'
    return render_template('exercicionotas.html', media=media,resultado=resultado)