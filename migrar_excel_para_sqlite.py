import pandas as pd
import sqlite3
import os

# Caminhos dos arquivos
excel_path = "assets/base_dados.xlsx"  # Substitua pelo caminho do seu arquivo Excel
sqlite_path = "database/transporte.db"  # Caminho do banco SQLite

def migrar_excel_para_sqlite():
    """
    Transforma o banco de dados em Excel para um banco SQLite.
    """
    # Garante que o diretório do banco existe
    os.makedirs(os.path.dirname(sqlite_path), exist_ok=True)

    # Lê o arquivo Excel
    dados_df = pd.read_excel(excel_path)

    # Conecta ao banco SQLite
    conn = sqlite3.connect(sqlite_path)

    # Cria a tabela e insere os dados
    dados_df.to_sql("dados", conn, if_exists="replace", index=False)

    print(f"Dados migrados com sucesso para {sqlite_path}")

    # Fecha a conexão com o banco
    conn.close()

if __name__ == "__main__":
    migrar_excel_para_sqlite()
