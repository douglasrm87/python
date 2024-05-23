from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

class JogoVelhaOO (tk.Frame):
    ultimaJogada = 0

    def __init__ (self):
        self.formato = 70
        self.desenharTela()

    def desenharTelaOtimizado(self):
        tk.Frame.__init__(self, relief=tk.GROOVE)
        self.winfo_toplevel().title("Elden Ring 2: A Vingança")
        self.master.geometry("600x620")

        for x in range(3):
            for y in range(3):
                tk.Button(
                    self.master,
                    text=str(x + 1),
                    border=1,
                    relief=tk.GROOVE,
                    padx=20,
                    pady=20,
                    command=lambda row=x, column=y: self.processarBotaoOtimizado(row, column)
                ).grid(
                    row=x,
                    column=y,

                    ipadx=self.formato,
                    ipady=self.formato
                )

    def desenharTela (self):
        tk.Frame.__init__ (self,border=3,relief=tk.GROOVE)
        self.master.title ("Jogo da Velha OO")
        self.master.geometry("600x620")
        formato = 70
        # Criando 9 botões
        self.teclaVet = [
        tk.Button(self.master, text=str(1),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[0])),
        tk.Button(self.master, text=str(2),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[1])),
        tk.Button(self.master, text=str(3),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[2])),
        tk.Button(self.master, text=str(4),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[3])),
        tk.Button(self.master, text=str(5),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[4])),
        tk.Button(self.master, text=str(6),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[5])),
        tk.Button(self.master, text=str(7),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[6])),
        tk.Button(self.master, text=str(8),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[7])),
        tk.Button(self.master, text=str(9),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[8]))
        ]
        indice = 0
        # Quantas vezes processa o looping? 9 vezes.
        for i in range (3):
            for j in range (3):
                self.teclaVet[indice].grid(row=i,column=j, ipadx=formato,ipady=formato)
                indice = indice + 1
    def processarBotaoOtimizado(self, x, y):
        myFont = font.Font(size=15, weight='bold')
  
        btnCli = self.master.grid_slaves(x, y)[0]
    
        texto = btnCli['text']
        print(texto)
        if (self.ultimaJogada == 0):
            btnCli.configure (text="0", bg='#0052cc', fg='#ffffff' )
            self.ultimaJogada = 1
        else:
            btnCli.configure (text="X", bg='#222222', fg='#ffffff' )
            self.ultimaJogada = 0
        btnCli['font'] = myFont
        btnCli["state"] = "disable"
        self.modelosVencedoresLinha()
        self.modelosVencedoresColuna()

    
        #btn.configure(text="ola")

    def processarBotao(self,btnCli):
        myFont = font.Font(size=15, weight='bold')
        texto = btnCli['text']
        print(texto)
        if (self.ultimaJogada == 0):
            btnCli.configure (text="O", bg='#0052cc', fg='#ffffff' )
            self.ultimaJogada = 1
        else:
            btnCli.configure (text="X", bg='#222222', fg='#ffffff' )
            self.ultimaJogada = 0
        btnCli['font'] = myFont
        btnCli["state"] = "disable"
        self.modelosVencedoresLinha()
        self.modelosVencedoresColuna()

    def apresentarMensagem (self,ganhador):
        if ((ganhador == "O")):
            messagebox.showinfo("Vencedor","Jogador BOLA ganhou")
        else:
            messagebox.showinfo("Vencedor","Jogador XIS ganhou")

    def modelosVencedoresLinha(self):
        linha = 0
        for i in range (3):
            if (self.teclaVet[linha]['text'] == self.teclaVet[linha+1]['text'] and 
                self.teclaVet[linha]['text'] == self.teclaVet[linha+2]['text']):
                print ("ganhador:" , self.teclaVet[linha]['text'])
                self.apresentarMensagem(self.teclaVet[linha]['text'])
            linha = linha + 3
    def modelosVencedoresColuna(self):
        linha = 0
        for i in range (3):
            if (self.teclaVet[linha]['text'] == self.teclaVet[linha+3]['text'] and 
                self.teclaVet[linha]['text'] == self.teclaVet[linha+6]['text']):
                self.apresentarMensagem(self.teclaVet[linha]['text'])
            linha = linha + 1

    def validarVencedorLinhasSolucaoRuim(self):
        print ("Validando campeão. ")
        # Se o conteúdo da coluna 0 igual a da coluna 1 E
        # Se o conteúdo da coluna 0 igual a da coluna 2. Fechou a linha 0. 
        if ((self.teclaVet[0]['text'] == self.teclaVet[1]['text'] and 
            self.teclaVet[0]['text'] == self.teclaVet[2]['text'])
            or
            (self.teclaVet[3]['text'] == self.teclaVet[4]['text'] and 
            self.teclaVet[3]['text'] == self.teclaVet[5]['text'])
            or
            (self.teclaVet[6]['text'] == self.teclaVet[7]['text'] and 
            self.teclaVet[6]['text'] == self.teclaVet[8]['text'])
            ):
            if ((self.teclaVet[0]['text'] == "0")or 
                (self.teclaVet[3]['text'] == "0")or 
                (self.teclaVet[6]['text'] == "0")):
                messagebox.showinfo("Vencedor","Jogador BOLA ganhou")
            else:
                messagebox.showinfo("Vencedor","Jogador XIS ganhou")
obj = JogoVelhaOO()
obj.mainloop()