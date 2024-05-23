import tkinter as tk
root = tk.Tk()
main_frame = tk.Frame(root, border=3, relief=tk.GROOVE)
main_frame.grid()
for i in range(10):
    #Create Labels for numbering the rows:
    tk.Label(main_frame, 
            text=str(i+1), 
            border=1,
            relief=tk.GROOVE,
            padx=20,
            pady=20,
            ).grid(column=0, row=i)
    #Create Frames with a Label inside:
    frame = tk.Frame(main_frame,
        border=1,
        relief=tk.GROOVE,
        background="blue",
    )
    frame.grid(row=0, column=i+1, rowspan=i+1, sticky=tk.N+tk.S)
    tk.Label(frame, 
            text='Rowspan {}'.format(i+1), 
            border=1,
            relief=tk.GROOVE,
            padx=20,
            pady=20,).grid()
root.mainloop()