import tkinter as tk

#https://docs.python.org/3/library/tkinter.html
class MeuProgramaTK(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.criarBotao()

    def criarBotao(self):
        self.botaoOlaMundo = tk.Button(self)
        self.botaoOlaMundo["text"] = "Clique aqui! - Alo Mundo"
        self.botaoOlaMundo["command"] = self.aloMundo
        self.botaoOlaMundo.pack(side="top")

        self.botaoSair = tk.Button(self, text="Sair", fg="red",command=self.master.destroy)
        self.botaoSair.pack(side="bottom")

    def aloMundo(self):
        print("Ola meu primeiro programa em TKinter.")

root = tk.Tk()
app = MeuProgramaTK(master=root)
app.mainloop()
