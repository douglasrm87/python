dadosBolsa = [ ["AC","10,90"]
              ,["AC","40,90"]
              ,["AC","66,80"]]

dictBolsa = {"estado":"valor"}
acumulador = 0.0
for linha in dadosBolsa:
    print (linha)
    linha [1] = linha [1].replace (",",".")
    acumulador = acumulador + float(linha [1])
print (acumulador)
for k , v in dictBolsa.items():
    print (k,v)