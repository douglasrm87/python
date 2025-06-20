#pip install transformers torch
from transformers import pipeline

def gerarRespostaComLLM(model_name, prompt):
    # Usa o pipeline de resposta a perguntas (question-answering)
    qa_pipeline = pipeline("question-answering", model=model_name)
    # Define um contexto simples para garantir a resposta correta
    contexto = "Paris é a capital da França."
    resposta = qa_pipeline(question=prompt, context=contexto)
    return resposta['answer']

if __name__ == "__main__":
    model_name = "deepset/roberta-base-squad2"  # Modelo treinado para QA em português/inglês
    prompt = "Qual é a capital da França?"
    resposta = gerarRespostaComLLM(model_name, prompt)
    print("resposta: ", resposta)
