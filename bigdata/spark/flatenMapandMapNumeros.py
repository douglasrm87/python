from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Basic_Transformation").getOrCreate()
range_rdd=spark.sparkContext.range(3,10,1)
#print ("@@@@@@@@@@")
#print (range_rdd.collect())

#Add 100 to all the values in rdd
#range_rdd_t1 = range_rdd.map(lambda x: x+100)
#print ("@@@@@@@@@@")
#print (range_rdd_t1.collect())
#print (range_rdd_t1.take(5))

print ("@@@@@@@@@@")
rddMap = range_rdd.map(lambda x: (x,x*x , x+100)).collect()
print (rddMap)
print (rddMap[0])
print (rddMap[1])
print ("@@@@@@@@@@")
rddMap = range_rdd.flatMap(lambda x: (x,x*x , x+100)).collect()
print (rddMap)
print (rddMap[0])
print (rddMap[1])
