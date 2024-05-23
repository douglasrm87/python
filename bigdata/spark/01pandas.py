import matplotlib.pyplot   as plt
import pandas as pd
import pyspark.pandas as ps

dfPS = ps.read_csv('./bolsafamiliateste.csv',sep=";")

dfPandas = dfPS.to_pandas()
#https://sparkbyexamples.com/pyspark/pyspark-groupby-explained-with-example/
# Acumula o valor porem manter as demais colunas.
# pandasGroupA = dfPandas.groupby("uf").sum("valor")
# print (pandasGroupA)
# print (type (pandasGroupA))
# #https://datatofish.com/convert-pandas-dataframe-to-list/
# lista = pandasGroupA.values.tolist()
# for linha in lista:
#    print (linha[0], " ",linha[1], " ",linha[2], " ",linha[3], " ",linha[4])

# print (pandasGroupA.columns)

# Obte apenmas as 2 colunas (uf e valor somado) para o gráfico
pandasGroupGraf = dfPandas.groupby("uf").valor.agg(["sum"])
print (pandasGroupGraf)
print (type (pandasGroupGraf))
pandasGroupGraf.plot (kind="bar")
plt.show()
