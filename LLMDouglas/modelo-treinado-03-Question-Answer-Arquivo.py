from transformers import pipeline
import os

# Exemplo simples de uso de LLM com Hugging Face Transformers
# Certifique-se de instalar: pip install transformers torch

qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

def carregarContextos():
    caminho_arquivo = "/workspaces/python/LLMDouglas/modelo-treinado-03-contexto.txt"  # ou "contexto.docx" para Word

    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo '{caminho_arquivo}' não encontrado. Verifique o caminho e o nome do arquivo.")

    if caminho_arquivo.endswith(".txt"):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            contexto = f.read()
    elif caminho_arquivo.endswith(".docx"):
        from docx import Document  # pip install python-docx
        doc = Document(caminho_arquivo)
        contexto = "\n".join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Formato de arquivo não suportado. Use .txt ou .docx")
    print(type(contexto))
    return contexto

def processarPerguntaresposta(pergunta):
    # Recarrega o contexto a cada execução para garantir dados atualizados
    contexto = carregarContextos()
    resposta = qa_pipeline(question=pergunta, context=contexto)
    return resposta['answer']
'''
def processarPerguntarespostaMultiplosModelos(pergunta):
    modelos = [
        "distilbert-base-cased-distilled-squad",
        "deepset/roberta-base-squad2",
        "bert-large-uncased-whole-word-masking-finetuned-squad"
    ]
    respostas = []
    contexto = carregarContextos()
    for modelo in modelos:
        qa_pipeline = pipeline("question-answering", model=modelo)
        resposta = qa_pipeline(question=pergunta, context=contexto)
        respostas.append(resposta['answer'])
    # Seleciona a resposta mais frequente (votação simples)
    resposta_final = Counter(respostas).most_common(1)[0][0]
    return resposta_final
'''

def main():
    pergunta = "Qual é a capital da França?"
    resposta = processarPerguntaresposta(pergunta)
    print(f"Pergunta: {pergunta} | Resposta: {resposta}")

    pergunta = "Qual é o modelo de governo da França?"
    resposta = processarPerguntaresposta(pergunta)
    print(f"Pergunta: {pergunta} | Resposta: {resposta}")


if __name__ == "__main__":
    main()