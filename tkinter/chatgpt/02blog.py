import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class BlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blog de Motocross")

        self.create_ui()

    def create_ui(self):
        self.label_title = ttk.Label(self.root, text="Blog de Notícias de Motocross", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        self.label_new_post = ttk.Label(self.root, text="Nova Postagem")
        self.label_new_post.pack()

        self.entry_title = ttk.Entry(self.root, width=40)
        self.entry_title.pack()

        self.text_content = scrolledtext.ScrolledText(self.root, width=40, height=10)
        self.text_content.pack()

        self.button_post = ttk.Button(self.root, text="Publicar", command=self.post)
        self.button_post.pack()

        self.label_posts = ttk.Label(self.root, text="Últimas Postagens")
        self.label_posts.pack(pady=10)

        self.listbox_posts = tk.Listbox(self.root, width=40, height=10)
        self.listbox_posts.pack()

    def post(self):
        title = self.entry_title.get()
        content = self.text_content.get("1.0", tk.END)

        if title and content:
            self.listbox_posts.insert(tk.END, title)
            self.clear_input_fields()

    def clear_input_fields(self):
        self.entry_title.delete(0, tk.END)
        self.text_content.delete("1.0", tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlogApp(root)
    app.run()