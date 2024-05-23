import tkinter as tk 
import psycopg2 as psy
#pip install tkcalendar - rodei 2x
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import datetime


class Notas (tk.Frame):
    matricula = tk.Entry() 
    nomeAluno = tk.Entry()
    dataRegistro  = tk.Entry()
    dataSelecionada=tk.StringVar()
    notaAV1 = tk.Entry()
    notaAV2 = tk.Entry()
    FLAG_TABELAS = 0

    cursor = psy.extensions.cursor 
    conexao = psy.extensions.connection 
    #primeiro metodo a ser executado
    #Constrtutor
    def __init__(self): 
        if (self.FLAG_TABELAS == 0):
            self.criarTabela()
        self.desenharTela("Tela de Gestão de Notas")

    def desenharTela(self,titulo):
        tk.Frame.__init__(self) 
        print ("Desenhando a tela.") 
        self.master.title (titulo) 
        self.master.geometry ("1000x600") 
        self.desenharTelaBase(self.master)

        botao1 = tk.Button(self.master, text="Gravar", command=self.persistirBanco) 
        botao1.grid(row=6, column=0)
        botao2 = tk.Button(self.master, text="Listar", command=self.listarBanco) 
        botao2.grid(row=6, column=1)
        botao3 = tk.Button(self.master, text="Atualizar", command=self.atualizarBanco) 
        botao3.grid(row=6, column=2)
        botao4 = tk.Button(self.master, text="Sair", command=quit) 
        botao4.grid(row=8, column=0)

    def desenharTelaBase(self,ponteiroTela):

        lb1 = tk.Label(ponteiroTela, text="Matricula", font="Arial 12") 
        lb2 = tk.Label(ponteiroTela, text="Nome do Aluno", font="Arial 12") 
        lb3 = tk.Label(ponteiroTela, text="Data", font="Arial 12") 
        lb4 = tk.Label(ponteiroTela, text="Nota AV1", font="Arial 12") 
        lb5 = tk.Label(ponteiroTela, text="Nota AV2", font="Arial 12") 

        lb1.grid(row=0, column=0) 
        lb2.grid(row=1, column=0) 
        lb3.grid(row=2, column=0) 
        lb4.grid(row=3, column=0) 
        lb5.grid(row=4, column=0) 

        self.matricula = tk.Entry(ponteiroTela, width=50) 
        self.matricula.grid(row=0, column=1, padx=10, pady=15, ipady=10) 
        self.nomeAluno = tk.Entry(ponteiroTela, width=50) 
        self.nomeAluno.grid(row=1, column=1, padx=10, pady=15, ipady=10) 

        self.dataRegistro = DateEntry(ponteiroTela, width= 16, textvariable=self.dataSelecionada,background= "magenta3", foreground= "white",bd=2)
        self.dataRegistro.grid(row=2, column=1, padx=10, pady=15, ipady=10) 

        self.notaAV1 = tk.Entry(ponteiroTela, width=50) 
        self.notaAV1.grid(row=3, column=1, padx=10, pady=15, ipady=10) 
        self.notaAV2 = tk.Entry(ponteiroTela, width=50) 
        self.notaAV2.grid(row=4, column=1, padx=10, pady=15, ipady=10) 



    def persistirBanco(self):
        print ("Gravando dados")

        mat = ""
        nomeAluno = ""
        nota01 = 0.0
        nota02 = 0.0
        #vamos tratar os dados
        if (len(self.matricula.get()) > 0 and self.matricula.get().isdigit()):
            mat = int (self.matricula.get())
            if (mat < 0  or mat > 9999999999):
                messagebox.showinfo("Ops","Máricula inválida (entre 0 e 9999999999).")
                return
            else:
                print ("Matrocula:",mat)
        else:
            messagebox.showinfo("Ops","Digitar uma Máricula válida (entre 0 e 9999999999).")
            return

        if (len(self.nomeAluno.get()) > 0):
            nomeAluno = self.nomeAluno.get()
            print ("Nome:",nomeAluno)
        else:
            messagebox.showinfo("Ops","Digitar um Nome de Aluno.")
            return

        textoAV1 = "Digitar uma nota válida para AV1 (entre 0 e 10)."
        if (len (self.notaAV1.get()) > 0 and self.notaAV1.get().isdigit()):
            nota01 = float(self.notaAV1.get())
            if ( nota01 < 0.0  or nota01 > 10.0):
                messagebox.showinfo("Ops",textoAV1)
                return
            else:
                print ("AV1:",nota01)
        else:
            messagebox.showinfo("Ops",textoAV1)

        textoAV2 = "Digitar uma nota válida para AV2 (entre 0 e 10)."
        if (len (self.notaAV2.get()) > 0 and self.notaAV2.get().isdigit()):
            nota02 = float(self.notaAV2.get())
            if ( nota02 < 0.0  or nota02 > 10.0):
                messagebox.showinfo("Ops",textoAV2)
                return
            else:
                print ("AV2:",nota02)
        else:
            messagebox.showinfo("Ops",textoAV2)
        
        print ("Data escolhida: ",self.dataSelecionada.get())
        # usando parâmetros 
        inserir = "insert into gestao_nota (matricula,nome_aluno,data_registro,nota_av1,nota_av2) values (%s,%s,%s,%s,%s)" 
        # Executar a query DML - Evitar SQL Injection
        self.cursor.execute(inserir, (mat ,nomeAluno, self.dataSelecionada.get(),nota01,nota02)) 
        # self.cursor.execute(inserir, (2 ,"Douglas", "01/01/2022" , 2.0 , 2.0)) 
        self.conexao.commit() 
        messagebox.showinfo("Ação Gravação","Dados Gravados comk sucesso. " + str(datetime.datetime.now()))
         
    def conectarBanco (self): 
        self.conexao = psy.connect(host='127.0.0.1', database='postgres', user='postgres', password='12345') 
        self.cursor=self.conexao.cursor()
    def criarTabela(self): 
        self.conectarBanco() 
        try: 
            # criarTabela = 'drop table gestao_nota' 
            # self.cursor.execute (criarTabela) 
            # self.conexao.commit() 

            # Executando um comando DDL - Data Definiton Language 
            criarTabela = 'create table gestao_nota (matricula int primary key , nome_aluno varchar (30) , data_registro date , nota_av1 float, nota_av2 float )' 
            # Executar a query DML 
            self.cursor.execute (criarTabela) 
            # Efetivar a criação. sem esta linha a Tabela não será Serializada no disco. 
            self.conexao.commit() 
        except Exception as e: 
            print ("Atenção: ", e)
            self.conexao.rollback() 
    def listarBanco(self):
        print ("Listando dados")
        telaListar = tk.Tk()
        telaListar.title ("Tela de Apresentação dos dados") 
        self.desenharTelaListarAtualizar(telaListar)

        telaListar.mainloop()

    def atualizarBanco(self):
        print ("Atualizando dados")
        telaAtualizar = tk.Tk()
        telaAtualizar.title ("Tela de Atualização dos dados") 
        self.desenharTelaListarAtualizar(telaAtualizar)
        botaoAtualizar = tk.Button(telaAtualizar, text="Atualizar Notas", command=self.atualizarDados) 
        botaoAtualizar.grid(row=6, column=2)
        telaAtualizar.mainloop()

    def desenharTelaListarAtualizar(self,telaListar):
        telaListar.geometry ("1000x600") 
        self.desenharTelaBase(telaListar)
        botaoVoltar = tk.Button(telaListar, text="Voltar", command=telaListar.destroy) 
        botaoVoltar.grid(row=6, column=0)
        botaoPesquisa = tk.Button(telaListar, text="Pesquisar", command=self.consultarMatricula) 
        botaoPesquisa.grid(row=6, column=1)

    def consultarMatricula(self):
        self.nomeAluno.delete(0,tk.END)
        self.dataRegistro.delete(0,tk.END)
        self.notaAV1.delete(0,tk.END)
        self.notaAV2.delete(0,tk.END)

        selecionar = "select nome_aluno , data_registro , nota_av1 , nota_av2 from gestao_nota where matricula = %s" 
        self.cursor.execute(selecionar,(self.matricula.get())) 
        registro = self.cursor.fetchall() 
        if (registro):
            for reg in registro: 
                print("Registro lido:", reg) 
                self.nomeAluno.insert(0,reg[0])
                self.dataRegistro.insert(0, reg[1])
                self.notaAV1.insert(0, reg[2])
                self.notaAV2.insert(0,reg[3])
        else:
            messagebox.showinfo("Listar Dados","Matricula não localizada. " + str(datetime.datetime.now()))
 
    def atualizarDados(self):
        selecionar = "update gestao_nota set nota_av1 = %s , nota_av2 = %s where matricula = %s" 
        self.cursor.execute(selecionar,(self.notaAV1.get(),self.notaAV2.get(),self.matricula.get())) 
        self.conexao.commit() 
        messagebox.showinfo("Atualiza Notas","Notas atualizadas. " + str(datetime.datetime.now()))
        self.persistirArquivo(self.matricula.get()+","+self.nomeAluno.get()+","+self.notaAV1.get()+","+self.notaAV2.get())
    
    def persistirArquivo(self,log):
        print ("Dados LOG: " , log)
        arq = "./lognotas.txt"
        arquivo = open(arq, "r" , encoding="utf8")
        conteudoAtual = arquivo.readlines()
        arquivo.close()
        conteudoAtual.append(log + "\n")
        arquivo = open(arq, "w" , encoding="utf8")
        arquivo.writelines(conteudoAtual)
        arquivo.close()

#Primeira linha a ser executada
obj = Notas()
obj.mainloop()