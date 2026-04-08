# pip install pyspark
#C:\Douglas\BackupDouglas\Desenvolvimento\jdk-17.0.18_windows-x64_bin\jdk-17.0.18\bin
#pip install pyspark --trusted-host pypi.org --trusted-host files.pythonhosted.org
#C:\Users\c049463\AppData\Local\Programs\Python\Python311
#pip install pandas --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyarrow --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyspark.pandas --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyspark==3.5.5 --trusted-host pypi.org --trusted-host files.pythonhosted.org

'''
pip uninstall numpy -y --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install numpy==1.26.4 --trusted-host pypi.org --trusted-host files.pythonhosted.org

'''
from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder \
    .appName("TestePySpark") \
    .master("local[*]") \
    .getOrCreate()

# Spark DataFrame
df = spark.createDataFrame(
    [(1, "Douglas"), (2, "Spark")],
    ["id", "nome"]
)
df.show()

# Pandas DataFrame (normal)
pdf = pd.DataFrame({
    "id": [1, 2, 3],
    "nome": ["Alice", "Bob", "Charlie"]
})

# Converter Pandas → Spark
sdf = spark.createDataFrame(pdf)
sdf.show()

spark.stop()
