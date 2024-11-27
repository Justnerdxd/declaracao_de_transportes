import pandas as pd

BASE_DADOS = "assets/base_dados.xlsx"

def ler_base():
    """Lê a base de dados do arquivo Excel."""
    try:
        df = pd.read_excel(BASE_DADOS, dtype={'codigo': str})  # Garante que 'codigo' seja string
        print(f"Base de dados lida com sucesso. Colunas: {df.columns}")
        return df
    except FileNotFoundError:
        raise FileNotFoundError("Base de dados não encontrada.")
    except Exception as e:
        raise RuntimeError(f"Erro ao ler a base de dados: {e}")

def buscar_cliente(codigo):
    """Busca um cliente pelo código."""
    df = ler_base()
    codigo = str(codigo).zfill(6)  # Garante que o código tenha 6 dígitos
    print(f"Buscando cliente com código: {codigo}")
    resultado = df[df['codigo'] == codigo]
    print(f"Resultado da busca:\n{resultado}")
    return resultado

def buscar_transportadora(codigo):
    """Busca uma transportadora pelo código."""
    df = ler_base()
    codigo = str(codigo).zfill(6)  # Garante que o código tenha 6 dígitos
    print(f"Buscando transportadora com código: {codigo}")
    resultado = df[df['codigo'] == codigo]
    print(f"Resultado da busca:\n{resultado}")
    return resultado
