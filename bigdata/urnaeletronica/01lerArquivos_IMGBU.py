# TSE
# https://dadosabertos.tse.jus.br/dataset/resultados-2022-arquivos-transmitidos-para-totalizacao
# Arquivos com a extensão imgbu segundo turno - 34.423 arquivos.
# 	https://pt.stackoverflow.com/questions/251807/python-abrir-m%C3%BAltiplos-arquivos-em-um-for


from pathlib import Path

caminho = Path("./") # diretório local
arquivos = caminho.glob("*.imgbu")
for lista in arquivos:
    print (lista)
