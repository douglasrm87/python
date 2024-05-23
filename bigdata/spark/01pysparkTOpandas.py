import matplotlib.pyplot   as plt
import pyspark 
from pyspark.sql import SparkSession 
from pyspark.sql.types import StructType, StructField, StringType,IntegerType,FloatType    
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()    

dataStruct = [(("João","","carlos"),36636,"M",12500.90), 
(("Michael","Rose",""),40288,"M",1000.00), 
(("Douglas","Rocha","Mendes"),42114,"M",2000.00), 
(("Maria","Anne","Jones"),39192,"F",4000.00), 
(("Jenifer","Mary","Lopes"),1111,"F",1900.00) ]    
#https://sparkbyexamples.com/pyspark/pyspark-structtype-and-structfield/
schemaStruct = StructType([    
        StructField('nome', StructType([    
             StructField('primeironome', StringType(), True),    
             StructField('nomemeio', StringType(), True),    
             StructField('ultimonome', StringType(), True)    
             ])),    
          StructField('IDJob', IntegerType(), True),    
         StructField('Genero', StringType(), True),    
         StructField('Salario', FloatType(), True)    
         ])    
df = spark.createDataFrame(data=dataStruct, schema = schemaStruct)    
df.printSchema()    
pandasDF2 = df.toPandas()    
print(pandasDF2)

cores = ['pink', 'silver' ]
tipoFlorGraf = pandasDF2.groupby (["Genero"]).nome.count()
tipoFlorGraf.plot(kind='pie', autopct='%1.0f%%',colors=cores)

plt.show()

