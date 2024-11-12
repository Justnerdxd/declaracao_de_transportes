import sqlite3
import os
import pandas as pd

# Caminho absoluto para o banco de dados
DB_PATH = os.path.join(os.path.dirname(__file__), 'transporte.db')

# Função para conectar ao banco de dados
def conectar():
    print(f"Conectando ao banco de dados em: {DB_PATH}")
    return sqlite3.connect(DB_PATH)

# Função para inicializar o banco de dados e criar a nova tabela
def inicializar_banco_novo():
    conn = conectar()
    cursor = conn.cursor()
    
    # Criação da nova tabela 'empresas_nova'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS empresas_nova (
        codigo TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        cnpj TEXT NOT NULL,
        cidade TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados e nova tabela 'empresas_nova' criados com sucesso.")

# Função para importar dados do Excel e adicionar à nova tabela
def importar_dados_excel_novo(caminho_arquivo):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_arquivo)
    
    # Exibir as colunas encontradas no arquivo Excel para verificação
    print("Colunas encontradas:", df.columns)
    
    # Remover linhas onde 'codigo' é NaN
    df = df.dropna(subset=['codigo'])

    # Converter o campo 'codigo' para string e remover duplicatas
    df['codigo'] = df['codigo'].apply(lambda x: str(int(x)) if isinstance(x, float) else str(x))
    df = df.drop_duplicates(subset=['codigo'])

    # Conectar ao banco de dados e inserir na nova tabela
    conn = conectar()
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        try:
            cursor.execute(
                "INSERT OR REPLACE INTO empresas_nova (codigo, nome, cnpj, cidade) VALUES (?, ?, ?, ?)",
                (row['codigo'], row['nome'], row['cnpj'], row['cidade'])
            )
        except sqlite3.IntegrityError:
            print(f"Erro: O código da empresa {row['codigo']} já existe.")
    
    conn.commit()
    conn.close()
    print("Dados importados com sucesso para a nova tabela 'empresas_nova'.")

# Função para listar dados da nova tabela para verificação
def listar_empresas_nova():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, nome, cnpj, cidade FROM empresas_nova")
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
        print("A tabela 'empresas_nova' está vazia.")
