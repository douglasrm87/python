def gravarAppendArquivo():
    try:
        arquivo = open("./02-arquivonotas.txt", "a" , encoding="utf8")
        arquivo.write("\nTchau pro tio Alone;50;60")
        arquivo.write("\nTrace route me;80;40")
        arquivo.close()
    except FileNotFoundError:
        print ("Arquivo não foi localizado.")
    except PermissionError:
        print ("Arquivo não possui permissão para gravação.")        

def lerArquivo():
    try:
        arquivo = open("./02-arquivonotas.txt", "r" , encoding="utf8")
        conteudoLido = arquivo.readlines()
        for linha in conteudoLido:
            print ("Linha lida: ",linha.split(";"))
        arquivo.close()
        return conteudoLido
    except FileNotFoundError ():
        print ("Arquivo não foi localizado.")
    except PermissionError:
        print ("Arquivo não possui permissão para leitura.")        
def gravarArquivo():
    try:
        #Append novas linhas
        conteudoLido= lerArquivo()
        #Abrindo Arquivo para gravação
        arquivo = open("./02-arquivonotas.txt", "w" , encoding="utf8")
        conteudoLido.append("\nSilvester Alone;50;60")
        conteudoLido.append("\nBradi Ping;80;40")
        #Gravando as linhas adicionais.
        arquivo.writelines(conteudoLido)
        arquivo.close()
    except FileNotFoundError:
        print ("Arquivo não foi localizado.")
    except PermissionError:
        print ("Arquivo não possui permissão para gravação.")        

#lerArquivo()
#gravarArquivo()
gravarAppendArquivo()
lerArquivo()
