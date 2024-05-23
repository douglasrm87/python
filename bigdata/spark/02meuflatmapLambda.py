from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("word count").setMaster("local[2]")
    sc = SparkContext(conf = conf)

    data = ["Project Douglas’s",
        "Alice’s Adventures in Wonderland",
        "Project Douglas’s",
        "Adventures in Wonderland",
        "Project Douglas’s"]
    rdd=sc.parallelize(data)
    print ("**************")
    for element in rdd.collect():
        print(element)
    print ("*****Contando as palavras*********")
    rdd2=rdd.flatMap(lambda x: x.split(" "))
    palavras = rdd2.countByValue()
    for palavra,valor in palavras.items():
        print("{} : {} ".format (palavra , valor ))
    print ("**************")