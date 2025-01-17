import aiosqlite


async def buscar_por_codigo(codigo):
    """
    Busca informações no banco de dados pelo código.
    :param codigo: Código do cliente ou transportadora.
    :return: Dicionário com as informações ou None se não encontrado.
    """
    try:
        async with aiosqlite.connect("database/transporte.db") as conn:
            cursor = await conn.execute("SELECT * FROM tabela WHERE codigo = ?", (codigo,))
            result = await cursor.fetchone()
            if result:
                return {
                    "codigo": result[0],
                    "nome": result[1],
                    "cnpj": result[2],
                    "cidade": result[3],
                }
            return None
    except Exception as e:
        print(f"Erro ao buscar no banco de dados: {e}")
        return None
