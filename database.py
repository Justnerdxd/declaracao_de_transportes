import sqlite3
import pandas as pd

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect('transporte.db')

# Função para inicializar o banco de dados e criar a tabela
def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    
    # Criação da tabela 'empresas' com os campos simplificados
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS empresas (
        codigo TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        cnpj TEXT NOT NULL,
        cidade TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

# Função para inserir uma empresa (cliente ou transportadora)
def inserir_empresa(codigo, nome, cnpj, cidade):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO empresas (codigo, nome, cnpj, cidade) VALUES (?, ?, ?, ?)",
                       (codigo, nome, cnpj, cidade))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Erro: O código da empresa {codigo} já existe.")
    finally:
        conn.close()

# Função para buscar uma empresa pelo código
def buscar_empresa(codigo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, cnpj, cidade FROM empresas WHERE codigo=?", (codigo,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return {
            'nome': resultado[0],
            'cnpj': resultado[1],
            'cidade': resultado[2]
        }
    return None

# Função para listar todas as empresas
def importar_dados_excel(caminho_arquivo):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_arquivo)
    
    # Exibir as colunas encontradas no arquivo Excel para verificação
    print("Colunas encontradas:", df.columns)
    
    # Remover linhas onde 'codigo' é NaN
    df = df.dropna(subset=['codigo'])

    # Converter o campo 'codigo' para string e remover duplicatas
    df['codigo'] = df['codigo'].apply(lambda x: str(int(x)) if isinstance(x, float) else str(x))
    df = df.drop_duplicates(subset=['codigo'])

    # Conectar ao banco de dados
    conn = conectar()
    cursor = conn.cursor()
    
    # Loop para inserir cada linha do DataFrame no banco de dados
    for _, row in df.iterrows():
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO empresas (codigo, nome, cnpj, cidade) VALUES (?, ?, ?, ?)",
                (row['codigo'], row['nome'], row['cnpj'], row['cidade'])
            )
        except sqlite3.IntegrityError:
            print(f"Erro: O código da empresa {row['codigo']} já existe.")
    
    conn.commit()
    conn.close()
    print("Dados importados com sucesso!")


def visualizar_com_pandas():
    conn = conectar()
    try:
        df = pd.read_sql_query("SELECT codigo, nome, cnpj, cidade FROM empresas", conn)
        print(df)
    finally:
        conn.close()

def listar_empresas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, nome, cnpj, cidade FROM empresas")
    resultados = cursor.fetchall()
    conn.close()

    if resultados:
        for row in resultados:
            print({
                'codigo': row[0],
                'nome': row[1],
                'cnpj': row[2],
                'cidade': row[3]
            })
    else:
        print("A tabela 'empresas' está vazia.")

