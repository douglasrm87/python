'''
#Este programa irá imprimir todas as linhas do arquivo.
import csv 
# opens csv file and assingns it to an object
with open('/workspaces/python/Replica/CLIC_ATUALIZA_DIA_ELEK.csv') as csvfile:
    # Use Sniffer to figure out csv dialect
    # lendo blocos de 1K
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    #Posicionar na primeira posição do arquivo.
    csvfile.seek(0)
    # pass the dialect to filereader to read the file
    reader = csv.reader(csvfile, dialect)
    # print(dialect)
    # Use for loop to print csv row by row
    for row in reader:
        print (row)
 
 '''
import pandas as pd

# Carregar o arquivo CSV usando '|' como separador
df = pd.read_csv('/workspaces/python/Replica/CLIC_ATUALIZA_DIA_ELEK.csv', sep='|')

# Exibir as primeiras 10 linhas do DataFrame de forma didática
print("Visualização das primeiras 10 linhas do arquivo:")
#print(df.head(10).to_string(index=False))
print("\nConteúdo da coluna 13:")

# Exibir os nomes das colunas 12 e 13 (índices 11 e 12)
coluna = 15
print(f"Nome da coluna: {df.columns[coluna]}")
print("\nConteúdo da coluna:")
print(df.head(5).iloc[:, coluna].to_string(index=False)) #  Exibir o conteúdo da coluna 13
print("\nInformações gerais sobre os dados:")
print(df.info())
'''
# Exibir o conteúdo das colunas 12 e 13
print("\nConteúdo da coluna 12:")
print(df.iloc[:, 11].to_string(index=False))

print("\nConteúdo da coluna 13:")
print(df.iloc[:, 12].to_string(index=False))


'''
 
