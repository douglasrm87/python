import csv
from pathlib import Path

urna = open('./AC_o00407-0100700090001.imgbu',"r",encoding='ISO-8859-1',errors='ignore')
for linhaValida in urna:
   if ("Município" in linhaValida):
       print (linhaValida)
       for proximaLinhaValida in urna:
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
      print (linhaValida)
      