import tkinter as tk
def processarBotao():
    print ("oi")

root = tk.Tk()
main_frame = tk.Frame(root, border=3, relief=tk.GROOVE)
main_frame.grid()
root.geometry("600x620")
formato = 70
for i in range(3):
    #Create Labels for numbering the rows:
    tk.Button(main_frame, 
            text=str(i+1), 
            border=1,
            relief=tk.RAISED,padx=20,pady=20,command=processarBotao
            ).grid(column=0, row=i,ipadx=formato,ipady=formato)
    for j in range(3):
        #Create Labels for numbering the rows:
        tk.Button(main_frame, 
        text=str(j+1), 
        border=1,relief=tk.RAISED,padx=20,pady=20,command=processarBotao).grid(column=j, row=i,ipadx=formato,ipady=formato)
root.mainloop()