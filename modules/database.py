import sqlite3
import os

def save_data_to_db(dados):
    # Cria (ou conecta) um banco de dados SQLite
    db_path = os.path.join(os.path.dirname(__file__), '..', 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Cria a tabela se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS declaracao_transporte (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            motorista TEXT,
            cpf_rg TEXT,
            telefone TEXT,
            cidade TEXT,
            transportadora TEXT,
            cnpj_transportadora TEXT,
            placa TEXT,
            data TEXT,
            hora TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas_fiscais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            declaracao_id INTEGER,
            numero TEXT,
            peso TEXT,
            volumes TEXT,
            observacao TEXT,
            FOREIGN KEY (declaracao_id) REFERENCES declaracao_transporte(id)
        )
    ''')

    # Insere dados na tabela de declaração de transporte
    cursor.execute('''
        INSERT INTO declaracao_transporte (
            motorista, cpf_rg, telefone, cidade, transportadora, cnpj_transportadora, placa, data, hora
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        dados['motorista'],
        dados['cpf_rg'],
        dados['telefone'],
        dados['cidade'],
        dados['transportadora'],
        dados['cnpj_transportadora'],
        dados['placa'],
        dados['data'],
        dados['hora']
    ))

    # Obtém o ID da declaração inserida
    declaracao_id = cursor.lastrowid

    # Insere dados na tabela de notas fiscais
    for nota in dados['notas_fiscais']:
        cursor.execute('''
            INSERT INTO notas_fiscais (
                declaracao_id, numero, peso, volumes, observacao
            ) VALUES (?, ?, ?, ?, ?)
        ''', (
            declaracao_id,
            nota['numero'],
            nota['peso'],
            nota['volumes'],
            nota['observacao']
        ))

    # Salva as mudanças e fecha a conexão
    conn.commit()
    conn.close()

# Teste de exemplo
if __name__ == "__main__":
    exemplo_dados = {
        "motorista": "João da Silva",
        "cpf_rg": "123.456.789-00",
        "telefone": "(11) 98765-4321",
        "cidade": "São Paulo",
        "transportadora": "Transportadora XYZ",
        "cnpj_transportadora": "12.345.678/0001-90",
        "placa": "XYZ-1234",
        "data": "10/10/2024",
        "hora": "14:30",
        "notas_fiscais": [
            {"numero": "12345", "peso": "500 kg", "volumes": "10", "observacao": "Sem avarias"},
            {"numero": "67890", "peso": "250 kg", "volumes": "5", "observacao": "Verificado"}
        ]
    }

    save_data_to_db(exemplo_dados)
    print("Dados salvos no banco de dados.")
