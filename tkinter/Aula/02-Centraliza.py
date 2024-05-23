import tkinter as tk 
def exit_button(master):
        window_width = 300
        window_height = 200
        # get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        master.resizable(False, False)
        button = tk.Button(master,text="Sair",bg="red",fg="white",command=master.quit)
        button.pack()
        
root = tk.Tk()
root.title("Usando tkinter")
exit_button(root)
root.mainloop()