from itertools import count
import pyspark.pandas as ps# Create a DataFrame with Pandas-on-Spark
from pyspark.sql import SparkSession
import matplotlib.pyplot   as plt
spark = SparkSession.builder.appName("Spark").getOrCreate()# For running Pandas on top of Spark

#Exemplos - https://sparkbyexamples.com/pyspark/select-columns-from-pyspark-dataframe/
# SPARK
sdf = spark.read.options(inferSchema='True',
              header='True').csv('./iris.csv')

# SPARK
resultado = sdf.select("*")# PANDAS-ON-SPARK
 
#converter o datarame para pandas
pandas = resultado.toPandas()
tipoFlor = pandas["variety"].unique()
print (tipoFlor)
print (type(tipoFlor))
#https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
plt.bar(pandas["variety"].unique(),len(tipoFlor), color ='green', width = 0.4)
plt.show()


