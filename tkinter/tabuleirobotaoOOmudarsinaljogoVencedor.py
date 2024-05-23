from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

class Grid( tk.Frame ):
    ultimaJogada = 0
    teclaVet = None
    def __init__(self):
        self.desenharTela()
    def desenharTela(self,):
        tk.Frame.__init__(self, border=3,relief=tk.GROOVE)
        self.master.title("Grid")
        self.master.geometry( "680x720" )
        formato = 70
        self.teclaVet = [
            tk.Button(self.master, text=str(1),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[0])),
            tk.Button(self.master, text=str(2),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[1])),
            tk.Button(self.master, text=str(3),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[2])),
            tk.Button(self.master, text=str(4),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[3])),
            tk.Button(self.master, text=str(5),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[4])),
            tk.Button(self.master, text=str(6),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[5])),
            tk.Button(self.master, text=str(7),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[6])),
            tk.Button(self.master, text=str(8),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[7])),
            tk.Button(self.master, text=str(9),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.teclaVet[8]))]
        indice = 0
        myFont = font.Font(size=20, weight='bold')
        for i in range(3):
            for j in range(3):
                self.teclaVet[indice]['font'] = myFont
                self.teclaVet[indice].grid(row=i,column=j, ipadx=formato,ipady=formato)
                indice = indice + 1
    def processarBotao(self,btnCli):
        myFont = font.Font(size=20, weight='bold')
        texto = btnCli['text']
        print(texto)
        if (self.ultimaJogada == 0):
            btnCli.configure (text="0", bg='#0052cc', fg='#ffffff' )
            self.ultimaJogada = 1
        else:
            btnCli.configure (text="X", bg='#222222', fg='#ffffff' )
            self.ultimaJogada = 0
        btnCli['font'] = myFont
        btnCli["state"] = "disabled"
        self.validarVencedorLinhas()

    def validarVencedorLinhas(self,):
        print ("Validando campeão")
        if (self.teclaVet[0]['text'] == self.teclaVet[1]['text'] and self.teclaVet[0]['text'] == self.teclaVet[2]['text']):
            if (self.teclaVet[0]['text'] == "0"):
                messagebox.showinfo("Vencedor","Jogador BOLA ganhou")
            else:
                messagebox.showinfo("Vencedor","Jogador XIS ganhou")
        
g = Grid()
g.mainloop()
 

