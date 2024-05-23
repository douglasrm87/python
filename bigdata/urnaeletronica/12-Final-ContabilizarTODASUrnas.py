# TSE
# https://dadosabertos.tse.jus.br/dataset/resultados-2022-arquivos-transmitidos-para-totalizacao
# Arquivos com a extensão imgbu segundo turno - 34.423 arquivos.
# 	https://pt.stackoverflow.com/questions/251807/python-abrir-m%C3%BAltiplos-arquivos-em-um-for

import csv
from pathlib import Path
import re

contadorLinhas = 0
totalGeral = 0
total13 = 0
total22 = 0
caminho = Path("./")
multiplosArquivos = caminho.glob("bu_imgbu_logjez_rdv_vscmr_2022_2t_AC.csv")
for arqs in multiplosArquivos:
    arquivoVotos = open(arqs ,"r")
    for linhaVotacao in arquivoVotos:
        vetor =linhaVotacao.split(",") 
        #para pular o header
        if (contadorLinhas > 0):
        #    print ("Lula: ",vetor[14]," ",vetor[15])
           totalGeral = totalGeral + int(vetor[7])+ int(vetor[8])
           total13 = total13 + int(vetor[7]) 
           total22 = total22 + int(vetor[8])
        else:
            i = 0
            for item in vetor:
                print ("Item:",i," - " ,item)
                i = i + 1
            print ("Estado:", arquivoVotos.name)

        contadorLinhas = contadorLinhas + 1

print ("Urnas Avaliadas:", contadorLinhas)
print ("Total Geral:", totalGeral)
print ("Total 13:", total13)
print ("Total 22:", total22)
print ("Percentual de cada candidato: ")
if (total22>0):
    print ("Percentual 22:", total22/totalGeral)

if (total13>0):
    print ("Percentual 13:", total13/totalGeral)


arquivoVotos.close()
   