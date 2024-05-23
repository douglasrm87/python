dadosBolsa = [["AC","10,90"],
              ["PR","2,0"],
              ["AC","10,90"],
              ["BH","20,90"],
              ["BH","20,90"],
              ["PR","10,90"],
              ["PR","40,90"]]
estadoAnt = "AC"
dictBolsa = {"estado":"valor"}
acumulador = 0.0
for linha in sorted (dadosBolsa):
    linha [1] = linha [1].replace(",",".")
    if (estadoAnt == linha [0]):
        acumulador = acumulador + float(linha [1])
        dictBolsa.update({estadoAnt:acumulador})
    else:
        print ("Troca estado: %s\t%s" % (estadoAnt,acumulador))
        estadoAnt = linha [0]
        acumulador = float(linha [1])
print ("Troca estado ultimo: %s\t%s" % (estadoAnt,acumulador))


for k , v in dictBolsa.items():
    print (k,v)