dadosBolsa = [ ["AC","10,90"]
              ,["AC","40,90"]
              ,["AC","66,80"]]

dictBolsa = {"estado":"valor"}
for linha in dadosBolsa:
    print (linha)

for k , v in dictBolsa.items():
    print (k,v)