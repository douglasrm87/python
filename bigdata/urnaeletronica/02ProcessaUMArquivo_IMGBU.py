# TSE
# https://dadosabertos.tse.jus.br/dataset/resultados-2022-arquivos-transmitidos-para-totalizacao
# Arquivos com a extensão imgbu segundo turno - 34.423 arquivos.
# 	https://pt.stackoverflow.com/questions/251807/python-abrir-m%C3%BAltiplos-arquivos-em-um-for

from pathlib import Path
urna = open("AC_o00407-0100700090001.imgbu","r",encoding='ISO-8859-1',errors='ignore')
for row in urna:
   print (row)