arq = open ("./arqnotas.txt","r")
cont = arq.readlines()
print (cont)
arqAV3 = open ("./av3.txt","w")
for linha in cont:
	valores = linha.split(";") 
	qdadeItens = len (valores)
	if (qdadeItens > 3):
		print ("Nome:", valores [0],"AV1:",valores [1],"AV2:",valores [2],"AV3:",valores [3])
		av3 = "Nome:", valores [0],"AV1:",valores [1],"AV2:",valores [2],"AV3:",valores [3]
		arqAV3.writelines (av3)
arq.close()
arqAV3.close()

