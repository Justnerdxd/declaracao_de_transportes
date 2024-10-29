import os

def obter_numero_arquivamento():
    # Verifica se o arquivo existe, caso contrário, cria com número inicial 1
    if not os.path.exists("numero_arquivamento.txt"):
        with open("numero_arquivamento.txt", "w") as file:
            file.write("1")
        return 1

    with open("numero_arquivamento.txt", "r") as file:
        numero = int(file.read().strip())
    
    return numero

def incrementar_numero_arquivamento():
    numero = obter_numero_arquivamento() + 1
    with open("numero_arquivamento.txt", "w") as file:
        file.write(str(numero))
    return numero
