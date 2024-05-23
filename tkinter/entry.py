import tkinter as tk
class Cadastro (tk.Frame):
	ent01 = tk.Entry ()
	ent02 = tk.Entry ()
	def __init__(self):
		self.desenharTela()
	def desenharTela(self):
		tk.Frame.__init__(self)
		self.master.title("Cadastrar Perguntas")
		self.master.geometry("1000x600")
		lb1 = tk.Label(self.master, text="Nova Pergunta", font="Arial 12")
		lb2 = tk.Label(self.master, text="Resposta Pergunta", font="Arial 12")
		lb1.grid(row=0, column=0)
		lb2.grid(row=1, column=0)
		self.ent01 = tk.Entry (self.master,width=100)
		self.ent01.grid (row = 0 , column = 1, padx = 10, pady=15, ipady = 10)
		self.ent02 = tk.Entry (self.master,width=100) 
		self.ent02.grid (row = 1 , column = 1, padx = 10, pady=15, ipady = 10)
		self.botao1 = tk.Button (self.master,text="Gravar",command=self.persistirArquivo)
		self.botao1.grid (row = 4 , column = 0)
		self.botao2 = tk.Button (self.master,text="Sair",command=self.quit)
		self.botao2.grid (row = 4 , column = 1)
	def persistirArquivo(self):
		print ("Gravando dados em arquivo")
		print ("Pergunta:",self.ent01.get())
		print ("Resposta",self.ent02.get())
obj = Cadastro()
obj.mainloop()
