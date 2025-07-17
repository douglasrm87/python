
import pandas as pd

# Carregar o arquivo CSV usando '|' como separador
df = pd.read_csv('/workspaces/python/Replica/CLIC_ATUALIZA_DIA_CONTATO.csv', sep='|')

# Exibir as primeiras 10 linhas do DataFrame de forma didática
print("Visualização das primeiras 10 linhas do arquivo:")
#print(df.head(10).to_string(index=False))
print("\nConteúdo da coluna 13:")

'''
# Exibir os nomes das colunas 12 e 13 (índices 11 e 12)
print(f"Nome da coluna 13: {df.columns[13]}")
print("\nConteúdo da coluna 13:")
print(df.iloc[:, 13].to_string(index=False)) #  Exibir o conteúdo da coluna 13
'''
print("\nInformações gerais sobre os dados:")
print(df.info())
