import sqlite3

def init_erp_db():
    conn = sqlite3.connect("erp_simulado.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ordens_servico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            categoria TEXT,
            prioridade TEXT,
            equipamento TEXT,
            subestacao_local TEXT,
            descricao_resumida TEXT,
            status TEXT DEFAULT 'ABERTA'
        )
    """)
    conn.commit()
    conn.close()