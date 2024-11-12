import sqlite3
import os

# Caminho absoluto para o banco de dados
DB_PATH = os.path.join(os.path.dirname(__file__), 'transporte.db')

# Conecte-se ao banco de dados e verifique o conteúdo
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT * FROM empresas")
rows = cursor.fetchall()
conn.close()

# Exiba o conteúdo
for row in rows:
    print(row)
