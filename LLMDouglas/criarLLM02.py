from transformers import pipeline

# Exemplo simples de uso de LLM com Hugging Face Transformers
# Certifique-se de instalar: pip install transformers torch

def carregarContextos():
    contexto = (
        "A capital da França é Paris. "
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

if __name__ == "__main__":
    main()