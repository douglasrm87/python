"""
author SparkByExamples.com
Instalar - pip install pyspark
"""

import pandas as pd    
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Dados para o DataFrame
data = [['Scott', 50], ['Jeff', 45], ['Thomas', 54], ['Ann', 34]]

# Criar o DataFrame do Pandas
pandasDF = pd.DataFrame(data, columns=['Name', 'Age'])
print("DataFrame Pandas:")
print(pandasDF)

# Criar a SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()

# Converter o DataFrame do Pandas para um DataFrame do Spark
sparkDF = spark.createDataFrame(pandasDF)
print("Schema do DataFrame Spark:")
sparkDF.printSchema()
print("Conteúdo do DataFrame Spark:")
sparkDF.show()

# Definir um schema personalizado
mySchema = StructType([
    StructField("First Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])

# Criar um DataFrame do Spark com o schema personalizado
sparkDF2 = spark.createDataFrame(pandasDF, schema=mySchema)
print("Schema do DataFrame Spark com schema personalizado:")
sparkDF2.printSchema()
print("Conteúdo do DataFrame Spark com schema personalizado:")
sparkDF2.show()

# Configurações do Arrow para otimizar a conversão entre Spark e Pandas
spark.conf.set("spark.sql.execution.arrow.enabled", "true")
spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled", "true")

# Converter o DataFrame do Spark para um DataFrame do Pandas usando Arrow
pandasDF2 = sparkDF2.toPandas()
print("DataFrame Pandas convertido do Spark:")
print(pandasDF2)

# Verificar as configurações do Arrow
arrow_enabled = spark.conf.get("spark.sql.execution.arrow.enabled")
print(f"Arrow Enabled: {arrow_enabled}")

arrow_fallback = spark.conf.get("spark.sql.execution.arrow.pyspark.fallback.enabled")
print(f"Arrow Fallback Enabled: {arrow_fallback}")