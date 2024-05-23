import tkinter as tk

top = tk.Tk()

B1 = tk.Button(top, text ="FLAT", relief=tk.FLAT )
B2 = tk.Button(top, text ="RAISED", relief=tk.RAISED )
B3 = tk.Button(top, text ="SUNKEN", relief=tk.SUNKEN )
B4 = tk.Button(top, text ="GROOVE", relief=tk.GROOVE )
B5 = tk.Button(top, text ="RIDGE", relief=tk.RIDGE )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()