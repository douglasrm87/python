#https://medium.com/team-data-stone/programa%C3%A7%C3%A3o-em-python-e-pyspark-681f4c405850
#https://www.linkedin.com/pulse/pyspark-primeiro-exemplo-fernando-anselmo/?trackingId=s0cDaliP0Oi901Wy%2B%2BtUoA%3D%3D
from pyspark.sql import SparkSession
spark = SparkSession.builder \
.appName("Python Spark SQL basic example") \
.config("spark.some.config.option", "some-value") \
.getOrCreate()
data = [1, 2, 3, 4, 5]
distData = spark.sparkContext.parallelize(data)

print ("oi)")


# importing necessary libraries
from pyspark.sql import SparkSession
 
# function to create SparkSession
def create_session():
  spk = SparkSession.builder \
      .master("spark://192.168.15.66:7077") \
      .appName("Products.com") \
      .getOrCreate()
  return spk
 
# function to create Dataframe
def create_df(spark,data,schema):
  df1 = spark.createDataFrame(data,schema)
  return df1
 
# main function
if __name__ == "__main__":
 
  # calling function to create SparkSession
  spark = create_session()
     
  input_data = [(1,"Direct-Cool Single Door Refrigerator",12499),
          (2,"Full HD Smart LED TV",49999),
          (3,"8.5 kg Washing Machine",69999),
          (4,"T-shirt",1999),
          (5,"Jeans",3999),
          (6,"Men's Running Shoes",1499),
          (7,"Combo Pack Face Mask",999)]
 
  schm = ["Id","Product Name","Price"]
 
  # calling function to create dataframe
  df = create_df(spark,input_data,schm)
  df.show()
 
  # extracting number of rows from the Dataframe
  row = df.count()
   
  # extracting number of columns from the Dataframe
  col = len(df.columns)
 
  # printing
  print(f'Dimension of the Dataframe is: {(row,col)}')
  print(f'Number of Rows are: {row}')
  print(f'Number of Columns are: {col}')
