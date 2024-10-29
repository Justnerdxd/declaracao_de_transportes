import tkinter as tk
from tkinter import messagebox
from modules.database import criar_bd, salvar_declaracao
from modules.arquivamento import obter_numero_arquivamento, incrementar_numero_arquivamento
from modules.pdf_generator import gerar_pdf

# Configuração inicial do banco de dados
criar_bd()

def salvar_dados():
    numero_declaracao = obter_numero_arquivamento()
    dados = {
        "numero_declaracao": str(numero_declaracao),
        "destinatario": destinatario_entry.get(),
        "cidade": cidade_entry.get(),
        "transportadora": transportadora_entry.get(),
        "cnpj_transportadora": cnpj_transportadora_entry.get(),
        "motorista": motorista_entry.get(),
        "cpf_motorista": cpf_motorista_entry.get()
    }

    if all(dados.values()):
        salvar_declaracao(dados)
        caminho_pdf = gerar_pdf(dados)
        incrementar_numero_arquivamento()
        messagebox.showinfo("Sucesso", f"PDF gerado com sucesso! Salvo em: {caminho_pdf}")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos.")

# Interface gráfica
root = tk.Tk()
root.title("Formulário de Declaração de Transporte")
root.geometry("500x400")

# Campos de entrada
tk.Label(root, text="Destinatário").grid(row=0, column=0, sticky="e")
destinatario_entry = tk.Entry(root)
destinatario_entry.grid(row=0, column=1)

tk.Label(root, text="Cidade").grid(row=1, column=0, sticky="e")
cidade_entry = tk.Entry(root)
cidade_entry.grid(row=1, column=1)

tk.Label(root, text="Transportadora").grid(row=2, column=0, sticky="e")
transportadora_entry = tk.Entry(root)
transportadora_entry.grid(row=2, column=1)

tk.Label(root, text="CNPJ da Transportadora").grid(row=3, column=0, sticky="e")
cnpj_transportadora_entry = tk.Entry(root)
cnpj_transportadora_entry.grid(row=3, column=1)

tk.Label(root, text="Motorista").grid(row=4, column=0, sticky="e")
motorista_entry = tk.Entry(root)
motorista_entry.grid(row=4, column=1)

tk.Label(root, text="CPF/RG do Motorista").grid(row=5, column=0, sticky="e")
cpf_motorista_entry = tk.Entry(root)
cpf_motorista_entry.grid(row=5, column=1)

# Botão de salvar
salvar_button = tk.Button(root, text="Salvar e Gerar PDF", command=salvar_dados)
salvar_button.grid(row=6, columnspan=2)

root.mainloop()
