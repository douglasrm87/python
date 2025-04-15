import matplotlib.pyplot   as plt
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

# Atenção:
#  A variável plt parece "desconectada" do gráfico porque o método plot está sendo chamado diretamente no objeto retornado por pandasDF2.groupby(...).nome.count(). Isso pode ser confuso, mas é importante entender como o matplotlib e o pandas interagem.
#  O método plot() do pandas retorna um objeto matplotlib, mas não o exibe automaticamente. Para exibir o gráfico, você deve chamar plt.show() após a criação do gráfico.

tipoFlorGraf = pandasDF2.groupby (["Genero"]).nome.count()
tipoFlorGraf.plot(kind='pie', autopct='%1.0f%%',colors=cores)

plt.title("Distribuição de Gêneros")
plt.ylabel("")
plt.xlabel("")
plt.legend(title="Gênero", loc="upper right")
plt.savefig('/workspaces/python/bigdata/sparkgraficos/pysparkTOpandas.png')
