from pyspark import SparkContext, SparkConf
import random

conf = SparkConf().setAppName("word count").setMaster("local[2]")
sc = SparkContext(conf = conf)
def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = sc.parallelize(range(0, 10)) \
             .filter(inside).count()
print("******************************")
print("Pi is roughly %f" % (4.0 * count / 20))
print("******************************")