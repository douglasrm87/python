import tkinter as tk

def move(event):
    """will print button property _name"""
    w = event.widget                      # here we recover your Button object
    print (w._name)

root = tk.Tk()

but_strings = ['But1', 'But2', 'But3']    # As many as buttons you want to create
for label in but_strings:                 # and store them in the list 'buttons'
    button_n = tk.Button(root, text=label)
    button_n.pack()
    button_n.bind('<Button-1>', move)     # here we bind the button press event with
                                          #  the function 'move()' for each widget
root.mainloop() 