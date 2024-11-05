import tkinter as tk
from tkinter import messagebox
from modules.excel_generator import gerar_excel_com_modelo  # Importe a função para gerar o Excel com modelo
import datetime

def coletar_dados_interface():
    # Coletar dados da interface gráfica
    dados = {
        'Motorista': motorista_entry.get(),
        'CPF_RG': cpf_rg_entry.get(),
        'Telefone': telefone_entry.get(),
        'Cidade': cidade_entry.get(),
        'Transportadora': transportadora_entry.get(),
        'CNPJ_Transportadora': cnpj_transportadora_entry.get(),
        'Placa': placa_entry.get(),
        'Data': datetime.datetime.now().strftime("%d/%m/%Y"),
        'Hora': datetime.datetime.now().strftime("%H:%M"),
        'Notas_Fiscais': [
            {'numero': '12345', 'peso': '100kg', 'volumes': '10', 'observacao': 'Nenhuma'},
            # Adicione outras notas fiscais conforme necessário
        ]
    }

    # Caminho do arquivo Excel de modelo e de saída
    modelo_path = "TEST (1).xlsm"
    output_excel_path = "decl_transporte_preenchido.xlsm"

    # Chame a função para preencher o documento Excel com o modelo e os dados
    gerar_excel_com_modelo(modelo_path, output_excel_path, dados)

    # Exibir mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Documento Excel gerado com sucesso: {output_excel_path}")

# Configuração da janela principal
root = tk.Tk()
root.title("Declaração de Transporte")

# Campos de entrada para os dados
tk.Label(root, text="Nome do Motorista:").grid(row=0, column=0, sticky="e")
motorista_entry = tk.Entry(root, width=40)
motorista_entry.grid(row=0, column=1)

tk.Label(root, text="CPF/RG do Motorista:").grid(row=1, column=0, sticky="e")
cpf_rg_entry = tk.Entry(root, width=40)
cpf_rg_entry.grid(row=1, column=1)

tk.Label(root, text="Telefone do Motorista:").grid(row=2, column=0, sticky="e")
telefone_entry = tk.Entry(root, width=40)
telefone_entry.grid(row=2, column=1)

tk.Label(root, text="Cidade:").grid(row=3, column=0, sticky="e")
cidade_entry = tk.Entry(root, width=40)
cidade_entry.grid(row=3, column=1)

tk.Label(root, text="Nome da Transportadora:").grid(row=4, column=0, sticky="e")
transportadora_entry = tk.Entry(root, width=40)
transportadora_entry.grid(row=4, column=1)

tk.Label(root, text="CNPJ da Transportadora:").grid(row=5, column=0, sticky="e")
cnpj_transportadora_entry = tk.Entry(root, width=40)
cnpj_transportadora_entry.grid(row=5, column=1)

tk.Label(root, text="Placa do Veículo:").grid(row=6, column=0, sticky="e")
placa_entry = tk.Entry(root, width=40)
placa_entry.grid(row=6, column=1)

# Botão para gerar o documento Excel
tk.Button(root, text="Gerar Documento Excel", command=coletar_dados_interface).grid(row=50, column=0, columnspan=5, pady=20)

root.mainloop()
