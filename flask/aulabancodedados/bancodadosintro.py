#python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip psycopg2-binary
#pip install psycopg2-binary
import psycopg2
con = psycopg2.connect(host='localhost', database='postgres',
user='postgres', password='12345')
cur = con.cursor()
#sql = 'drop table cidade'
#cur.execute(sql)
sql = 'create table cidade (id serial primary key, nome varchar(100), uf varchar(2))'
cur.execute(sql)
sql = "insert into cidade values (default,'Sao Paulo','SP')"
cur.execute(sql)
sql = "insert into cidade values (default,'Curitiba','PR')"
cur.execute(sql)
sql = "insert into cidade values (default,'Florianopolis','SC')"
cur.execute(sql)
con.commit()
cur.execute('select * from cidade')
vetor = cur.fetchall()
print ("Conteudo do vetor:",vetor)
print ("Tamanho do vetor:",len(vetor))
print ("Conteudo do vetor [0]:",vetor[0])
print ("Conteudo do vetor [1]:",vetor[1])
print ("Conteudo do vetor [1][2]. Estado:",vetor[1][2])
for rec in vetor:
    print (rec)
con.close()