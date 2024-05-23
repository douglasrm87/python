import tkinter as tk
from tkinter import messagebox

class Grid( tk.Frame ):

    def __init__(self):
        self.desenharTela()
    def desenharTela(self,):
        tk.Frame.__init__(self, border=3,relief=tk.GROOVE)
        self.master.title("Grid")
        self.master.geometry( "600x620" )
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
        for i in range(3):
            for j in range(3):
                self.teclaVet[indice].grid(row=i,column=j, ipadx=formato,ipady=formato)
                indice = indice + 1
            
    def processarBotao(self,btnCli):
        texto = btnCli['text']
        btnCli.configure (text="ola")
        print(texto)
        #messagebox.showinfo("Message","Hey There! I hope you are doing well.")

g = Grid()
g.mainloop()

'''
        self.tecla7 = tk.Button(self.master,  text=str(7),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.tecla7))
        self.tecla7.grid(row=2,column=0,ipadx=formato,ipady=formato)

        self.tecla8 = tk.Button(self.master,  text=str(8),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.tecla8))
        self.tecla8.grid(row=2,column=1,ipadx=formato,ipady=formato)

        self.tecla9 = tk.Button(self.master,  text=str(9),border=1,relief=tk.RAISED,padx=20,pady=20,command=lambda:self.processarBotao (self.tecla9))
        self.tecla9.grid(row=2,column=2,ipadx=formato,ipady=formato)

'''

