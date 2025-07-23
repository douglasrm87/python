#python -m pip install PySimpleGUI
import tkinter as tk

### CREATE VIRTUAL DISPLAY ###
#sudo apt-get install -y xvfb # Install X Virtual Frame Buffer
#sudo apt install ghostscript python3-tk
#import os
#os.system('Xvfb :2 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
#os.environ['DISPLAY']=':2'    # tell X clients to use our virtual DISPLAY :1.

def exit_button(master):
    master.geometry( "400x400" )
    button = tk.Button(master,text="Sair",bg="red",fg="white",command=master.quit)
    button.pack()
root = tk.Tk()
root.title("Usando tkinter")
exit_button(root)
root.mainloop()

