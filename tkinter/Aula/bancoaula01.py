# importar driver
import psycopg2 as psy
def funcaoInserir (cidade,estado,cursor):
    sql = "insert into minha_cidade values (default,%s,%s)"
    cursor.execute(sql, (cidade, estado))
# Conectar ao banco de dados.
conexao=psy.connect (host='127.0.0.1',database='postgres',
user='postgres', password='12345')
# estabelecendo um ambiente para executarmos comandos
cursor=conexao.cursor()
try:
    # Executando um comando DDL - Data Definiton Language
    criarTabela = 'create table minha_cidade (id serial primary key , nome_cidade varchar (100) ,  estado varchar (2) )'
    # Executar a query DML
    cursor.execute (criarTabela)
    conexao.commit()
    print ("Tabela criada comk sucesso.")
except Exception as e:
    print ("Tabela já criada. Mensagem: ",e)
    conexao.rollback()

funcaoInserir ("Apucarana","SC",cursor)
funcaoInserir ("Camburiu","SC",cursor)

conexao.commit()
cursor.execute('select * from minha_cidade')
recset = cursor.fetchall()  
for rec in recset:
    print ("Dados recuyperados:",rec)
    conexao.close()