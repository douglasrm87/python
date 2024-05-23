#https://medium.com/@vk.sajin/pyspark-basics-map-flatmap-99bf3697afa0
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Basic_Transformation").getOrCreate()

text_df= spark.read.text('./flatemap.txt')
text_df.take(5)
print ("**********************")
print ("Tipo de dado",type(text_df))
print ("**********************")
text_rdd = text_df.rdd
print ("Tipo de dado",type(text_df))
print ("**********************")
exSem= text_rdd.collect()
print ("Conteúdo Arquivo Sem Map: ",exSem)
print ("Conteúdo Arquivo Sem Map [0]: ",exSem[0])
print ("**********************")
exMap = text_rdd.map(lambda x : x.value.split()).collect()
print ("Conteúdo Arquivo COM Map: ",exMap)
print ("Conteúdo Arquivo COM Map [0]: ",exMap[0])
print ("**********************")
exflatMap = text_rdd.flatMap(lambda x : x.value.split()).collect()
print ("Conteúdo Arquivo COM flatMap: ", exflatMap)
print ("Conteúdo Arquivo COM flatMap [0]: ",exflatMap[0])