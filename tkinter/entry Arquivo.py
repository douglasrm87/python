import tkinter as tk
class Cadastro (tk.Frame):
    ent01 = tk.Entry ()
    ent02 = tk.Entry ()
    def __init__(self):
        self.desenharTela()
    def desenharTela(self):
        tk.Frame.__init__(self)
        self.master.title("Cadastrar Perguntas")
        self.master.geometry("1300x600")
        lb1 = tk.Label(self.master, text="Nova Pergunta", font="Arial 12")
        lb2 = tk.Label(self.master, text="Resposta Pergunta", font="Arial 12")
        lb1.grid(row=0, column=0)
        lb2.grid(row=1, column=0)
        self.ent01 = tk.Entry (self.master,width=100,font = ('Courier',11, 'bold'))
        self.ent01.grid (row = 0 , column = 2, padx = 10, pady=15, ipady = 10)
        self.ent02 = tk.Entry (self.master,width=100,font = ('Courier',11, 'bold'))
        self.ent02.grid (row = 1 , column = 2, padx = 10, pady=15, ipady = 10)
        botao1 = tk.Button (self.master,text="Gravar",command=self.persistirArquivo )
        botao1.grid (row = 4 , column = 0)
        botao2 = tk.Button (self.master,text="Sair",command=self.quit)
        botao2.grid (row = 4 , column = 1)
    def persistirArquivo(self):
        print ("Gravando arquivo")
        print ("Pergunta 01: " , self.ent01.get())
        pergunta ="Pergunta;" +  self.ent01.get() + "\n"
        resposta = "Resposta;" + self.ent02.get() + "\n"
        arquivo = open("./cadastro.txt", "w" , encoding="utf8")
        arquivo.writelines(pergunta)
        arquivo.writelines(resposta)
obj = Cadastro()
obj.mainloop()