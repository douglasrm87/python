import tkinter as tk 
import psycopg2 as psy       

class Notas ():
    ent01 = tk.Entry() 
    #primeiro metodo a ser executado
    #Constrtutor
    def __init__(self): 
        print ("ola") 
        self.desenharTela("Tele de Gestão de Notas")

    def desenharTela(self,titulo):
        print ("Desenhando a tela.") 
        abrirTela = tk.Tk() 
        abrirTela.title (titulo) 
        abrirTela.geometry ("1000x600") 
        lb1 = tk.Label(abrirTela, text="Matricula", font="Arial 12") 
        lb2 = tk.Label(abrirTela, text="Nome do Aluno", font="Arial 12") 
        lb3 = tk.Label(abrirTela, text="Data", font="Arial 12") 
        lb4 = tk.Label(abrirTela, text="Nota AV1", font="Arial 12") 
        lb5 = tk.Label(abrirTela, text="Nota AV2", font="Arial 12") 

        lb1.grid(row=0, column=0) 
        lb2.grid(row=1, column=0) 
        lb3.grid(row=2, column=0) 
        lb4.grid(row=3, column=0) 
        lb5.grid(row=4, column=0) 

        self.ent01 = tk.Entry(abrirTela, width=50) 
        self.ent01.grid(row=0, column=1, padx=10, pady=15, ipady=10) 
        self.ent02 = tk.Entry(abrirTela, width=50) 
        self.ent02.grid(row=1, column=1, padx=10, pady=15, ipady=10) 
        self.ent03 = tk.Entry(abrirTela, width=50) 
        self.ent03.grid(row=2, column=1, padx=10, pady=15, ipady=10) 
        self.ent04 = tk.Entry(abrirTela, width=50) 
        self.ent04.grid(row=3, column=1, padx=10, pady=15, ipady=10) 
        self.ent05 = tk.Entry(abrirTela, width=50) 
        self.ent05.grid(row=4, column=1, padx=10, pady=15, ipady=10) 

        botao1 = tk.Button(abrirTela, text="Gravar", command=self.persistirBanco) 
        botao1.grid(row=6, column=0)
        botao2 = tk.Button(abrirTela, text="Listar", command=self.listarBanco) 
        botao2.grid(row=6, column=1)
        botao3 = tk.Button(abrirTela, text="Atualizar", command=self.atualizarBanco) 
        botao3.grid(row=6, column=2)
        botao4 = tk.Button(abrirTela, text="Sair", command=quit) 
        botao4.grid(row=8, column=0)
        abrirTela.mainloop() 

    def persistirBanco(self):
        print ("Gravando dados")
    def listarBanco(self):
        print ("Listando dados")
    def atualizarBanco(self):
        print ("Atualizando dados")

#Primeira linha a ser executada
obj = Notas()