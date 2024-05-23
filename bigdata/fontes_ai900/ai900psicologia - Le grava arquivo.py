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
                print (item)
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
 
nomeArquivoCSV = 'frasespsicologia.csv'
dicComentariosAPP = lerCSV(nomeArquivoCSV)
gravarCSV(nomeArquivoCSV)

 