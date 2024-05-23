from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("word count").setMaster("local[2]")
sc = SparkContext(conf = conf)

text_file = sc.textFile("./bigdata.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("./bigdatasaida")
