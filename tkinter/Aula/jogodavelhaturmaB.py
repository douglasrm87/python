import tkinter as tk
def processarBotao():
    print ("Fui Clicado")
root = tk.Tk()
formato = 70
main_frame = tk.Frame (root,border=3,relief=tk.GROOVE)
main_frame.grid()
root.geometry("600x620")
for i in range (3):
    for j in range (3):
        tk.Button (main_frame
                ,text="A"
                ,border=1
                ,relief=tk.GROOVE
                ,padx=20
                ,pady=20
                ,command=processarBotao).grid (column=j
                                               ,row=i
                                               ,ipadx=formato
                                               ,ipady=formato)
 
root.mainloop()