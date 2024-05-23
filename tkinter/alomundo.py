
import psycopg2 as psy
class Conexao(object):
    _db=None
    def __init__(self, mhost, db, usr, pwd):
        self._db = psy.connect(host=mhost, database=db, user=usr,  password=pwd)
def manipular(self, sql):
	try:
        	cur=self._db.cursor()
		cur.execute(sql)
		cur.close()
		self._db.commit()
	except:
		return False
	return True