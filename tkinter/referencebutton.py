from tkinter import *

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def changeText():  
    button['text'] = 'Submitted'

button = Button(tkWindow,
	text = 'Submit',
	command = changeText)  
button.pack()  
  
tkWindow.mainloop()