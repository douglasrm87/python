import tkinter as tk
def processarBotao(event):
    w = event.widget                      # here we recover your Button object
    print (w._name)
    

root = tk.Tk()
main_frame = tk.Frame(root, border=3, relief=tk.GROOVE)
main_frame.grid()
root.geometry("600x620")
formato = 70
numLabel = 1
for i in range(3):
    tabBotao = tk.Button(main_frame, text=str(numLabel), border=1,
            relief=tk.RAISED,padx=20,pady=20)
    tabBotao.grid(column=0, row=i,ipadx=formato,ipady=formato)
    tabBotao.bind ('<Button-1>', processarBotao)
    for j in range(3):
        tabBotao = tk.Button(main_frame, 
        text=str(numLabel), 
        border=1,relief=tk.RAISED,padx=20,pady=20)
        tabBotao.grid(column=j, row=i,ipadx=formato,ipady=formato)
        tabBotao.bind ('<Button-1>', processarBotao)
        numLabel = numLabel + 1
root.mainloop()