acumulador = 0.0
estadoAnt = "AC"
def processarLinha(estado,valor):
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
dadosBolsa = [["AC","10,90"],["PR","2,0"],["AC","10,90"],["BH","20,90"],["BH","20,90"],["PR","10,90"],["PR","40,90"]]
# Com o arquivo real precisaremos tirar o sorted pelo tempo de processamento.
for linha in sorted (dadosBolsa):
    processarLinha(linha [0],linha [1])

print ("Troca estado ultimo: %s\t%s" % (estadoAnt,acumulador))

