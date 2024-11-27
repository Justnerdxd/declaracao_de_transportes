import pandas as pd

BASE_DADOS = "assets/base_dados.xlsx"

def ler_base():
    try:
        return pd.read_excel(BASE_DADOS)
    except FileNotFoundError:
        raise FileNotFoundError("Base de dados não encontrada.")

def buscar_cliente(codigo):
    df = ler_base()
    codigo = str(codigo).zfill(6)
    return df[df['codigo'].astype(str) == codigo]

def buscar_transportadora(codigo):
    df = ler_base()
    codigo = str(codigo).zfill(6)
    return df[df['codigo'].astype(str) == codigo]
