
arquivo = open("C://Desenvolvimemto/Fontes/python/tkinter/arqnotas.txt", "r" , encoding="utf8")
#arquivo = open("./arqnotas.txt", "r" , encoding="utf8")​
conteudoAtual = arquivo.readlines()
print("\n\nDados Recuperados do arquivo primeira etapa: \n")
print(conteudoAtual)
print("\n") 
arquivo.close
conteudoAtual.append("Pedro Mendes;60;60\n")
conteudoAtual.append("Rafael Antunes;50;70\n")
conteudoAtual.append("Juliana Amora;75;75\n")
conteudoAtual.append("Beatriz Pacheco;85;85\n")
arquivo = open("C://Desenvolvimemto/Fontes/python/tkinter/arqnotas.txt", "w" , encoding="utf8")
arquivo.writelines(conteudoAtual)
arquivo.close
arquivo = open("C://Desenvolvimemto/Fontes/python/tkinter/arqnotas.txt", "r" , encoding="utf8")
print("\n\nLendo apenas os 6 primeiros caracters do nome, observe o ponteiro de leitura que mudar de posição: \n")
print(arquivo.readline(7))
print("\n\nDados Recuperados apos append: \n") 
print(arquivo.readlines()) 
arquivo.close