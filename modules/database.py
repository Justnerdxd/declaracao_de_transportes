import sqlite3

# Função para criar o banco de dados e a tabela
def criar_bd():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS declaracoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_declaracao TEXT,
        destinatario TEXT,
        cidade TEXT,
        transportadora TEXT,
        cnpj_transportadora TEXT,
        motorista TEXT,
        cpf_motorista TEXT
    )
    """)
    
    conn.commit()
    conn.close()

# Função para salvar uma nova declaração no banco de dados
def salvar_declaracao(dados):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO declaracoes (numero_declaracao, destinatario, cidade, transportadora, cnpj_transportadora, motorista, cpf_motorista)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        dados["numero_declaracao"],
        dados["destinatario"],
        dados["cidade"],
        dados["transportadora"],
        dados["cnpj_transportadora"],
        dados["motorista"],
        dados["cpf_motorista"]
    ))
    
    conn.commit()
    conn.close()

# Função para buscar uma declaração pelo número
def buscar_declaracao(numero_declaracao):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM declaracoes WHERE numero_declaracao = ?", (numero_declaracao,))
    resultado = cursor.fetchone()
    
    conn.close()
    return resultado
