import database

# Inicializa o banco de dados e cria a nova tabela
database.inicializar_banco_novo()

# Caminho para o arquivo Excel
caminho_arquivo = 'empresas.xlsx'  # Substitua pelo caminho correto do seu arquivo Excel

# Importa os dados do Excel para a nova tabela
database.importar_dados_excel_novo(caminho_arquivo)
