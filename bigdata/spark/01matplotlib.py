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
print (df)
exe01 = df.groupby(df["gênero"]).idade.agg(["min","max","sum","count","mean"])
print (exe01)
exe01.plot(kind='bar')
plt.show()