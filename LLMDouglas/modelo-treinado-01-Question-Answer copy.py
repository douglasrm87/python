from transformers import pipeline

# Exemplo simples de uso de LLM com Hugging Face Transformers
# Certifique-se de instalar: pip install transformers torch

def carregarContextos():
    contexto = (
        "A França é um país localizado na Europa Ocidental, conhecido por sua rica história, cultura e influência global. " 
        "A cidade de Paris é famosa por seus museus, arquitetura e como um centro de arte e moda. Sendo a principal cidade francesa Paris é sua capital. "
        "A França foi libertada pela acção dos Aliados e da Resistência Francesa (organizada em Londres pelo general Charles de Gaulle, também veterano que lutou nas trincheiras da Primeira Guerra Mundial). Quando os Aliados desembarcaram no norte de África em novembro de 1942, ocuparam a zona livre metropolitana (o que acarretou o afundamento da frota francesa em Toulon). A Resistência, não obstante, desenvolveu-se e organizou-se. Em maio de 1943, o general De Gaulle chegou a Argel: um Comitê francês de libertação nacional foi criado em 3 de Junho de 1944 e transformado em governo provisório da República Francesa. Em 6 de Junho de 1944, os Aliados desembarcaram na Normandia e avançaram em direção a Paris, que foi libertada em 25 de Agosto. O governo provisório, presidido por De Gaulle, lá se instalou imediatamente."
        "Paris é conhecida por sua cultura, gastronomia e monumentos históricos como a Torre Eiffel. "
        "Python é uma linguagem de programação popular, conhecida por sua simplicidade e legibilidade. "
        "Ela é amplamente utilizada em ciência de dados, desenvolvimento web, automação e inteligência artificial."
    )
    print(type(contexto))
    return contexto

def main():
    # Carrega um modelo LLM pequeno para perguntas e respostas
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    contexto = carregarContextos()

    pergunta = "Qual é a capital da França?"
    resposta = qa_pipeline(question=pergunta, context=contexto)
    print(f"Pergunta: {pergunta}")
    print(f"Resposta: {resposta['answer']}")

    pergunta = "Me diga qual é uma linguagem popular?"
    resposta = qa_pipeline(question=pergunta, context=contexto)
    print(f"Pergunta: {pergunta}")
    print(f"Resposta: {resposta['answer']}")

if __name__ == "__main__":
    main()