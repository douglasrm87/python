import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
appName= "hive_pyspark"
master= "local"
spark = SparkSession.builder.master(master).appName(appName).enableHiveSupport().getOrCreate()
spark.sql('use faculdade')
#tables = spark.sql("show tables").show()

#spark.sql("load data local inpath './202501_NovoBolsaFamilia.csv'\
#spark.sql("load data local inpath './amostrabolsafamilia2025JAN.csv'
          
spark.sql("load data local inpath './amostrabolsafamilia2025JAN.csv'\
                 overwrite into table bolsafamilia")
spark.sql("select count (*) from bolsafamilia").show(truncate = False)

spark.sql("select * from bolsafamilia where nome_favorecido = '\"FERNANDA RAMOS TEIXEIRA\"'").show(truncate = False)
print ("Dados selecionados")