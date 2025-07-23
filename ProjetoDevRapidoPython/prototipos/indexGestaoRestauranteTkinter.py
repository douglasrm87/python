import tkinter as tk
from tkinter import ttk

# Função para alternar entre os frames
def mostrar_tela(tela):
    for frame in telas.values():
        frame.pack_forget()
    telas[tela].pack(fill='both', expand=True)

# Criar janela principal
root = tk.Tk()
root.title("Sistema de Gestão de Restaurante")
root.geometry("900x600")
root.resizable(False, False)

# Cores padrão
COR_PRIMARIA = "#e74c3c"
COR_FUNDO = "#f8f8f8"
COR_TEXTO = "#2c3e50"

# Frame lateral (menu)
menu_lateral = tk.Frame(root, bg=COR_PRIMARIA, width=200)
menu_lateral.pack(side="left", fill="y")

# Frame principal (conteúdo)
conteudo = tk.Frame(root, bg=COR_FUNDO)
conteudo.pack(side="right", fill="both", expand=True)

# Cabeçalho
header = tk.Label(conteudo, text="Sistema de Gestão de Restaurante", bg=COR_PRIMARIA,
                  fg="white", font=("Segoe UI", 16), pady=10)
header.pack(fill="x")

# Dicionário de telas
telas = {}

# Tela: Dashboard
tela_dashboard = tk.Frame(conteudo, bg=COR_FUNDO)
tk.Label(tela_dashboard, text="Bem-vindo ao Sistema!", bg=COR_FUNDO, font=("Segoe UI", 14)).pack(pady=20)
telas['dashboard'] = tela_dashboard

# Tela: Mesas
tela_mesas = tk.Frame(conteudo, bg=COR_FUNDO)
tk.Label(tela_mesas, text="Mesas Disponíveis", font=("Segoe UI", 14), bg=COR_FUNDO).pack(pady=10)
mesas_frame = tk.Frame(tela_mesas, bg=COR_FUNDO)
mesas_frame.pack(pady=10)
for i in range(1, 6):
    btn = tk.Button(mesas_frame, text=f"Mesa {i}", width=10, height=2, bg="#ecf0f1")
    btn.grid(row=(i-1)//3, column=(i-1)%3, padx=10, pady=10)
telas['mesas'] = tela_mesas

# Tela: Novo Pedido
tela_pedido = tk.Frame(conteudo, bg=COR_FUNDO)
tk.Label(tela_pedido, text="Novo Pedido", font=("Segoe UI", 14), bg=COR_FUNDO).pack(pady=10)

frm_pedido = tk.Frame(tela_pedido, bg=COR_FUNDO)
frm_pedido.pack(pady=10)

tk.Label(frm_pedido, text="Mesa:", bg=COR_FUNDO).grid(row=0, column=0, sticky='e', pady=5)
combo_mesa = ttk.Combobox(frm_pedido, values=["Mesa 1", "Mesa 2", "Mesa 3"], width=30)
combo_mesa.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frm_pedido, text="Produto:", bg=COR_FUNDO).grid(row=1, column=0, sticky='e', pady=5)
combo_produto = ttk.Combobox(frm_pedido, values=["Pizza Calabresa", "Hambúrguer", "Refrigerante"], width=30)
combo_produto.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frm_pedido, text="Quantidade:", bg=COR_FUNDO).grid(row=2, column=0, sticky='e', pady=5)
entry_qtd = tk.Entry(frm_pedido, width=32)
entry_qtd.insert(0, "1")
entry_qtd.grid(row=2, column=1, padx=10, pady=5)

tk.Button(tela_pedido, text="Adicionar ao Pedido", bg=COR_PRIMARIA, fg="white",
          font=("Segoe UI", 10, "bold"), width=25).pack(pady=10)

telas['pedido'] = tela_pedido

# Tela: Pedidos
tela_pedidos = tk.Frame(conteudo, bg=COR_FUNDO)
tk.Label(tela_pedidos, text="Pedidos Atuais", font=("Segoe UI", 14), bg=COR_FUNDO).pack(pady=10)

tree = ttk.Treeview(tela_pedidos, columns=("ID", "Mesa", "Garçom", "Status"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Mesa", text="Mesa")
tree.heading("Garçom", text="Garçom")
tree.heading("Status", text="Status")
tree.pack(pady=10)

# Dados de exemplo
tree.insert("", "end", values=(101, "Mesa 1", "João", "Aberto"))
tree.insert("", "end", values=(102, "Mesa 2", "Ana", "Fechado"))

telas['pedidos'] = tela_pedidos

# Botões do menu
menu_opcoes = [
    ("🏠 Dashboard", 'dashboard'),
    ("🍽️ Mesas", 'mesas'),
    ("📝 Novo Pedido", 'pedido'),
    ("📋 Pedidos", 'pedidos')
]

for texto, chave in menu_opcoes:
    btn = tk.Button(menu_lateral, text=texto, font=("Segoe UI", 10), fg="white", bg=COR_PRIMARIA,
                    relief="flat", anchor="w", command=lambda c=chave: mostrar_tela(c))
    btn.pack(fill="x", padx=10, pady=5)

# Mostrar tela inicial
mostrar_tela("dashboard")

# Executar a interface
root.mainloop()
