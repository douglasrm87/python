import tkinter as tk
root = tk.Tk()
main_frame = tk.Frame(root, border=3, relief=tk.GROOVE)
main_frame.grid()
root.geometry("550x550")
formato = 70
for i in range(3):
    #Create Labels for numbering the rows:
    tk.Label(main_frame, 
            text=str(i+1), 
            border=1,
            relief=tk.GROOVE,
            padx=20,
            pady=20,
            ).grid(column=0, row=i,ipadx=formato,ipady=formato)

    for j in range(3):
        #Create Labels for numbering the rows:
        tk.Label(main_frame, 
        text=str(j+1), 
        border=1,relief=tk.GROOVE,padx=20,pady=20,).grid(column=j, row=i,ipadx=formato,ipady=formato)
    #Create Frames with a Label inside:
   
root.mainloop()