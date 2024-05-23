import tkinter as tk
import psycopg2 as psy      
class Seguro ():
	ent01 = tk.Entry()
	ent02 = tk.Entry()
	ent03 = tk.Entry()
	ent04 = tk.Entry()
	cursor = psy.extensions.cursor
	conexao = psy.extensions.connection
	def __init__(self):
		print ("ola")
		self.criarTabela()
		self.desenharTela("Cadastrar Seguro")

	def desenharTela(self,titulo):
		print ("Desenhando a tela.")
		abrirTela = tk.Tk()
		abrirTela.title (titulo)
		abrirTela.geometry ("1000x600")
		lb1 = tk.Label(abrirTela, text="Placa", font="Arial 12")
		lb2 = tk.Label(abrirTela, text="Modelo", font="Arial 12")
		lb3 = tk.Label(abrirTela, text="Ano", font="Arial 12")
		lb4 = tk.Label(abrirTela, text="Valor", font="Arial 12")
		lb1.grid(row=0, column=0)
		lb2.grid(row=1, column=0)
		lb3.grid(row=2, column=0)
		lb4.grid(row=3, column=0)
		self.ent01 = tk.Entry(abrirTela, width=50)
		self.ent01.grid(row=0, column=1, padx=10, pady=15, ipady=10)
		self.ent02 = tk.Entry(abrirTela, width=50)
		self.ent02.grid(row=1, column=1, padx=10, pady=15, ipady=10)
		self.ent03 = tk.Entry(abrirTela, width=50)
		self.ent03.grid(row=2, column=1, padx=10, pady=15, ipady=10)
		self.ent04 = tk.Entry(abrirTela, width=50)
		self.ent04.grid(row=3, column=1, padx=10, pady=15, ipady=10)
		botao1 = tk.Button(abrirTela, text="Sair", command=quit)
		botao1.grid(row=4, column=0)
		if (titulo == "Cadastrar Seguro"):
			botao2 = tk.Button(abrirTela, text="Gravar Dados",command=self.persistirBanco)
			botao2.grid(row=4, column=1)
			botao3 = tk.Button(abrirTela, text="Consultar Seguro",command=self.consultar)
			botao3.grid(row=5, column=0)
		if (titulo == "Pesquisar Seguro"):
			botao6 = tk.Button(abrirTela, text="Consultar Placa",command=self.selecionarRegistro)
			botao6.grid(row=6, column=1)
		abrirTela.mainloop()

	def persistirBanco (self):
		print ("ola")
		placa = self.ent01.get()        
		modelo = self.ent02.get()        
		ano = self.ent03.get()        
		valor = self.ent04.get()        
		inserir = "insert into seguro (placa , modelo , ano , valor) values (%s,%s,%s,%s)"
		self.cursor.execute(inserir, (placa , modelo , ano , valor))
		self.conexao.commit()  

	def consultar (self):
		self.desenharTela("Pesquisar Seguro")
		print ("ola")
		self.selecionarRegistro()

	def selecionarRegistro (self):
		print ("ola")
		self.conectarBanco()
		pl = self.ent01.get()
		selecionar = "select placa , modelo , ano , valor from seguro where placa = '" + pl + "'"
		self.cursor.execute(selecionar)
		registros = self.cursor.fetchall()
		for reg in registros:
			self.ent02.insert (0,reg[1])
			self.ent03.insert (0,reg[2])            
			self.ent04.insert (0,reg[3])

	def conectarBanco (self):
		self.conexao = psy.connect(host='127.0.0.1', database='postgres', user='postgres', password='12345')
		self.cursor=self.conexao.cursor()        

	def criarTabela(self):
		self.conectarBanco()
		try:        
			criarTabela = 'create table seguro (id serial primary key , placa varchar (10) , modelo varchar (10), ano int , valor float )'
			self.cursor.execute (criarTabela)
		except Exception as e:
			print (str(e))        



obj = Seguro()
