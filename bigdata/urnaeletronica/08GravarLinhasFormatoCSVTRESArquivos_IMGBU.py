# TSE
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
multiplosArquivos = ("AC_o00407-0100700090001.imgbu","AL_o00407-2700600170011.imgbu")
headerCSV = ""
LinhaCSV = ""
flagHeader = 0
urnasUnificadas = open("./urnas_unificadas.csv" ,"w")
for arqs in multiplosArquivos:
    urna = open(arqs ,"r",encoding='ISO-8859-1',errors='ignore')
    for linhaValida in urna:
        linhaValida = re.sub(r'\s+', " ",linhaValida)
        if ("Município" in linhaValida):
            vet = linhaValida.strip().split (" ")
            vet[-1] = ","+vet[-1]
            headerCSV = vetorToString(vet).split(",")[0]+","
            LinhaCSV = vetorToString(vet).split(",")[1]+","
            for proximaLinhaValida in urna:
                proximaLinhaValida = "Cidade," + re.sub(r'\s+', " ",proximaLinhaValida)
                headerCSV = headerCSV + proximaLinhaValida.split(",")[0]+","
                LinhaCSV = LinhaCSV + proximaLinhaValida.split(",")[1]+","
                break
        if ("Zona Eleitoral" in linhaValida or
                "Local de Votação" in linhaValida or 
                "Seção Eleitoral" in linhaValida or
                "Eleitores faltosos" in linhaValida or
                "Habilitados por ano nascimento" in linhaValida ):
            vet = linhaValida.strip().split (" ")
            vet[-1] = ","+vet[-1]
            headerCSV = headerCSV + vetorToString(vet).split(",")[0]+","
            LinhaCSV = LinhaCSV + vetorToString(vet).split(",")[1]+","

        if ("PRESIDENTE" in linhaValida):
                for linhaValida in urna:
                    if ("LULA" in linhaValida or "JAIR BOLSONARO" in linhaValida or
                        "Eleitores Aptos" in linhaValida or "Total de votos Nominais" in linhaValida or
                        "Brancos" in linhaValida or "Nulos" in linhaValida or 
                        "Total Apurado" in linhaValida):
                        vet = linhaValida.strip().split (" ")
                        vet[-1] = ","+vet[-1]
                        headerCSV = headerCSV + vetorToString(vet).split(",")[0]+","
                        LinhaCSV = LinhaCSV + vetorToString(vet).split(",")[1]+","

    if (flagHeader == 0):
        headerCSV = re.sub(r'\s+', " ",headerCSV)
        urnasUnificadas.write(headerCSV)
        urnasUnificadas.write("\n")
        flagHeader = 1
    urnasUnificadas.write(LinhaCSV)
    urnasUnificadas.write("\n")
urna.close()
urnasUnificadas.close()
   