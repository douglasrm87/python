import tkinter as tk
import psycopg2 as psy

class Cadastro (tk.Frame):
    ent01 = tk.Entry()
    ent02 = tk.Entry()
    cursor = psy.extensions.cursor
    conexao = psy.extensions.connection
    # implementar o construtor. Primeiro método executadona classe
    def __init__(self):
        self.desenharTela()
        self.criarTabela()
    def desenharTela(self):
        tk.Frame.__init__(self)
        self.master.title("Cadastrar Perguntas")
        self.master.geometry("1000x600")
        lb1 = tk.Label(self.master, text="Cidade", font="Arial 12")
        lb2 = tk.Label(self.master, text="Estado", font="Arial 12")
        lb1.grid(row=0, column=0)
        lb2.grid(row=1, column=0)
        self.ent01 = tk.Entry(self.master, width=100)
        self.ent01.grid(row=0, column=1, padx=10, pady=15, ipady=10)
        self.ent02 = tk.Entry(self.master, width=100)
        self.ent02.grid(row=1, column=1, padx=10, pady=15, ipady=10)
        #executa somente uma vez
        botao1 = tk.Button(self.master, text="Gravar Arquivo",command=self.persistirArquivo())
        botao1.grid(row=4, column=0)
        botao2 = tk.Button(self.master, text="Sair", command=self.quit)
        botao2.grid(row=4, column=1)
        botao3 = tk.Button(self.master, text="Gravar Banco",command=self.persistirBanco)
        botao3.grid(row=5, column=0)
        botao4 = tk.Button(self.master, text="Ler Banco",command=self.selecionarRegistro)
        botao4.grid(row=5, column=1)
    def persistirArquivo(self):
        print("Gravando arquivo")
    def persistirBanco(self):
        self.conectarBanco()
        print("Gravando Banco")
        self.inserirRegistro(self.ent01.get(), self.ent02.get())
    def selecionarRegistro(self):
        self.conectarBanco()
        selecionar = "select * from minha_cidade"
        self.cursor.execute(selecionar)
        registros = self.cursor.fetchall()
        for reg in registros:
            print("Registro lido:", reg)
    def inserirRegistro(self, nome_cidade, estado):
        print("nome_cidade: " + nome_cidade)
        # usando parâmetros
        inserir = "insert into minha_cidade (nome_cidade,estado) values (%s,%s)"
        # Executar a query DML
        self.cursor.execute(inserir, (nome_cidade, estado))

    def conectarBanco(self):
        # Conectar ao banco de dados.
        self.conexao = psy.connect(host='127.0.0.1', database='postgres', user='postgres', password='12345')
        self.cursor=self.conexao.cursor() 

    def criarTabela(self):
        self.conectarBanco()
        try:
            # Executando um comando DDL - Data Definiton Language
            criarTabela = 'create table minha_cidade (id serial primary key , nome_cidade varchar (100) , estado varchar (2) )'
            # Executar a query DML
            self.cursor.execute (criarTabela)
            # Efetivar a criação. sem esta linha a Tabela não será Serializada no disco.
            self.conexao.commit()
        except Exception as e:
            print ("Tabela já criada.")
            self.conexao.rollback()
obj = Cadastro()
obj.mainloop()