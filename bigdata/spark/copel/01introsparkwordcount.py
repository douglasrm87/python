from pyspark import SparkContext, SparkConf
# pip install pyspark
#C:\Douglas\BackupDouglas\Desenvolvimento\jdk-17.0.18_windows-x64_bin\jdk-17.0.18\bin
#pip install pyspark --trusted-host pypi.org --trusted-host files.pythonhosted.org
#C:\Users\c049463\AppData\Local\Programs\Python\Python311
#pip install pandas --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyarrow --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyspark.pandas --trusted-host pypi.org --trusted-host files.pythonhosted.org
#pip install pyspark==3.5.5 --trusted-host pypi.org --trusted-host files.pythonhosted.org

conf = SparkConf().setAppName("WordCount").setMaster("local")
sc = SparkContext(conf=conf)    
# Carregar o arquivo de texto
text_file = sc.textFile("01introsparkwordcount.py")
# Contar as palavras
word_counts = text_file.flatMap(lambda line: line.split()) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)    
# Exibir os resultados
for word, count in word_counts.collect():
    print(f"{word}: {count}")
# Parar o SparkContext
sc.stop()

