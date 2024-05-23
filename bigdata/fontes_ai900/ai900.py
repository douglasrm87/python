import csv
import codecs
# pip install azure-ai-textanalytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def lerCSV(coluna,nomeArquivoCSV):
    dicComentariosAPP = {}
    cont = 0
    comentAPP=csv.reader (codecs.open(nomeArquivoCSV, 'rU', 'utf-16'))
    for item in comentAPP:
        if item[coluna]:
            dicComentariosAPP [cont] = item[coluna]
            cont = cont + 1
    return dicComentariosAPP

def analisarSentimento(opiniao):
    api_key = "c2278282be80402fa0cb6163f2579e0c"
    credential = AzureKeyCredential(api_key)
    text_analytics_client = TextAnalyticsClient(endpoint="https://douglasanalisetextoinstancia.cognitiveservices.azure.com/", credential=credential)
    documents = [
        {"id": "1", "language": "pt", "text": opiniao},
    ]
    response = text_analytics_client.analyze_sentiment(documents)
    #print ("Analise sentimento completo: ",response[0])
    return response[0]
def converterNumero (numero):
    strValor = numero.split ("=")
    valor = float (strValor[1].replace (" ",""))
    return valor

def tratarAnaliseRetornada(dicComentariosAPPSentimento,chave):
    #print ("Conteudo completo:\n " ,dicComentariosAPPSentimento)
    #print ("Chaves do dicionario:\n ",dicComentariosAPPSentimento.keys())
    #print ("Conteudo chave sentences:\n " , dicComentariosAPPSentimento ["sentences"]) 
    #Converter para string
    strDetalheSentimento = '.'.join(str(v) for v in dicComentariosAPPSentimento ["sentences"])
    #print ("String obtida: " , strDetalheSentimento)
    # Selecionar itens de sentimento
    strDetalheSentimentoSplit = strDetalheSentimento.split("SentimentConfidenceScores(")
    #print ("String Split pelo caractere (: " , strDetalheSentimentoSplit[1])
    #print ("String Split pelo caractere ([0]: " , strDetalheSentimentoSplit[1].split(", ")[0])
    #print ("String Split pelo caractere ([1]: " , strDetalheSentimentoSplit[1].split(", ")[1])
    #print ("String Split pelo caractere ([2]: " , strDetalheSentimentoSplit[1].split(", ")[2].split(")")[0])
    # Selecionar a opiniao
    strOpiniao = strDetalheSentimento.split(",")[0].split(":")[1].replace("'","")
    #print ("strOpiniao: " , strOpiniao)
    positivo = strDetalheSentimentoSplit[1].split(", ")[0]
    neutro = strDetalheSentimentoSplit[1].split(", ")[1]
    negativo = strDetalheSentimentoSplit[1].split(", ")[2].split(")")[0]

    #print ("Valor Positivo: ",listaFinalComentariosAPPSentimento[chave][1])
    listaFinalComentariosAPPSentimento [chave] =  (strOpiniao,converterNumero(positivo), converterNumero(neutro), converterNumero(negativo))

def processarAnalise(dicComentariosAPP):
    contSent = 0
    for chave in dicComentariosAPP.keys():
        retAnalise = analisarSentimento(dicComentariosAPP[chave])
        tratarAnaliseRetornada(retAnalise,contSent)
        contSent = contSent + 1
    #print ("listaFinalComentariosAPPSentimento: ",listaFinalComentariosAPPSentimento)

    npsArquivo = 0
    #Fórmula para calcular o NPS é: NPS = Promotores – Detratores/Número total de opiniões.
    valorPromotor = 0.0
    valorDetrator = 0.0
    for npsItem in listaFinalComentariosAPPSentimento.keys():
        valorPromotor = valorPromotor + listaFinalComentariosAPPSentimento[npsItem][1] + listaFinalComentariosAPPSentimento[npsItem][2]
        valorDetrator = valorDetrator + listaFinalComentariosAPPSentimento[npsItem][3]
    print (len (listaFinalComentariosAPPSentimento))
    npsArquivo = ((valorPromotor - valorDetrator) / len (listaFinalComentariosAPPSentimento))
    print ("npsFinal: ",npsFinal)
    return npsArquivo


# escolher a coluna que preciso.
# './appcopelcsv/reviews_reviews_com.copel.mbf_202201.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202202.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202203.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202204.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202205.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202206.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202207.csv'
listaFinalComentariosAPPSentimento = {}
nomeArquivoCSV = ['./appcopelcsv/reviews_reviews_com.copel.mbf_202201.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202202.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202203.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202204.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202205.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202206.csv', './appcopelcsv/reviews_reviews_com.copel.mbf_202207.csv']
npsFinal = 0.0
totalOpinioes = 0
for arq in nomeArquivoCSV:
    listaFinalComentariosAPPSentimento = {}
    dicComentariosAPP = lerCSV(11 , arq)
    npsArquivo = processarAnalise(dicComentariosAPP)
    print ("\nArquivo analisado: ",arq, "NPS Arquivo: " , npsArquivo)
    #print ("Quantidade de opiniões analisadas: ",len (listaFinalComentariosAPPSentimento))
    npsFinal = npsFinal + npsArquivo
    totalOpinioes = totalOpinioes + len (listaFinalComentariosAPPSentimento)

print ("\nForam analisadas: ", totalOpinioes, " com NPS Final: " , float ((npsFinal/len(nomeArquivoCSV))*100))

