# TSE
# https://dadosabertos.tse.jus.br/dataset/resultados-2022-arquivos-transmitidos-para-totalizacao
# Arquivos com a extensão imgbu segundo turno - 34.423 arquivos.
# 	https://pt.stackoverflow.com/questions/251807/python-abrir-m%C3%BAltiplos-arquivos-em-um-for

from pathlib import Path

contadorLinhas = 0
totalGeral = 0
total13 = 0
total22 = 0
caminho = Path("./")
multiplosArquivos = caminho.glob("*.csv")
for arqs in multiplosArquivos:
    arquivoVotos = open(arqs ,"r")
    for linhaVotacao in arquivoVotos:
        vetor =linhaVotacao.split(",") 
        #para pular o header
        if (contadorLinhas > 0):
           totalGeral = totalGeral + int(vetor[7])+ int(vetor[8])
           total13 = total13 + int(vetor[7]) 
           total22 = total22 + int(vetor[8])
        else:
            cont = 0
            for item in vetor:
                print ("Cont: " , cont, " - " , item)
                cont = cont + 1

        if (contadorLinhas > 3):
           break
        contadorLinhas = contadorLinhas + 1
    break
print ("Total Geral:", totalGeral)
print ("Total 13:", total13)
print ("Total 22:", total22)
print ("Percentual de cada candidato: ")
print ("Percentual 22:", total22/totalGeral)
print ("Percentual 13:", total13/totalGeral)

arquivoVotos.close()
   