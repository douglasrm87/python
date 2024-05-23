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
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.root.resizable(False, False)
 
    def create_login_screen(self):
        self.label_login = ttk.Label(self.root, text="Faça login para continuar")
        self.label_login.grid(row=0,columnspan=2)

        self.label_username = ttk.Label(self.root, text="Usuário:")
        self.label_username.grid(row=5,column=0)
        self.entry_username = ttk.Entry(self.root, width=40)
        self.entry_username.grid(row=5,column=1)

        self.label_password = ttk.Label(self.root, text="Senha:")
        self.label_password.grid(row=6,column=0)
        self.entry_password = ttk.Entry(self.root, show="*", width=40)
        self.entry_password.grid(row=6,column=1)

        self.button_login = ttk.Button(self.root, text="Login", command=self.login)
        self.button_login.grid(row=8,column=1)

    

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "drm" and password == "drm123":  # Verificação de usuário/senha básica
            self.post()  # Chama o método create_ui após o login bem-sucedido
        else:
            messagebox.showerror("Erro de Login", "Credenciais inválidas. Tente novamente.")

    def clear_login_fields(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def post(self):
        # Código para a funcionalidade de publicação de postagens aqui...
        #Criando um novo Frame
        telaPost = tk.Tk()
        moduloPost = modulo_post.ModuloPost(telaPost)
        #moduloPost = modulo_post.ModuloPost(self.root)
        moduloPost.publicar()
        self.root.destroy()
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlogApp(root)
    app.run()