"""
author SparkByExamples.com
Instalar - pip install pyspark
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    'nome': ['Paulo','Daniel','Maria','Lucas','Tiago','Marina','Julia','Carla'],
    'idade': [23,78,22,19,45,33,20,23],
    'gênero': ['M','M','F','M','M','F','F','F'],
    'estado': ['SP','RJ','SC','SP','PE','PR','PR','SP'],
    'criancas': [2,0,0,3,2,1,4,0],
    'animais': [1,2,3,5,1,2,1,2]
})
print ("Original DataFrame")
print (df)
exe01 = df.groupby(df["gênero"]).idade.agg(["min","max","sum","count","mean"])

print ("\n DataFrame Apos  groupby \n")
# para apresentar na cor vermelha.
print("\033[91m", exe01, "\033[0m")
# Criar um gráfico de barras para os dados de exe01
exe01.plot(kind='bar', figsize=(10, 6), color=['blue', 'orange', 'green', 'red', 'purple'])


# Adicionar título e rótulos aos eixos
plt.title('Estatísticas por Gênero', fontsize=16)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Valores', fontsize=12)

# Exibir o gráfico
plt.tight_layout()
plt.show()

