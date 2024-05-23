# Importar o módulo
import json
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType,IntegerType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()


# String em formato JSON
data_JSON =  """
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}
"""

# Converter a string em JSON em um dicionário
data_dict = json.loads(data_JSON)

print (data_dict)

print(data_dict["size"])
print(data_dict["price"])
print(data_dict["toppings"])
print(data_dict["client"])

# Read JSON file into dataframe
df = spark.read.json("./exjson.txt")
df.printSchema()
df.show()