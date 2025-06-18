#pip install transformers torch
from transformers import AutoModelForCausalLM, AutoTokenizer
def criarLLM(model_name: str):
    """
    Cria um modelo de linguagem grande (LLM) usando a biblioteca Transformers.
    Args:
        model_name (str): O nome do modelo a ser carregado.
    Returns:
        tuple: Um tupla contendo o modelo e o tokenizador.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype='auto')
    return model, tokenizer
def carregarLLM(model_name: str):
    """
    Carrega um modelo de linguagem grande (LLM) e seu tokenizador.
    Args:
        model_name (str): O nome do modelo a ser carregado.
    Returns:
        tuple: Um tupla contendo o modelo e o tokenizador.
    """
    return criarLLM(model_name)
def gerarResposta(model, tokenizer, prompt: str):
    """ Gera uma resposta para um prompt usando o modelo de linguagem grande (LLM).
    Args:
        model: O modelo de linguagem grande (LLM).
        tokenizer: O tokenizador associado ao modelo.
        prompt (str): O prompt de entrada para o modelo.
    Returns:
        str: A resposta gerada pelo modelo.
    """
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return resposta 
def gerarRespostaComLLM(model_name: str, prompt: str):
    """ Gera uma resposta para um prompt usando um modelo de linguagem grande (LLM) especificado pelo nome do modelo.
    Args:
        model_name (str): O nome do modelo a ser carregado.
        prompt (str): O prompt de entrada para o modelo.
    Returns:
        str: A resposta gerada pelo modelo.
    """
    model, tokenizer = carregarLLM(model_name)
    return gerarResposta(model, tokenizer, prompt)

if __name__ == "__main__":
    model_name = "gpt2"  # Modelo popular e amplamente suportado
    prompt = "Qual é a capital da França?"
    resposta = gerarRespostaComLLM(model_name, prompt)
    print ("resposta: ", resposta)
    #print(f"Resposta: {resposta}")