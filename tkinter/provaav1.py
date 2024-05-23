import tkinter as tk
from tkinter import END, messagebox

class Cadastro (tk.Frame):
    ent01 = tk.Entry ()
    ent02 = tk.Entry ()
    ent03 = tk.Entry ()
    ent04 = tk.Entry ()
    # implementar o construtor. Primeiro método executadona classe
    def __init__(self):
        self.desenharTela()
    def desenharTela(self):
        tk.Frame.__init__(self)
        self.master.title("SEGUROS")
        self.master.geometry("600x350")
        lb1 = tk.Label(self.master, text="PLACA (XXX-XXXX)", font="Arial 12")
        lb2 = tk.Label(self.master, text="MODELO / ANO", font="Arial 12")
        lb3 = tk.Label(self.master, text="IDADE", font="Arial 12")
        lb4 = tk.Label(self.master, text="VALOR BASE", font="Arial 12")
        lb1.grid(row=0, column=0)
        lb2.grid(row=1, column=0)
        lb3.grid(row=2, column=0)
        lb4.grid(row=3, column=0)
        self.ent01 = tk.Entry (self.master,width=40,font = ('Courier',11, 'bold'))
        self.ent01.grid (row = 0 , column = 1, padx = 10, pady=15, ipady = 10)

        self.ent02 = tk.Entry (self.master,width=40,font = ('Courier',11, 'bold'))
        self.ent02.grid (row = 1 , column = 1, padx = 10, pady=15, ipady = 10)

        self.ent03 = tk.Entry (self.master,width=40,font = ('Courier',11, 'bold'))
        self.ent03.grid (row = 2 , column = 1, padx = 10, pady=15, ipady = 10)

        self.ent04 = tk.Entry (self.master,width=40,font = ('Courier',11, 'bold'))
        self.ent04.grid (row = 3 , column = 1, padx = 10, pady=15, ipady = 10)

        botao1 = tk.Button (self.master,text="Gravar",command=self.persistirArquivo )
        botao1.grid (row = 4 , column = 0)
        botao2 = tk.Button (self.master,text="Ler Placas",command=self.LerPlacas )
        botao2.grid (row = 4 , column = 1)
        botao2 = tk.Button (self.master,text="Sair",command=self.quit)
        botao2.grid (row = 4 , column = 2)

    ## LEIO AS PLACAS
    def LerPlacas(self):
        arquivox = open("./dados.txt", "r" , encoding="utf8")
        conteudoAtual = arquivox.readlines()
        arquivox.close
        self.ent01.delete(0,END)
        for n in conteudoAtual:
            veiculo = n.split("|")
            conteudoAtual = str(conteudoAtual)
            #messagebox.showinfo("DADOS",conteudoAtual)
            #veiculo = conteudoAtual.split("|") # separa os valores
            self.ent01.insert(0,veiculo[0])
            self.ent02.insert(0,veiculo[1])
            self.ent03.insert(0,veiculo[2])
            self.ent04.insert(0,veiculo[3])

    ## GRAVOS OS DADOS
    def persistirArquivo(self):
        arquivox = open("./dados.txt", "a+" , encoding="utf8")
        conteudoAtual = arquivox.readlines()
        arquivox.close

        print ("Gravando arquivo")
        print ("Veiculo: " , self.ent01.get())

        seguro= self.ent01.get() + "|" + self.ent02.get()+ "|" + self.ent03.get()+ "|" + self.ent04.get() + "\n"
        conteudoAtual.append(seguro)
        arquivo = open("./dados.txt", "w" , encoding="utf8")
        arquivo.writelines(conteudoAtual)
        arquivo.close
        messagebox.showinfo("SEGURO","Dados salvos com sucesso !")
        self.ent01.delete(0,END)
        self.ent02.delete(0,END)
        self.ent03.delete(0,END)
        self.ent04.delete(0,END)

obj = Cadastro()
obj.mainloop()