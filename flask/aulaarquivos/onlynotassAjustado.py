try:
	arquivo = open ("./onlynotass.txt")
	conteudo = arquivo.readlines()
	print ("Conteudo:", conteudo)
	conteudoArqSaida = list()
	for linha in conteudo:
		itens = linha.split(";")
		av1 = int (itens[1].strip())
		conteudoArqSaida.append ("Matricula: ")
		conteudoArqSaida.append (itens[0])
		conteudoArqSaida.append (";AV1:")
		conteudoArqSaida.append (str(av1))
		conteudoArqSaida.append (";AV1 ajustada:")
		conteudoArqSaida.append (str(av1 + 10))
		conteudoArqSaida.append ("\n")
	arqSaida = open ("./arqsaida.txt","w")
	arqSaida.writelines(conteudoArqSaida)
except Exception as e:
    print ("Erro:", e)