import csv  

import pprint  

acumulador = 0.0  

estadoAnt = None  

def processarLinha(estado,valor):  

    global estadoAnt  

    global acumulador  

    estado = estado.strip()  

    valor = valor.strip().replace(",",".")  

    if (estadoAnt == estado):  

        acumulador = acumulador + float(valor)  

        dictBolsa.update({estadoAnt:acumulador})  

    else:  

        #print ("Troca estado: %s\t%s" % (estadoAnt,acumulador))  

        estadoAnt = estado  

        acumulador = float(valor)  

dictBolsa = {estadoAnt: 0.0}  

# opens csv file and assingns it to an object  

with open('202101_BolsaFamilia_Pagamentos.csv') as csvfile:  

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

            processarLinha(row[2],row[8])  

    for k, v in dictBolsa.items():  

        print ("%s\t%s" % (k, v))  