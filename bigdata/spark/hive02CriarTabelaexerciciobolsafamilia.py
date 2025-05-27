import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
appName= "hive_pyspark"
master= "local"
spark = SparkSession.builder.master(master).appName(appName).enableHiveSupport().getOrCreate()
df=spark.sql("show databases")
df.show()
spark.sql('use faculdade')
spark.sql('drop table bolsafamilia ') 
spark.sql('create table bolsafamilia \
         (mes_competencia int,mes_referencia int, uf string,codigo_municipio int,nome_municipio string, ' \
         'cpf string, nis_favorecido int , nome_favorecido string, valor_parcela float) \
         row format delimited fields terminated by ";"\
         stored as textfile') 

 
tables = spark.sql("show tables").show()

spark.sql("describe formatted bolsafamilia").show(truncate = False)
print ("Tabela Criada")