import database

# Inicializa o banco de dados e cria a tabela (se necessário)
database.inicializar_banco()

# Caminho para o arquivo Excel
caminho_arquivo = 'empresas.xlsx'  # Substitua pelo caminho correto do seu arquivo Excel

# Importa os dados do Excel para o banco de dados
database.importar_dados_excel(caminho_arquivo)
