Declaração de Transporte - Sistema de Automação
Descrição
Este programa foi desenvolvido para automatizar a criação de declarações de transporte. Ele permite:

Gerenciar informações de clientes, transportadoras, motoristas e notas fiscais.
Gerar automaticamente um arquivo Excel com os dados preenchidos.
Exibir informações do cliente e da transportadora ao inserir seus respectivos códigos.
Funcionalidades
Interface Gráfica (Tkinter):

Inserção de dados como motorista, CPF, telefone, placa do veículo, notas fiscais.
Consulta dinâmica do nome de clientes e transportadoras com base no código.
Adição de múltiplas notas fiscais.
Base de Dados (Excel):

Os dados de clientes e transportadoras são armazenados em um arquivo Excel (base_dados.xlsx).
Busca dinâmica e validação dos códigos.
Geração de Documentos Excel:

O programa utiliza um modelo (modelo_declaracao.xlsm) para gerar arquivos preenchidos com os dados coletados.
Arquivos gerados são salvos no diretório output/.
Requisitos
1. Ambiente de Execução
Python 3.8 ou superior
Sistema Operacional: Windows, Linux ou macOS.
2. Bibliotecas Necessárias
Instale as dependências necessárias usando o comando:
bash
Copiar código
pip install pandas openpyxl
Estrutura do Projeto
A organização do projeto segue uma estrutura modular:

plaintext
Copiar código
projeto/
├── main.py                     # Ponto de entrada do programa
├── modules/
│   ├── gui.py                  # Interface gráfica principal (Tkinter)
│   ├── database.py             # Manipulação da base de dados (Excel)
│   ├── excel_generator.py      # Geração de documentos Excel
├── assets/                     # Arquivos auxiliares
│   ├── base_dados.xlsx         # Base de dados com informações de clientes/transportadoras
│   ├── modelo_declaracao.xlsm  # Modelo Excel usado para gerar declarações
├── output/                     # Diretório de saída dos arquivos gerados
│   ├── decl_transporte.xlsm    # Arquivo Excel gerado pelo programa
├── README.md                   # Documentação do projeto
Como Usar
1. Preparação
Certifique-se de que o arquivo base_dados.xlsx está localizado na pasta assets/.
Certifique-se de que o modelo Excel (modelo_declaracao.xlsm) está na mesma pasta.
2. Executando o Programa
Inicie o programa com o comando:

bash
Copiar código
python main.py
Preencha os dados necessários na interface gráfica:

Insira o código do cliente e da transportadora para buscar os nomes correspondentes.
Insira os dados do motorista, CPF, telefone, placa, e adicione as notas fiscais.
Clique em "Gerar Excel" para criar o documento no formato Excel.

3. Resultado
O arquivo Excel gerado será salvo no diretório output/ com o nome decl_transporte.xlsm.
Notas Importantes
O arquivo base_dados.xlsx deve conter as seguintes colunas:

codigo	nome	cnpj	cidade
000837	Cliente Exemplo	12.345.678/0001	São Paulo
000841	Transportadora Exemplo	98.765.432/0001	Rio de Janeiro
Certifique-se de que o código do cliente e transportadora tem 6 dígitos.

Possíveis Erros e Soluções
Erro	Causa	Solução
Cliente ou transportadora não encontrados	Código não existe ou não tem 6 dígitos	Verifique o código no arquivo base_dados.xlsx.
Arquivo Excel não gerado	Modelo não encontrado ou problema no código	Verifique se o arquivo modelo_declaracao.xlsm existe.
Mensagem "MergedCell is read-only"	Tentativa de escrever em células mescladas	Edite o modelo para corrigir as células mescladas.
Contribuição
Sugestões e melhorias são bem-vindas! Crie uma issue ou envie um pull request.
Licença
Este projeto está licenciado sob a Licença MIT.

