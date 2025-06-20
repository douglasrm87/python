from transformers import pipeline


# Lista de textos para analisar
texts = [
    "Hoje o dia está maravilhoso e estou muito feliz!",
    "Estou me sentindo muito triste e desanimado.",
    "O tempo está normal, nada de especial aconteceu.",
    "Ganhei um presente incrível, estou radiante!",
    "Perdi meu ônibus e isso me deixou chateado."
]

# Cria o pipeline de análise de sentimento
analisarSentimento = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Função para mapear o resultado do modelo para feliz, triste ou normal
def classificar_sentimento(i, text, result):
    #print (f"Texto {i}: \"{text}\" -> Sentimento: {result[0]['label']}")
    #print (f"Texto {i}: \"{text}\" -> Score: {result[0]['score']}")
    if result[0]['label'] in ["4 stars", "5 stars"]:
        return "feliz"
    elif result[0]['label'] in ["1 star", "2 stars"]:
        return "triste"
    else:
        return "normal"
# Podemos usar o score para uma análise mais detalhada, mas aqui vamos simplificar

# Analisa cada texto e apresenta o sentimento
for i, text in enumerate(texts, 1):
    result = analisarSentimento(text)
    sentimento = classificar_sentimento(i, text, result)
    print(f"Texto {i}: \"{text}\" -> Sentimento: {sentimento}")