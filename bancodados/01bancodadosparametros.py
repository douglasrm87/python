import psycopg2
con = psycopg2.connect(host='localhost', database='postgres',
			user='postgres', password='12345')
cur = con.cursor()

sql = "insert into cidade (nome,uf) values (%s,%s)"
cur.execute(sql,("Rio de Janeiro","RJ"))
 
con.commit()
cur.execute('select * from cidade')
recset = cur.fetchall()
for rec in recset:
    print (rec)
con.close()

