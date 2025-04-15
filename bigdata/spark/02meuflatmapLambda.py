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


    '''
    O método flatMap é uma operação amplamente utilizada em frameworks de processamento distribuído, como o PySpark, para transformar e manipular dados em um RDD (Resilient Distributed Dataset). Ele combina duas operações em uma: aplicar uma função a cada elemento do RDD e "achatar" os resultados (ou seja, transformar listas de listas em uma única lista).

Papel do flatMap
Aplicação de uma função: Ele aplica uma função fornecida (f) a cada elemento do RDD. Essa função deve retornar uma coleção (como uma lista, tupla ou outro iterável) para cada elemento.

Flattening (achatamento): Após aplicar a função, o flatMap "achata" os resultados, ou seja, combina todas as coleções retornadas em um único RDD contínuo. Isso é diferente do método map, que preserva a estrutura de listas aninhadas.

Diferença entre map e flatMap
map: Retorna um RDD onde cada elemento é o resultado direto da função aplicada. Se a função retornar uma lista, o RDD conterá listas como elementos.
flatMap: Retorna um RDD onde os elementos das listas retornadas pela função são "desempacotados" e adicionados diretamente ao RDD.
Exemplo prático
Usando map:
Aqui, o map preserva a estrutura de listas aninhadas.

Usando flatMap:
O flatMap "achata" os resultados, retornando um único RDD com todos os elementos.

Como funciona internamente
No código fornecido:

A função func é definida para ser aplicada a cada partição do RDD.
A função mapPartitionsWithIndex aplica func a cada partição, garantindo que os resultados sejam achatados usando chain.from_iterable.
Quando usar flatMap
Quando você precisa transformar cada elemento em múltiplos elementos.
Quando deseja evitar listas aninhadas no resultado.
Exemplos comuns incluem:
Dividir strings em palavras.
Expandir ranges ou intervalos.
Gerar combinações ou pares.
Exemplo mais detalhado
Imagine que você tem um RDD com frases e deseja obter uma lista de palavras:

Aqui, o flatMap divide cada frase em palavras e "achata" o resultado em um único RDD.

Conclusão
O flatMap é uma ferramenta poderosa para transformar dados em pipelines distribuídos, especialmente quando você precisa lidar com coleções aninhadas ou gerar múltiplos elementos a partir de um único elemento.
    '''