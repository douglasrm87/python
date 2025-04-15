from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("word count").setMaster("local[2]")
    sc = SparkContext(conf = conf)

    lines = sc.textFile("/workspaces/python/bigdata/spark/teste.txt")
    words = lines.flatMap(lambda line: line.split(" "))
    print ("Palavras:" ,words)
    wordCounts = words.countByValue()

    for word, count in wordCounts.items():
        print("{} : {}".format(word, count))