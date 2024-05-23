import matplotlib.pyplot   as plt
import pandas as pd 
import pyspark.pandas as ps 
dfPS = ps.read_csv('./bolsafamiliateste.csv',sep=";") 
dfPandas = dfPS.to_pandas() 
pandasGroupGraf = dfPandas.groupby("uf").valor.agg(["sum"]) 
pandasGroupGraf.plot (kind="pie",subplots=True,autopct = "%0.2f%%") 
plt.show()