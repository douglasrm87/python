import tkinter as tk 
      
root = tk.Tk()
root.title("Usando tkinter")
root.geometry( "400x400" )
button = tk.Button(root,text="Sair",bg="green",fg="white",command=root.quit)
button.pack()
root.mainloop()

