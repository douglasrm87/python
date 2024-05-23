import csv,sys
import codecs
# pip install azure-ai-textanalytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def lerCSV(nomeArquivoCSV):
    dicComentariosAPP = {}
    cont = 0
    with codecs.open(nomeArquivoCSV, 'rU', 'utf-8') as ficheiro:
        comentAPP = csv.reader(ficheiro,delimiter=";")
        try:
            for item in comentAPP:
                dicComentariosAPP [cont] = item[0]
                cont = cont + 1

        except csv.Error as e:
            sys.exit ('Leitura ficheiro %s, linha %d: %s' % (nomeArquivoCSV, comentAPP.line_num, e))
        return dicComentariosAPP

def gravarCSV(nomeArquivoCSV):
    c = csv.writer(codecs.open("saida.csv", 'wb', 'utf-8'))
    c.writerow(["Declaracao","POSITIVA","NEUTRA","NEGATIVA","SENTIMENTO"] )
    

    with codecs.open(nomeArquivoCSV, 'rU', 'utf-8') as ficheiro:
        comentAPP = csv.reader(ficheiro,delimiter=";")
        try:
            for item in comentAPP:
                print ()
                c.writerow(item)
                
        except csv.Error as e:
            sys.exit ('Leitura ficheiro %s, linha %d: %s' % (nomeArquivoCSV, comentAPP.line_num, e))

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

nomeArquivoCSV = 'frasespsicologia.csv'
dicComentariosAPP = lerCSV(nomeArquivoCSV)
print (dicComentariosAPP)
ret = analisarSentimento(dicComentariosAPP)
print(ret)

#gravarCSV(nomeArquivoCSV)

 