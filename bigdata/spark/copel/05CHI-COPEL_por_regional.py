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

Para o programa abaixo criado preciso que ajuste os seguintes pontos:
Desconsiderar do valor do CHI, quanto a diferença do CHI (n-m) por registro for menor ou igual a 2:59minutos. Menor que 2:59 minutos são chamadas de falhas momentaneas.
Desconsiderar os registros que tiver com a coluna D preenchida. A coluna D são dias criticos que a ANEEl desconsidera do valor do CHI


Para calcular o DEC dividir o valor do chi total pela quantidade de clientes faturados. usar 5278902 como clientes faturados.

'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    to_timestamp,
    trim,
    year,
    month,
    unix_timestamp,
    sum as spark_sum
)
from pyspark.sql.functions import round, lit
import matplotlib.pyplot as plt

# --------------------------------
# 1) Spark Session
# --------------------------------
spark = SparkSession.builder \
    .appName("CHI_Mensal_Por_Regional") \
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
# 3) Seleção e parsing das colunas
# --------------------------------
df_chi = df.select(
    to_timestamp(col("INT_014"), "dd/MM/yyyy HH:mm").alias("data_fim"),
    to_timestamp(col("INT_013"), "dd/MM/yyyy HH:mm").alias("data_ini"),
    col("regional").alias("regional"),
    col("INT_020").cast("double").alias("clientes"),
    col("INT_004").alias("dia_critico")  # ✅ Coluna D
)

# --------------------------------
# 4) Cálculo da duração (em minutos e horas)
# --------------------------------
df_chi = df_chi.withColumn(
    "duracao_minutos",
    (unix_timestamp("data_fim") - unix_timestamp("data_ini")) / 60
).withColumn(
    "duracao_horas",
    (unix_timestamp("data_fim") - unix_timestamp("data_ini")) / 3600
)

# --------------------------------
# 5) Filtros regulatórios
# --------------------------------

df_chi = df_chi.filter(
    (col("duracao_minutos") > 2.9833) &   # > 2:59 minutos  # ✅ Falhas não momentâneas
    (
        col("dia_critico").isNull() |       # ✅ Excluir dias críticos
        (trim(col("dia_critico")) == "")    # ✅ Excluir dias críticos
    )
)


# --------------------------------
# 6) Criar ano e mês
# --------------------------------
df_chi = df_chi.withColumn("ano", year(col("data_fim"))) \
               .withColumn("mes", month(col("data_fim")))

# --------------------------------
# 7) Cálculo do CHI
# --------------------------------
df_chi = df_chi.withColumn(
    "CHI",
    col("duracao_horas") * col("clientes")
)

# --------------------------------
# 8) Agregação mensal por regional
# --------------------------------
df_chi_mensal = df_chi.groupBy("ano", "mes", "regional") \
    .agg(
        round(spark_sum("CHI"), 2).alias("CHI_MENSAL")
    ) \
    .orderBy("ano", "mes", "regional")

df_chi_mensal.show(truncate=False)

# --------------------------------
# 8B) Agregação TOTAL por regional (sem mês)
# --------------------------------
df_chi_regional = df_chi.groupBy("regional") \
    .agg(
        round(spark_sum("CHI"), 2).alias("CHI_TOTAL_REGIONAL")
    ) \
    .orderBy("regional")

df_chi_regional.show(truncate=False)

# --------------------------------
# 9) Converter para Pandas
# --------------------------------
pdf = df_chi_mensal.toPandas()
pdf_regional = df_chi_regional.toPandas()

# --------------------------------
# 10) Formatação K / M (sem notação E)
# --------------------------------
def format_k_m(valor):
    if abs(valor) >= 1_000_000:
        return f"{valor/1_000_000:.2f} M"
    elif abs(valor) >= 1_000:
        return f"{valor/1_000:.2f} K"
    else:
        return f"{valor:.2f}"

pdf["CHI_FORMATADO"] = pdf["CHI_MENSAL"].apply(format_k_m).round(2)

pdf_regional["CHI_FORMATADO"] = pdf_regional["CHI_TOTAL_REGIONAL"].apply(format_k_m).round(2)


CLIENTES_FATURADOS = 5_278_902
#DEC por REGIONAL
df_chi_regional = df_chi.groupBy("regional") \
    .agg(
        round(spark_sum("CHI"), 2).alias("CHI_TOTAL_REGIONAL")
    ) \
    .withColumn(
        "DEC",
        round(col("CHI_TOTAL_REGIONAL") / lit(CLIENTES_FATURADOS), 2)
    ) \
    .orderBy("regional")

df_chi_regional.show(truncate=False)

#DEC TOTAL
df_chi_total = df_chi.agg(
    round(spark_sum("CHI"), 2).alias("CHI_TOTAL")
).withColumn(
    "DEC",
    round(col("CHI_TOTAL") / lit(CLIENTES_FATURADOS), 2)
)

df_chi_total.show(truncate=False)



# --------------------------------
# 11) Gráfico – CHI mensal por regional
# --------------------------------
plt.figure(figsize=(14, 7))

for regional in pdf["regional"].unique():
    dados = pdf[pdf["regional"] == regional]
    eixo_x = dados["ano"].astype(str) + "-" + dados["mes"].astype(str)
    plt.plot(eixo_x, dados["CHI_MENSAL"], marker="o", label=regional)

plt.title("CHI Mensal por Regional (ANEEL)")
plt.xlabel("Ano-Mês")
plt.ylabel("CHI")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))

plt.bar(
    pdf_regional["regional"],
    pdf_regional["CHI_TOTAL_REGIONAL"]
)

plt.title("CHI Total Consolidado por Regional (ANEEL)")
plt.xlabel("Regional")
plt.ylabel("CHI")
plt.grid(axis="y")
plt.tight_layout()
plt.show()



spark.stop()
