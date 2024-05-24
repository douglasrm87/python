#Este programa irá imprimir todas as linhas do arquivo.
import csv 
import pprint
from datetime import datetime
acumulador = 0.0
estadoAnt = "AC"
def processar_linha(estado,valor):
    global estadoAnt
    global acumulador
    valor = valor.replace(",",".")
    if (estadoAnt == estado):
        acumulador = acumulador + float(valor)
        dictBolsa.update({estadoAnt:acumulador})
    else:
        print ("Troca estado: %s\t%s" % (estadoAnt,acumulador))
        estadoAnt = estado
        acumulador = float(valor)
dictBolsa = {estadoAnt: 0.0}            
def real_br_money_mask(my_value):
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')
# opens csv file and assingns it to an object
with open('C:/Users/dougl/Downloads/202101_BolsaFamilia_Pagamentos/202101_BolsaFamilia_Pagamentos.csv') as csvfile:
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
    iniciarEstado = 0
    for row in reader:
        #pprint.pprint("Estado: ",row[2])
        if (row[8]!= 'VALOR PARCELA'):
            if (iniciarEstado == 0):
                estadoAnt = row[2]
                iniciarEstado = iniciarEstado + 1
                #print ("Estado: [%s]\t Valor:[%s]" % (row[2].strip(),row[8].strip().replace(",",".")))
            processar_linha(row[2],row[8])
    for k, v in dictBolsa.items():
        print ("%s\t%s" % (k, real_br_money_mask(v)))
print ("Quantidade de linhas: ",contLinhas)
now = datetime.now()
print("now =", now)
print ("*********************")