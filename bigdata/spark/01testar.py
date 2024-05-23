from pyspark import SparkContext
from pyspark.sql import HiveContext

sc = SparkContext()
SQLContext = HiveContext(sc)
SQLContext.setConf("spark.sql.hive.convertMetastoreOrc", "false")
txt = SQLContext.sql( "SELECT 1")
txt.show(2000000, False)