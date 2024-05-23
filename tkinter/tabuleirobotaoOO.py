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
        for i in range(3):
            tk.Button(self.master,  text=str(i+1),border=1,relief=tk.RAISED,padx=20,pady=20,command=self.processarBotao
            ).grid(column=0, row=i,ipadx=formato,ipady=formato)
            for j in range(3):
                tk.Button(self.master, text=str(j+1), 
                border=1,relief=tk.RAISED,padx=20,pady=20,command=self.processarBotao).grid(column=j, row=i,ipadx=formato,ipady=formato)
    def processarBotao(self):
        self.Button.text.set ("ola")
        messagebox.showinfo("Message","Hey There! I hope you are doing well.")

g = Grid()
g.mainloop()

