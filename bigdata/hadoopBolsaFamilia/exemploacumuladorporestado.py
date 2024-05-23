
dadosBolsa = [["AC","10,90"],["PR","2,0"],["AC","10,90"],["BH","20,90"],["BH","20,90"],["PR","10,90"],["PR","40,90"]]

acumulador = 0.0
estadoAnt = "AC"
dictBolsa = {estadoAnt: 0.0}

# sorted garante que mesmo que tenhamos uma linha de um estado fora da ordem ficará na ordem
for linha in sorted (dadosBolsa):
    #Os valores vem do arquivo com vírgula
    linha [1] = linha [1].replace(",",".")
    if (estadoAnt == linha [0]):
        acumulador = acumulador + float(linha [1])
        dictBolsa.update({estadoAnt:acumulador})
    else:
        print ("Troca estado: %s\t%s" % (estadoAnt,acumulador))
        estadoAnt = linha [0]
        acumulador = float(linha [1])
        
print ("Troca estado ultimo: %s\t%s" % (estadoAnt,acumulador))
   

for k, v in dictBolsa.items():
    print(k, v)
