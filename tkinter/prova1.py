import tkinter as tk
import psycopg2 as psy
class Cadastro ():
	ent01 = tk.Entry()
	ent02 = tk.Entry()
	ent03 = tk.Entry()
	ent04 = tk.Entry()        
	#<class 'psycopg2.extensions.cursor'>
	#<class 'psycopg2.extensions.connection'>
	cursor = psy.extensions.cursor
	conexao = psy.extensions.connection
	# implementar o construtor. Primeiro método executadona classe
	def __init__(self):
		self.desenharTela("Cadastrar Seguro")
		self.criarTabela()
	def desenharTela(self,titulo):
		abrirTela = tk.Tk()
		abrirTela.title(titulo)
		abrirTela.geometry("1000x600")
		lb1 = tk.Label(abrirTela, text="Placa", font="Arial 12")
		lb2 = tk.Label(abrirTela, text="Modelo", font="Arial 12")
		lb3 = tk.Label(abrirTela, text="Ano", font="Arial 12")
		lb4 = tk.Label(abrirTela, text="Valor", font="Arial 12")
		lb1.grid(row=0, column=0)
		lb2.grid(row=1, column=0)
		lb3.grid(row=2, column=0)
		lb4.grid(row=3, column=0)
		self.ent01 = tk.Entry(abrirTela, width=100)
		self.ent01.grid(row=0, column=1, padx=10, pady=15, ipady=10)
		self.ent02 = tk.Entry(abrirTela, width=100)
		self.ent02.grid(row=1, column=1, padx=10, pady=15, ipady=10)
		self.ent03 = tk.Entry(abrirTela, width=100)
		self.ent03.grid(row=2, column=1, padx=10, pady=15, ipady=10)
		self.ent04 = tk.Entry(abrirTela, width=100)
		self.ent04.grid(row=3, column=1, padx=10, pady=15, ipady=10)
		#executa somente uma vez
		botao1 = tk.Button(abrirTela, text="Gravar Arquivo",command=self.persistirArquivo())
		botao1.grid(row=4, column=0)
		botao2 = tk.Button(abrirTela, text="Sair", command=quit)
		botao2.grid(row=4, column=1)
		if (titulo == "Cadastrar Seguro"):
			botao3 = tk.Button(abrirTela, text="Gravar Banco",command=self.persistirBanco)
			botao3.grid(row=5, column=0)
			botao4 = tk.Button(abrirTela, text="Ler Banco",command=self.consultar)
			botao4.grid(row=5, column=1)
		if (titulo == "Pesquisar Seguro"):
			botao6 = tk.Button(abrirTela, text="Consultar Placa",command=self.selecionarRegistro)
			botao6.grid(row=6, column=1)
		abrirTela.mainloop()
	def persistirArquivo(self):
	 	print("Gravando arquivo")
	def persistirBanco(self):
		self.conectarBanco()
		print("Gravando Banco")
		self.inserirRegistro(self.ent01.get(), self.ent02.get(), self.ent03.get(), self.ent04.get())
	def consultar(self):
		self.desenharTela("Pesquisar Seguro")        
	def selecionarRegistro(self):
		self.conectarBanco()
		pl = self.ent01.get()
		print ("placa consultada:",str(pl))
		selecionar = "select placa , modelo , ano , valor from seguro where placa = '" + pl + "'"
		self.cursor.execute(selecionar)
		registros = self.cursor.fetchall()
		for reg in registros:
 	 	 	print("Registro lido:", reg)
 	 	 	self.ent02.insert(0,reg[1])
 	 	 	self.ent03.insert(0,reg[2])
 	 	 	self.ent04.insert(0,reg[3])                                             
	def inserirRegistro(self, placa , modelo , ano , valor):
  		print("placa:" + placa)
  		print("modelo:" + modelo)
  		print("ano:" + ano)
  		print("valor:" + valor)                              
	 	# usando parâmetros
 	 	inserir = "insert into seguro (placa , modelo , ano , valor) values (%s,%s,%s,%s)"
 	 	# Executar a query DML , (placa , modelo , ano , valor)
 	 	self.cursor.execute(inserir, (placa , modelo , ano , valor))
 	 	self.conexao.commit()  

	def conectarBanco(self):
 	 	# Conectar ao banco de dados.
		self.conexao = psy.connect(host='127.0.0.1', database='postgres', user='postgres', password='12345')
		self.cursor=self.conexao.cursor() 
	
	
	def criarTabela(self):
		self.conectarBanco()
		try:
			# Executando um comando DDL - Data Definiton Language
			criarTabela = 'create table seguro (id serial primary key , placa varchar (10) , modelo varchar (10), ano int , valor float )'
			# Executar a query DML
			self.cursor.execute (criarTabela)
			# Efetivar a criação. sem esta linha a Tabela não será Serializada no disco.
			self.conexao.commit()
		except Exception as e:
			print ("Tabela já criada.")
			self.conexao.rollback()

obj = Cadastro()

