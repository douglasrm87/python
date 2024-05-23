# importar driver​ 
import psycopg2 as psy
# Conectar ao banco de dados.​   
conexao=psy.connect (host='127.0.0.1',database='postgres',user='postgres',password='12345')    
# estabelecendo um ambiente para executarmos comandos ​   
cursor=conexao.cursor()
try:
    # Executando um comando DDL - Data Definiton Language​   
    criarTabela = 'create table minha_cidade (id serial primary key , nome_cidade varchar (100) , estado varchar (2) )'
    # Executar a query DML​   
    cursor.execute (criarTabela)
    conexao.commit()
except Exception as e:
    print ("Tabela já criada.")
    conexao.rollback()

nome_cidade = "Jandaia do Sul"
estado = "PR"
# usando parâmetros​   
inserir = "insert into minha_cidade (nome_cidade,estado) values (%s,%s)"
# Executar a query DML​   
cursor.execute (inserir,(nome_cidade,estado))
inserir = "insert into minha_cidade (nome_cidade,estado) values ('Cascavel','PR')"
# Executar a query DML​
cursor.execute (inserir)

# Permitira SQL Injection​
conteudo = "Cascavel"
cursor.execute ("insert into minha_cidade (nome_cidade) values ('%s')" % conteudo)
conteudo = "'Apucarana','PR'"
cursor.execute ("insert into minha_cidade (nome_cidade,estado)  values (%s)" % conteudo)
conteudo = "'Kalore','PR'"
cursor.execute ("insert into minha_cidade (nome_cidade,estado)  values (" + conteudo + ")")

# Sem SQL Injection​
conteudo = "Apucarana"
estado = "PR"
cursor.execute ('insert into minha_cidade (nome_cidade,estado) values (%s,%s)', (conteudo,estado,))


#Efetivando as alterações
conexao.commit()
selecionar="select * from minha_cidade"
cursor.execute (selecionar)
registros = cursor.fetchall()
for reg  in registros:
    print ("Registro lido:",reg)
conexao.close()

#Efetivando as alterações
conexao.commit()
selecionar="select * from minha_cidade"
cursor.execute (selecionar)
registros = cursor.fetchall()
for reg  in registros:
    print ("Registro lido:",reg)
conexao.close()