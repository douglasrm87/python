# importar driver​ 
import psycopg2 as psy
from datetime import date, datetime, timedelta

# Conectar ao banco de dados.​   
conexao=psy.connect (host='127.0.0.1',database='postgres',user='postgres',password='12345')    
# estabelecendo um ambiente para executarmos comandos ​   
cursor=conexao.cursor()
try:
    # Executando um comando DDL - Data Definiton Language​   
    criarTabela = 'create table carro  (id serial primary key , nome varchar (100) , data_fabricacao timestamp )'
    # Executar a query DML​   
    cursor.execute (criarTabela)
    conexao.commit()
except Exception as e:
    print ("Tabela já criada.", e)
    conexao.rollback()

# usando parâmetros​   
nome = "Ranger"
cursor.execute ("insert into carro (nome,data_fabricacao) values (%s,%s)", (nome,datetime.now().date()))
nome = "Fusca"
tomorrow = datetime.now().date() + timedelta(days=1)
cursor.execute ("insert into carro (nome,data_fabricacao) values (%s,%s)", (nome,tomorrow))

#Efetivando as alterações
conexao.commit()
selecionar="select * from carro"
cursor.execute (selecionar)
registros = cursor.fetchall()
for reg  in registros:
    print ("Registro lido:",reg)
conexao.close()
