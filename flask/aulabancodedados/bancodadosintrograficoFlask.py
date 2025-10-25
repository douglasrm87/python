from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Necessário para flash messages

# Configuração do banco de dados
def get_db():
    # Criar diretório para o banco de dados se não existir
    os.makedirs('data', exist_ok=True)
    
    # Conectar ao banco de dados
    conn = sqlite3.connect('data/banco_cidades.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        cur = db.cursor()
        
        # Criar tabela se não existir
        cur.execute('''CREATE TABLE IF NOT EXISTS cidade (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            uf TEXT NOT NULL
        )''')
        
        # Inserir dados iniciais apenas se a tabela estiver vazia
        cur.execute('SELECT COUNT(*) FROM cidade')
        if cur.fetchone()[0] == 0:
            cidades = [
                ('São Paulo', 'SP'),
                ('Curitiba', 'PR'),
                ('Florianópolis', 'SC')
            ]
            cur.executemany('INSERT INTO cidade (nome, uf) VALUES (?, ?)', cidades)
            db.commit()
        db.close()

@app.route('/')
def index():
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM cidade ORDER BY nome')
    cidades = cur.fetchall()
    db.close()
    return render_template('index.html', cidades=cidades)

@app.route('/adicionar', methods=['POST'])
def adicionar_cidade():
    nome = request.form['nome'].strip()
    uf = request.form['uf'].strip().upper()
    
    if not nome or not uf:
        flash('Por favor, preencha todos os campos', 'error')
        return redirect(url_for('index'))
    
    if len(uf) != 2:
        flash('UF deve ter exatamente 2 letras', 'error')
        return redirect(url_for('index'))
    
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('INSERT INTO cidade (nome, uf) VALUES (?, ?)', (nome, uf))
        db.commit()
        db.close()
        flash('Cidade adicionada com sucesso!', 'success')
    except sqlite3.Error as e:
        flash(f'Erro ao adicionar cidade: {e}', 'error')
    
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir_cidade(id):
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('DELETE FROM cidade WHERE id = ?', (id,))
        db.commit()
        db.close()
        flash('Cidade excluída com sucesso!', 'success')
    except sqlite3.Error as e:
        flash(f'Erro ao excluir cidade: {e}', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)