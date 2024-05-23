# TSE
# https://dadosabertos.tse.jus.br/dataset/resultados-2022-arquivos-transmitidos-para-totalizacao
# Arquivos com a extensão imgbu segundo turno - 34.423 arquivos.
# 	https://pt.stackoverflow.com/questions/251807/python-abrir-m%C3%BAltiplos-arquivos-em-um-for

import csv
from pathlib import Path
import re

contadorLinhas = 0
caminho = Path("./")
multiplosArquivos = caminho.glob("*.csv")
for arqs in multiplosArquivos:
    arquivoVotos = open(arqs ,"r")
    for linhaVotacao in arquivoVotos:
        print (linhaVotacao)
        if (contadorLinhas == 2):
            break
        contadorLinhas = contadorLinhas + 1
    break
arquivoVotos.close()
   