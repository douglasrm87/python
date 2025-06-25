from transformers import pipeline
from datetime import datetime

def carregarModeloTraducao(langSource,langTarget, texto):
    #Necessario instalar - pip install sentencepiece
    m2m100 = pipeline('translation', 'facebook/m2m100_418M', src_lang=langSource, tgt_lang=langTarget)
    print(m2m100([texto]))
    return m2m100    


def traduzir():
    modeloIA =  carregarModeloTraducao("pt","en", "texto a ser traduzido")
    while True:
        texto = input("Digite o texto para traduzir (ou 'sair' para encerrar): ")
        print("Hora atual Antes:", datetime.now().strftime("%H:%M:%S"))
        if texto.lower() == 'sair':
            break
        print(modeloIA([texto]))
        print("Hora atual Depois:", datetime.now().strftime("%H:%M:%S"))

def main():
    traduzir()
    
     
if __name__ == "__main__":
    main()