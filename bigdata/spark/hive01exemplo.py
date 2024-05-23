import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
appName= "hive_pyspark"
master= "local"
spark = SparkSession.builder.master(master).appName(appName).enableHiveSupport().getOrCreate()
df=spark.sql("show databases")
df.show()

#criar o database faculdade
#spark.sql("create database faculdade").show()
#df=spark.sql("show databases")
spark.sql('use faculdade')
#criar tabelas
'''
spark.sql('create table movies \
         (movieId int,title string,genres string) \
         row format delimited fields terminated by ","\
         stored as textfile') 
spark.sql("create table ratings\
           (userId int,movieId int,rating float,timestamp string)\
           stored as ORC" )        
spark.sql("create table genres_by_count\
           ( genres string,count int)\
           stored as AVRO" )
 
'''
tables = spark.sql("show tables").show()
#spark.sql("describe formatted ratings").show(truncate = False)
#C:/Desenvolvimemto/Fontes/python/bigdata/spark/cinema.csv
# spark.sql("load data local inpath './cinema.csv'\
#                  overwrite into table movies")
# spark.sql("select * from movies limit 10").show(truncate = False)
print ("oi")