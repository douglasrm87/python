import csv,sys
import codecs
# pip install azure-ai-textanalytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def lerCSV(coluna,nomeArquivoCSV):
    dicComentariosAPP = {}
    cont = 0
    with codecs.open(nomeArquivoCSV, 'rU', 'utf-8') as ficheiro:
        comentAPP = csv.reader(ficheiro,delimiter=";")
        try:
            for item in comentAPP:
                print (item)
        except csv.Error as e:
            sys.exit ('ficheiro %s, linha %d: %s' % (nomeArquivoCSV, comentAPP.line_num, e))
        return dicComentariosAPP
   
 
nomeArquivoCSV = 'frasespsicologia.csv'
dicComentariosAPP = lerCSV(1 , nomeArquivoCSV)
print ("dicComentariosAPP: " , dicComentariosAPP)
 