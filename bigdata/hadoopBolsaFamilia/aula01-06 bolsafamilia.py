#Este programa irá imprimir todas as linhas do arquivo.
import csv 
import pprint
from datetime import datetime
# opens csv file and assingns it to an object
with open('202101_BolsaFamilia_Pagamentos.csv') as csvfile:
    # Use Sniffer to figure out csv dialect
    # lendo blocos de 1K
    dialect = csv.Sniffer().sniff(csvfile.read(16384))
    #Posicionar na primeira posição do arquivo.
    csvfile.seek(0)
    # pass the dialect to filereader to read the file
    reader = csv.reader(csvfile, dialect)
    # print(dialect)
    # Use for loop to print csv row by row
    contLinhas = 0
    now = datetime.now()
    print("now =", now)
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print ("*********************")
    print("date and time =", dt_string) 
    for row in reader:
        contLinhas = contLinhas + 1
        #pprint.pprint("Estado: ",row[2])
        #print ("Estado: %s\t Valor: %s" % (row[2],row[8]))
print ("Quantidade de linhas: ",contLinhas)
now = datetime.now()
print("now =", now)
print ("*********************")