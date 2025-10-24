try:  # tenta executar este bloco e captura erro se o arquivo não existir
    arquivo = open("./onlynotass.txt")  # abre o arquivo "onlynotass.txt" para leitura
    conteudo = arquivo.readlines()  # lê todas as linhas do arquivo e guarda numa lista
    print("Conteudo:", conteudo)  # mostra na tela o conteúdo bruto lido (lista de linhas)
    for linha in conteudo:  # percorre cada linha da lista de linhas
        itens = linha.split(";")  # separa a linha em campos usando ';' como delimitador
        av1 = int(itens[1].strip())  # pega o segundo campo, remove espaços e converte pra inteiro
        print("Matricula: ", itens[0], "AV1:" ,av1 , "AV1 ajustada:", av1 + 10)  # imprime matrícula, AV1 e AV1 ajustada (+10)
except FileNotFoundError as e:  # trata o caso em que o arquivo não foi encontrado
    print("Arquivo não encontrado, verificar.")  # avisa que o arquivo não existe ou caminho está errado
    print ("Erro:", e)  # imprime a mensagem de erro detalhada
except IOError as e:  # trata erros de entrada/saída
    print("Erro ao ler o arquivo. Sem acesso a pastas.")  # avisa que houve um erro ao tentar ler o arquivo     
    print ("Erro:", e)  # imprime a mensagem de erro detalhada
except IndexError as e:  # trata erros de índice fora do intervalo
    print("Erro ao processar linha: índice fora do intervalo.") # avisa que houve um erro ao acessar campos da linha
    print("Linha com erro:", linha)  # imprime a linha que causou o erro
    print("Itens extraídos:", itens)  # imprime os itens extraídos da linha
    print ("Erro:", e)  # imprime a mensagem de erro detalhada

except Exception as e:  # captura qualquer outro erro
    print("Ocorreu um erro:", e)