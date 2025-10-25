# Usando SQLite3, que já vem instalado com o Python
import sqlite3
import os

# Criar o diretório para o banco de dados se não existir
os.makedirs('data', exist_ok=True)

# Conectar ao banco SQLite (será criado se não existir)
con = sqlite3.connect('data/banco_cidades.db')
cur = con.cursor()
           
# Apagar tabela se existir e criar nova
cur.execute('DROP TABLE IF EXISTS cidade')
sql = '''CREATE TABLE cidade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    uf TEXT
)'''
cur.execute(sql)

# Inserir dados
cidades = [
    ('Sao Paulo', 'SP'),
    ('Curitiba', 'PR'),
    ('Florianopolis', 'SC')
]
cur.executemany('INSERT INTO cidade (nome, uf) VALUES (?, ?)', cidades)
con.commit()

# Consultar dados
cur.execute('SELECT * FROM cidade')
vetor = cur.fetchall()
print ("Conteudo do vetor:",vetor)
print ("Tamanho do vetor:",len(vetor))
print ("Conteudo do vetor [0]:",vetor[0])
print ("Conteudo do vetor [1]:",vetor[1])
print ("Conteudo do vetor [1][2]. Estado:",vetor[1][2])
for rec in vetor:
    print (rec)
con.close()