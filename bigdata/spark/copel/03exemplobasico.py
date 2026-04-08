from pyspark.sql import SparkSession
# pip install pyspark
#C:\Douglas\BackupDouglas\Desenvolvimento\jdk-17.0.18_windows-x64_bin\jdk-17.0.18\bin
#pip install pyspark --trusted-host pypi.org --trusted-host files.pythonhosted.org
#C:\Users\c049463\AppData\Local\Programs\Python\Python311
#pip install pandas --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyarrow --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyspark.pandas --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyspark==3.5.5 --trusted-host pypi.org --trusted-host files.pythonhosted.org

spark = SparkSession.builder \
    .appName("TestePySpark") \
    .master("local[*]") \
    .getOrCreate()

df = spark.createDataFrame(
    [(1, "Douglas"), (2, "Spark")],
    ["id", "nome"]
)

df.show()

spark.stop()