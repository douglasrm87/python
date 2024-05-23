import tkinter as tk
from tkinter.filedialog import askopenfilename
class ArquivoTkinter01 (tk.Frame):
    #Construtor da Sub Classe
    def __init__  (self):
        #Construtor da Super Classe. Primeiro a ser executado.
        tk.Frame.__init__(self)
        print ("ola")
        self.desenharTela ()

    def desenharTela (self):
        self.master.geometry ("600x620")
        self.msg = tk.Label (self.master,text="Treinando uso de arquivos em Python.")
        self.msg.pack()

        self.botaoBuscar = tk.Button (self.master)
        self.botaoBuscar ["text"] = "Clique Buscar"
        self.botaoBuscar ["font"] = ("Calibri", "9")
        self.botaoBuscar ["width"] = 30
        self.botaoBuscar ["command"] = self.buscarArquivo
        self.botaoBuscar.pack()

        self.msg2 = tk.Label (self.master,text="Resultado após clicar:")
        self.msg2 ["font"]= ("Calibri", "15")
        self.msg2.pack()

        self.botaoSair = tk.Button (self.master,text="Sair",bg="red",fg="white",width=20,command=self.quit)
        self.botaoSair.pack()

    def buscarArquivo (self):
        print ("ola, sou o Buscar Arquivo.")
        nomeArquivo = askopenfilename()
        print("Arquivo Selecionado:",nomeArquivo)
        self.msg2 ["text"] = "Aberto:"+nomeArquivo
obj = ArquivoTkinter01()
obj.mainloop()