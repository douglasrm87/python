import hashlib
from tkinter import *
def senha ():
	global final
	root = Tk()
	root.geometry("800x200+10+10")
	modify = final.get()
	senha = hashlib.sha256(b"%s").hexdigest()
	print("Senha modificada!.")
	texto = Label(root, text="Senha no formato SHA-256:")
	texto.place(x=10,y=55)
	texto = Label(root, text=senha)
	texto.place(x=10, y=85)
root = Tk()
root.geometry("300x200+10+10")
texto = Label(root, text="Informe sua senha")
texto.place(x=50, y=55)
final = Entry(root,)
final.place(x=50, y=75)
botao = Button(root, text="Transformar" , bg="#EEEEEE", command=senha)
botao.place(x=50,y=95)
root.mainloop()
