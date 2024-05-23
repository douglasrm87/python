# TSE
# https://dadosabertos.tse.jus.br/dataset/resultados-2022-arquivos-transmitidos-para-totalizacao
# Arquivos com a extensão imgbu segundo turno - 34.423 arquivos.
# 	https://pt.stackoverflow.com/questions/251807/python-abrir-m%C3%BAltiplos-arquivos-em-um-for

import csv
from pathlib import Path
import re

# opens csv file and assingns it to an object
def vetorToString(s):
    # initialize an empty string
    str1 = " "
    # return string 
    return (str1.join(s))      
urna = open('./AL_o00407-2700600170011.imgbu',"r",encoding='ISO-8859-1',errors='ignore')

for linhaValida in urna:
   linhaValida = re.sub(r'\s+', " ",linhaValida)
   if ("Município" in linhaValida):
      vet = linhaValida.strip().split (" ")
      vet[-1] = ","+vet[-1]
      print (vetorToString(vet))
      for proximaLinhaValida in urna:
         proximaLinhaValida = "Cidade," + re.sub(r'\s+', " ",proximaLinhaValida)
         print (proximaLinhaValida)
         break
   if ("Zona Eleitoral" in linhaValida or 
       "Local de Votação" in linhaValida or 
       "Seção Eleitoral" in linhaValida or 
       "Eleitores aptos" in linhaValida or 
       "Comparecimento" in linhaValida or 
       "Eleitores faltosos" in linhaValida or 
       "Habilitados por" in linhaValida or 
       "Código identificação" in linhaValida or 
       "Data de abertura" in linhaValida or
       "Horário de abertura" in linhaValida or
       "Data de fechamento da UE" in linhaValida or
       "Horário de fechamento" in linhaValida or
       "LULA" in linhaValida or
       "JAIR BOLSONARO" in linhaValida or
       "Eleitores Aptos" in linhaValida or
       "Total de votos Nominais" in linhaValida or
       "Brancos" in linhaValida or
       "Nulos" in linhaValida or
       "Total Apurado" in linhaValida  ):
      vet = linhaValida.strip().split (" ")
      vet[-1] = ","+vet[-1]
      print (vetorToString(vet))
urna.close()
