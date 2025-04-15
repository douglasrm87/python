"""
author SparkByExamples.com
Instalar - pip install pyspark
"""

import matplotlib.pyplot as plt
import pandas as pd
import webbrowser
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

#Explicação
'''
O método .plot() que você está usando pertence ao pandas, mas ele utiliza internamente o matplotlib para renderizar o gráfico. Quando você chama tipoFlorGraf.plot(...), o pandas cria o gráfico e o associa ao contexto atual do matplotlib. Esse contexto é gerenciado automaticamente pela biblioteca matplotlib.pyplot, que você importou como plt.

Por isso:

Você não vê plt diretamente no código que cria o gráfico.
Mas o gráfico ainda aparece porque o pandas usa o contexto do matplotlib.pyplot para renderizá-lo.
Como isso funciona
O matplotlib.pyplot mantém um "estado global" para o gráfico atual. Quando o pandas cria o gráfico, ele usa esse estado global. Em seguida, quando você chama funções como plt.title() ou plt.savefig(), elas afetam o gráfico que está no estado global.
'''
# Salvar o gráfico em um arquivo
plt.savefig('/workspaces/python/bigdata/sparkgraficos/graficoGeneroBarra.png')

# Apresentar o gráfico em uma nova aba do navegador
