#Este programa irá imprimir todas as linhas do arquivo.
import csv 
import pprint
# opens csv file and assingns it to an object
with open('202101_BolsaFamilia_Pagamentos.csv') as csvfile:
    # Use Sniffer to figure out csv dialect
    # lendo blocos de 1K
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    #Posicionar na primeira posição do arquivo.
    csvfile.seek(0)
    # pass the dialect to filereader to read the file
    reader = csv.reader(csvfile, dialect)
    # print(dialect)
    # Use for loop to print csv row by row
    for row in reader:
        #pprint.pprint("Estado: ",row[2])
        print ("Estado: %s\t Valor: %s" % (row[2],row[8]))