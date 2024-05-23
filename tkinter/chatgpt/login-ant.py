
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import modulo_post
class BlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blog de Motocross")
        self.create_login_screen()
    def create_login_screen(self):
        self.label_login = ttk.Label(self.root, text="Faça login para continuar")
        self.label_login.pack(pady=10)
        self.label_username = ttk.Label(self.root, text="Usuário:")
        self.label_username.pack()
        self.entry_username = ttk.Entry(self.root, width=40)

        self.entry_username.pack()
        self.label_password = ttk.Label(self.root, text="Senha:")
        self.label_password.pack()
        self.entry_password = ttk.Entry(self.root, show="*", width=40)
        self.entry_password.pack()
        self.button_login = ttk.Button(self.root, text="Login", command=self.login)

        self.button_login.pack()
            

    def create_ui(self):
        self.clear_login_fields()  # Limpa os campos de login
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

            

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "drm" and password == "drm123":  # Verificação de usuário/senha básica
            self.create_ui()  # Chama o método create_ui após o login bem-sucedido
        else:
            messagebox.showerror("Erro de Login", "Credenciais inválidas. Tente novamente.")
         

    def clear_login_fields(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
    def post(self):
         # Código para a funcionalidade de publicação de postagens aqui...
        moduloPost = modulo_post()
        moduloPost.create_ui()

          

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = BlogApp(root)
    app.run()