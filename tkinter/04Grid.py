import tkinter as tk
class Grid( tk.Frame ):
    def __init__(self):
        # Inicializando o frame ​
        tk.Frame.__init__(self)
        self.master.title("Grid")
        self.master.geometry( "400x400" )
        tk.Label(self.master, text="Nome").grid(row=0)
        tk.Label(self.master, text="Sobrenome").grid(row=1)
        entrada1 = tk.Entry(self.master)
        entrada2 = tk.Entry(self.master)
        entrada1.grid(row=0, column=1)
        entrada2.grid(row=1, column=1)
        button = tk.Button(self.master,text="Sair",bg="red",fg="white",command=self.master.quit)
        button.grid(row=4, column=1)
g = Grid()
g.mainloop()