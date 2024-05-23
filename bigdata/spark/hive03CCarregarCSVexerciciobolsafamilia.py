import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
appName= "hive_pyspark"
master= "local"
spark = SparkSession.builder.master(master).appName(appName).enableHiveSupport().getOrCreate()
spark.sql('use faculdade')
 
spark.sql("load data local inpath './bolsafamiliateste.csv'\
                 overwrite into table bolsafamilia")
spark.sql("select * from bolsafamilia").show(truncate = False)
print ("Dados selecionados")