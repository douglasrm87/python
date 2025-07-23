#python -m pip install PySimpleGUI
import tkinter as tk
def exit_button(master):
    master.geometry( "400x400" )
    button = tk.Button(master,text="Sair",bg="red",fg="white",command=master.quit)
    button.pack()
root = tk.Tk()
root.title("Usando tkinter")
exit_button(root)
root.mainloop()

