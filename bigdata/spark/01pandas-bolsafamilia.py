import matplotlib.pyplot as plt
import pandas as pd

# Carregar o arquivo CSV diretamente com pandas
dfPandas = pd.read_csv('/workspaces/python/bigdata/spark/bolsafamiliateste.csv', sep=";")

# Atenção:
#  A variável plt parece "desconectada" do gráfico porque o método plot está sendo chamado diretamente no objeto retornado por pandasDF2.groupby(...).nome.count(). Isso pode ser confuso, mas é importante entender como o matplotlib e o pandas interagem.
#  O método plot() do pandas retorna um objeto matplotlib, mas não o exibe automaticamente. Para exibir o gráfico, você deve chamar plt.show() após a criação do gráfico.

# Agrupar os dados por "uf" e somar os valores
pandasGroupGraf = dfPandas.groupby("uf")["valor"].sum()
print(pandasGroupGraf)
print(type(pandasGroupGraf))

# Criar o gráfico de barras
pandasGroupGraf.plot(kind="bar")
plt.xlabel("UF")
plt.ylabel("Valor Total")
plt.title("Valores Totais por UF")
plt.savefig('/workspaces/python/bigdata/sparkgraficos/bolsafamilia01.png')
