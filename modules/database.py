import sqlite3

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect('database.db')

# Função para inicializar o banco de dados e criar a tabela
def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    
    # Criação da tabela 'empresas'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS empresas (
        codigo TEXT PRIMARY KEY,
        tipo TEXT NOT NULL,      -- "cliente" ou "transportadora"
        nome TEXT NOT NULL,
        cnpj TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

# Função para inserir uma empresa (cliente ou transportadora)
def inserir_empresa(codigo, tipo, nome, cnpj, cidade, estado):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO empresas (codigo, tipo, nome, cnpj, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)",
                       (codigo, tipo, nome, cnpj, cidade, estado))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Erro: O código da empresa já existe.")
    finally:
        conn.close()

# Função para buscar uma empresa pelo código
def buscar_empresa(codigo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT tipo, nome, cnpj, cidade, estado FROM empresas WHERE codigo=?", (codigo,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return {
            'tipo': resultado[0],
            'nome': resultado[1],
            'cnpj': resultado[2],
            'cidade': resultado[3],
            'estado': resultado[4]
        }
    return None

# Função para buscar empresas por tipo (cliente ou transportadora)
def buscar_empresas_por_tipo(tipo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, nome, cnpj, cidade, estado FROM empresas WHERE tipo=?", (tipo,))
    resultados = cursor.fetchall()
    conn.close()
    return [
        {
            'codigo': row[0],
            'nome': row[1],
            'cnpj': row[2],
            'cidade': row[3],
            'estado': row[4]
        }
        for row in resultados
    ]
# Em database.py

def listar_empresas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, tipo, nome, cnpj, cidade, estado FROM empresas")
    resultados = cursor.fetchall()
    conn.close()
    
    for row in resultados:
        print({
            'codigo': row[0],
            'tipo': row[1],
            'nome': row[2],
            'cnpj': row[3],
            'cidade': row[4],
            'estado': row[5]
        })
