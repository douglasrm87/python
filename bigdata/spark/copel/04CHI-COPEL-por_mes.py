from pyspark.sql import SparkSession
# pip install pyspark
#C:\Douglas\BackupDouglas\Desenvolvimento\jdk-17.0.18_windows-x64_bin\jdk-17.0.18\bin
#pip install pyspark --trusted-host pypi.org --trusted-host files.pythonhosted.org
#C:\Users\c049463\AppData\Local\Programs\Python\Python311
#pip install pandas --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyarrow --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyspark.pandas --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyspark==3.5.5 --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install matplotlib --trusted-host pypi.org --trusted-host files.pythonhosted.org


'''
Apresentar em formato de mil ou milhão. Não usar a notação E. 
Somar todos os valores de chi do mês e agrupar por regional (coluna Z).
Para calcular o DEC dividir o valor do chi total pela quantidade de clientes faturados. usar 5278902 como clientes faturados.
Desconsiderar na conta total se a diferença do CHI por registro for menor ou igual a 2:59minutos. Este tratamos como Falha momentanea (FM)
Desconsiderar os registros que tiver com a coluna D preenchida.

'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, to_timestamp, to_date, sum as spark_sum
)
import matplotlib.pyplot as plt

# --------------------------------
# 1) Spark Session
# --------------------------------
spark = SparkSession.builder \
    .appName("Calculo_CHI_Interrupcoes") \
    .master("local[*]") \
    .config("spark.sql.session.timeZone", "America/Sao_Paulo") \
    .getOrCreate()

# --------------------------------
# 2) Leitura do CSV
# --------------------------------
df = spark.read.option("header", True) \
               .option("sep", ";") \
               .option("inferSchema", True) \
               .csv("BDO_INTERRUPCOES.csv")

# --------------------------------
# 3) Parse correto de data + hora
# --------------------------------
df_chi = df.select(
    to_timestamp(col("INT_013"), "dd/MM/yyyy HH:mm").alias("data_hora"),
    col("INT_021").cast("double").alias("N"),
    col("INT_020").cast("double").alias("M"),
    col("INT_022").cast("double").alias("T")
)

# --------------------------------
# 4) Extrair apenas a data
# --------------------------------
df_chi = df_chi.withColumn(
    "data",
    to_date(col("data_hora"))
)

# --------------------------------
# 5) Cálculo do CHI
# --------------------------------
df_chi = df_chi.withColumn(
    "CHI",
    ((col("N") - col("M")) * 24) * col("T")
)

# --------------------------------
# 6) Agregação diária
# --------------------------------
df_chi_dia = df_chi.groupBy("data") \
    .agg(
        spark_sum("CHI").alias("CHI_TOTAL_DIA")
    ) \
    .orderBy("data")

df_chi_dia.show(truncate=False)

# --------------------------------
# 7) Gráfico
# --------------------------------
pdf = df_chi_dia.toPandas()

plt.figure(figsize=(12, 6))
plt.plot(pdf["data"], pdf["CHI_TOTAL_DIA"], marker="o")
plt.title("CHI Diário – Cliente Hora Interrupção")
plt.xlabel("Data")
plt.ylabel("CHI")
plt.grid(True)
plt.tight_layout()
plt.show()

spark.stop()