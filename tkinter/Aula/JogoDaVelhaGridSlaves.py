from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

class JogoDaVelhaGridSlaves(tk.Frame):
    ultimaJogada = 0
    def __init__(self):
        self.formato = 65
        self.desenhar_tela()

    def processar_botao(self, x, y):
        self.btnCli = self.master.grid_slaves(x, y)[0]
        texto = self.btnCli['text']
        myFont = font.Font(size=15, weight='bold')

        if (self.ultimaJogada == 0):
            self.btnCli.configure (text="O", bg='#0052cc', fg='#ffffff' )
            self.ultimaJogada = 1
        else:
            self.btnCli.configure (text="X", bg='#222222', fg='#ffffff' )
            self.ultimaJogada = 0
        self.btnCli['font'] = myFont
        self.btnCli["state"] = "disable"
        self.modelosVencedores(0)
        self.modelosVencedores(1)
        self.modelosVencedoresDiagonalPrincipal()
        self.modelosVencedoresDiagonalSecundaria()
         

    def apresentarMensagem (self,ganhador):
        if ((ganhador == "O")):
            messagebox.showinfo("Vencedor","Jogador BOLA ganhou")
        else:
            messagebox.showinfo("Vencedor","Jogador XIS ganhou")
    
    def modelosVencedores(self,tpVencedor):
        linha = 0
        for x in range (3):
            linha = ["*","@","#"]
            for y in range (3):
                if (tpVencedor == 0):
                    #linhas
                    self.btnCli = self.master.grid_slaves(x, y)[0]
                else:
                    #colunas
                    self.btnCli = self.master.grid_slaves(y, x)[0]
                texto = self.btnCli['text']
                linha [y] = texto
                #print ("linha [y]: " +linha [y] )
                if (linha[0] == linha[1] and linha[0] == linha[2]):
                    #print ("ganhador: " + linha[0] )
                    self.apresentarMensagem (linha[0])

    def modelosVencedoresDiagonalPrincipal(self):
        linha = ["*","@","#"]
        for x in range (3):
            for y in range (3):
                if (x == y):
                    self.btnCli = self.master.grid_slaves(x, y)[0]
                    texto = self.btnCli['text']
                    linha [x] = texto
                    print ("linha [x]: " +linha [x] )
                    print (" [x]: " , x )
                if (linha[0] == linha[1] and linha[0] == linha[2]):
                    print ("ganhador: " + linha[0] )
                    self.apresentarMensagem (linha[0])                     
    
    def modelosVencedoresDiagonalSecundaria(self):
        linha = ["*","@","#"]
        self.btnCli = self.master.grid_slaves(0, 2)[0]
        texto = self.btnCli['text']
        linha [0] = texto
        
        self.btnCli = self.master.grid_slaves(1, 1)[0]
        texto = self.btnCli['text']
        linha [1] = texto
        
        self.btnCli = self.master.grid_slaves(2, 0)[0]
        texto = self.btnCli['text']
        linha [2] = texto
        if (linha[0] == linha[1] and linha[0] == linha[2]):
            print ("ganhador: " + linha[0] )
            self.apresentarMensagem (linha[0]) 

    def desenhar_tela(self):
        tk.Frame.__init__(self, relief=tk.GROOVE)
        self.winfo_toplevel().title("Elden Ring 2: A Vingança")
        self.master.geometry("580x620")
        indice = 0
        for x in range(3):
            for y in range(3):
                tk.Button(
                    self.master,
                    text=str(indice),
                    border=1,
                    relief=tk.GROOVE,
                    padx=20,
                    pady=20,
                    command=lambda row=x, column=y: self.processar_botao(row, column)
                ).grid(
                    row=x,
                    column=y,

                    ipadx=self.formato,
                    ipady=self.formato
                )
                indice = indice + 1
main = JogoDaVelhaGridSlaves()
main.mainloop()
