# importar driver
import psycopg2 as psy
# Conectar ao banco de dados.
conexao=psy.connect (host='127.0.0.1',database='postgres',user='postgres',password='12345')
print ("oi")
