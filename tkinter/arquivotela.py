import tkinter as tk
from tkinter.filedialog import askopenfilename

class Application( tk.Frame ):
	def __init__(self):
		self.abrirTela()
	def abrirTela(self,):
		tk.Frame.__init__(self, border=3,relief=tk.GROOVE)
		self.master.geometry( "400x400" )
		self.msg = tk.Label(self.master, text="Busque o arquivo")
		self.msg["font"] = ("Calibri", "9", "italic")
		self.buscar = tk.Button(self.master)
		self.buscar["text"] = "Buscar"
		self.buscar["font"] = ("Calibri", "9")
		self.buscar["width"] = 10
		self.buscar["command"] = self.mudarTexto
		self.buscar.pack()
		self.msg2 = tk.Label(self.master, text="")
		self.msg2["font"] = ("Calibri", "9", "italic")
		self.msg2.pack()
		self.sair = tk.Button(self.master,text="Sair",bg="red",fg="white",command=self.master.quit)
		self.sair.pack()
	def mudarTexto(self):
		if self.msg["text"] == "Busque o arquivo":
			#Teria que abrir a pasta do windows aqui
			filename = askopenfilename() # Isto te permite selecionar um arquivo
			print("Nome do Arquivo escolhido: ",filename) # printa o arquivo selecionado
			self.msg2["text"] = "NOME DO ARQUIVO AQUI: " + filename

obj = Application()
obj.mainloop()