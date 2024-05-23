# import Pandas-on-Spark
# ps_df = ps.DataFrame(range(10))# Convert a Pandas-on-Spark Dataframe into a Pandas Dataframe
# pd_df = ps_df.to_pandas()# Convert a Pandas Dataframe into a Pandas-on-Spark Dataframe
# ps_df = ps.from_pandas(pd_df)

# Create a DataFrame with Pandas-on-Spark
# ps_df = ps.DataFrame(range(10))# Convert a Pandas-on-Spark Dataframe into a Spark Dataframe
# spark_df = ps_df.to_spark()# Convert a Spark Dataframe into a Pandas-on-Spark Dataframe
# ps_df_new = spark_df.to_pandas_on_spark()
# import pyspark.pandas as ps

import pyspark.pandas as ps# Create a DataFrame with Pandas-on-Spark

# For running Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark").getOrCreate()# For running Pandas on top of Spark

# SPARK
sdf = spark.read.options(inferSchema='True',
              header='True').csv('./iris.csv')# PANDAS-ON-SPARK
pdf = ps.read_csv('./iris.csv')

# SPARK
sdf.select("sepal_length","sepal_width").show()# PANDAS-ON-SPARK
cab = pdf[["sepal_length","sepal_width"]].head()
print (cab)

# SPARK
sdf.drop('sepal_length').show()# PANDAS-ON-SPARK
rem = pdf.drop('sepal_length').head()
print (rem)

# SPARK
sdf.union(sdf)# PANDAS-ON-SPARK
unir = pdf.append(pdf)
print (unir)



