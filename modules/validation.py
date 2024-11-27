def validar_campos(dados):
    for campo, valor in dados.items():
        if not valor.strip():
            raise ValueError(f"O campo {campo} está vazio.")
