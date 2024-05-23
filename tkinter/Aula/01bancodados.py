# importar driver​ 
import psycopg2 as psy

def add_comments(content):  
  conn=psy.connect (host='127.0.0.1',database='postgres',user='postgres',password='12345')    
  cursor = conn.cursor()
  #ursor.execute("insert into comments values ('$s')"% content)
  cursor.execute("insert into minha_cidade (nome_cidade,estado) values ('$s','$s')" % 1111 % 1111)
  conn.commit()
  conn.close()

# Conectar ao banco de dados.​   
conexao=psy.connect (host='127.0.0.1',database='postgres',user='postgres',password='12345')    
# estabelecendo um ambiente para executarmos comandos ​   
cursor=conexao.cursor()
print ("Conexão: ",conexao.fileno)

nome_cidade = "Maringá"
estado = "PR"
# usando parâmetros​   
inserir = "insert into minha_cidade (nome_cidade,estado) values (%s,%s)"
#a = 'Paranavai'
#cursor.execute(f"UPDATE minha_cidade SET estado={a} WHERE id=1")
#nome = 'João'
#cursor.execute(f"UPDATE cliente SET nome={nome} WHERE idcliente=13")

add_comments("Teste comentario")