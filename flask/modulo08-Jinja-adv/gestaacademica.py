
from flask import Flask, request,render_template # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação
@app.route('/') # Nova rota
def main():
    resultado = None    
    primeira = request.args.get('SM1')
    print ("Primeira nota:", primeira) # Debug: imprime a primeira nota
    if primeira:
        primeira = primeira.strip() # Remove espaços em branco
        if primeira == '':
            primeira = None # Se a nota for vazia, define como None
    else:
        primeira = 0 # Se a nota não for informada, define como None
    print ("Primeira nota após verificação:", primeira) # Debug: imprime a primeira nota
    segunda = request.args.get('SM2')   
    print ("Segunda nota:", segunda) # Debug: imprime a segunda nota
    if segunda:
        segunda = segunda.strip() # Remove espaços em branco
        if segunda == '':
            segunda = None # Se a nota for vazia, define como None
    else:
        segunda = 0 # Se a nota não for informada, define como None
    print ("Segunda nota após verificação:", segunda) # Debug: imprime a segunda nota
    terceira = request.args.get('AV')
    print ("Terceira nota:", terceira) # Debug: imprime a terceira nota
    if terceira:
        terceira = terceira.strip() # Remove espaços em branco
        if terceira == '':
            terceira = None # Se a nota for vazia, define como None
    else:
        terceira = 0 # Se a nota não for informada, define como None
    print ("Terceira nota após verificação:", terceira) # Debug: imprime a terceira nota
    media = 0

    if primeira and segunda:
        # Converte as notas para float
        # Se a terceira nota não for informada, calcula a média com as duas primeiras
        if terceira:
            primeira = float(primeira)
            segunda = float(segunda)
            terceira = float(terceira)
            media = (primeira + segunda + terceira) 
        else:
            media = (primeira + segunda)
    elif primeira or segunda or terceira:
        # Se apenas uma ou duas notas forem informadas, calcula a média com as disponíveis
        if primeira:
            primeira = float(primeira)
        if segunda:
            segunda = float(segunda)
        if terceira:
            terceira = float(terceira)
            media = (primeira + segunda + terceira)
        else:
            media = (primeira + segunda)
    else:
        # Se nenhuma nota for informada, define a média como 0
        media = 0    
    if media >= 60:
            resultado = 'Aprovado'
    elif media >= 40:
        resultado = 'Recuperação - Realizar AVS'
    else:
        resultado = 'Reprovado'
    return render_template('notas.html', media=media,resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True) # Executa a aplicação com debug ativado