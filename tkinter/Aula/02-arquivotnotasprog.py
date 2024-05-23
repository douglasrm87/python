print ("oi")
def lerArquivo():
    arquivo = open("./02-arquivonotas.txt", "r" , encoding="utf8")
    conteudoLido = arquivo.readlines()
    for linha in conteudoLido:
        valores = linha.split(";")
        print (valores)
        qdadeItens = len (valores)
        if (qdadeItens == 3):
            media = (float (valores[1]) + float (valores[2]))/2
            print (media)
            if (media >= 6):
                print (valores [0] + " esta Aprovado.")
            else:
                print (valores [0] + " esta Reprovado.")
    arquivo.close()
    return conteudoLido
def gravarArquivo():
    #Abrindo Arquivo para leitura
    arquivo = open("./02-arquivonotas.txt", "w" , encoding="utf8")
    #Append novas linhas
    conteudoLido= lerArquivo()
    conteudoLido.append("\nSilvester Alone;50;60")
    conteudoLido.append("\nBradi Ping;80;40")
    #Gravando as linhas adicionais.
    arquivo.writelines(conteudoLido)
    arquivo.close()
lerArquivo()
gravarArquivo()
lerArquivo()
