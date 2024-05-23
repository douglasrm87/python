import tkinter as tk
from tkinter import ttk

class BlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blog de Motocross")

        # Crie elementos da interface aqui...

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlogApp(root)
    app.run()