import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

class AplicativoCidades:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Cidades")
        
        # Configurar o banco de dados
        self.setup_database()
        
        # Criar widgets
        self.criar_widgets()
        
        # Carregar dados iniciais
        self.carregar_cidades()

    def setup_database(self):
        # Criar diretório para o banco de dados
        os.makedirs('data', exist_ok=True)
        
        # Conectar ao banco de dados
        self.conn = sqlite3.connect('data/banco_cidades.db')
        self.cur = self.conn.cursor()
        
        # Criar tabela se não existir
        self.cur.execute('''CREATE TABLE IF NOT EXISTS cidade (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            uf TEXT NOT NULL
        )''')
        self.conn.commit()

    def criar_widgets(self):
        # Frame para entrada de dados
        frame_entrada = ttk.LabelFrame(self.root, text="Nova Cidade", padding="10")
        frame_entrada.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        # Widgets de entrada
        ttk.Label(frame_entrada, text="Nome da Cidade:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_nome = ttk.Entry(frame_entrada, width=30)
        self.entrada_nome.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_entrada, text="UF:").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_uf = ttk.Entry(frame_entrada, width=5)
        self.entrada_uf.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Botões
        frame_botoes = ttk.Frame(frame_entrada)
        frame_botoes.grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Button(frame_botoes, text="Adicionar Cidade", command=self.adicionar_cidade).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botoes, text="Excluir Selecionada", command=self.excluir_cidade).pack(side=tk.LEFT, padx=5)

        # Frame de pesquisa
        frame_pesquisa = ttk.LabelFrame(self.root, text="Pesquisar", padding="10")
        frame_pesquisa.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        ttk.Label(frame_pesquisa, text="Filtrar:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_pesquisa = ttk.Entry(frame_pesquisa, width=30)
        self.entrada_pesquisa.grid(row=0, column=1, padx=5, pady=5)
        self.entrada_pesquisa.bind('<KeyRelease>', self.pesquisar_cidades)

        # Treeview para exibir as cidades
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Nome', 'UF'), show='headings', height=10)
        self.tree.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        # Configurar cabeçalhos
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nome', text='Nome da Cidade')
        self.tree.heading('UF', text='UF')

        # Configurar colunas
        self.tree.column('ID', width=50)
        self.tree.column('Nome', width=200)
        self.tree.column('UF', width=50)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=2, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Configurar expansão da grade
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

    def carregar_cidades(self):
        # Limpar dados existentes
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Carregar dados do banco
        self.cur.execute("SELECT * FROM cidade ORDER BY nome")
        for row in self.cur.fetchall():
            self.tree.insert('', 'end', values=row)

    def adicionar_cidade(self):
        nome = self.entrada_nome.get().strip()
        uf = self.entrada_uf.get().strip().upper()

        if not nome or not uf:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return

        if len(uf) != 2:
            messagebox.showerror("Erro", "UF deve ter exatamente 2 letras!")
            return

        try:
            self.cur.execute("INSERT INTO cidade (nome, uf) VALUES (?, ?)", (nome, uf))
            self.conn.commit()
            self.carregar_cidades()
            self.entrada_nome.delete(0, tk.END)
            self.entrada_uf.delete(0, tk.END)
            messagebox.showinfo("Sucesso", "Cidade adicionada com sucesso!")
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao adicionar cidade: {e}")

    def excluir_cidade(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione uma cidade para excluir!")
            return

        if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir esta cidade?"):
            for item in selecionado:
                cidade_id = self.tree.item(item)['values'][0]
                try:
                    self.cur.execute("DELETE FROM cidade WHERE id = ?", (cidade_id,))
                    self.conn.commit()
                except sqlite3.Error as e:
                    messagebox.showerror("Erro", f"Erro ao excluir cidade: {e}")
            self.carregar_cidades()

    def pesquisar_cidades(self, event=None):
        termo = self.entrada_pesquisa.get().strip().lower()
        
        # Limpar Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Pesquisar no banco de dados
        if termo:
            sql = "SELECT * FROM cidade WHERE lower(nome) LIKE ? OR lower(uf) LIKE ? ORDER BY nome"
            self.cur.execute(sql, (f'%{termo}%', f'%{termo}%'))
        else:
            self.cur.execute("SELECT * FROM cidade ORDER BY nome")
        
        # Preencher Treeview com resultados
        for row in self.cur.fetchall():
            self.tree.insert('', 'end', values=row)

    def __del__(self):
        # Fechar conexão com o banco de dados ao fechar o programa
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == '__main__':
    root = tk.Tk()
    app = AplicativoCidades(root)
    root.mainloop()