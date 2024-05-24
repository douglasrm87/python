#Fonte da planilha: https://www.portaltransparencia.gov.br/download-de-dados/bolsa-familia-pagamentos
# Este programa usou recursos para evitar o erro: csv.Error: unknown dialect

import csv

# opens csv file and assingns it to an object
with open('C:/Desenvolvimemto/Fontes/python/bigdata/hadoopBolsaFamilia/testebolsafamilia.csv') as csvfile:
    # Use Sniffer to figure out csv dialect
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    # pass the dialect to filereader to read the file
    reader = csv.reader(csvfile, dialect)
    # print(dialect)
    iniciarEstado = 0 # necesario para ignorar a primeira linha da planilha e iniciar Estado
    #for row in sorted (reader):
    for row in reader:
        #pprint.pprint("Estado: ",row[2])
        if (row[8]!= 'VALOR PARCELA'):
            if (iniciarEstado == 0):
                estadoAnt = row[2]
                iniciarEstado = iniciarEstado + 1
            #print ("Estado: [%s]\t Valor:[%s]" % (row[2].strip(),row[8].strip().replace(",",".")))
            print ("%s:%s" % (row[2].strip(),row[8].strip().replace(",",".")))