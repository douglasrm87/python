import tkinter as tk
class Grid( tk.Frame ):
    def __init__(self):
    # Inicializando o frame
        tk.Frame.__init__(self)
        self.master.title("Grid")
        self.master.geometry( "400x400" )
        # Criando os labels e adicionando​
        # com o método grid()​
        for linha in range(3):
            for coluna in range(3):
                tk.Label(self.master, text=str(linha)+','+str(coluna)).grid(row=linha,column=coluna)
g = Grid()
g.mainloop()