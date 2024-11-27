import tkinter as tk
from tkinter import ttk, messagebox
from modules.excel_generator import gerar_excel_com_modelo  # Função para gerar o Excel com modelo
import datetime
import os  # Import para abrir o Excel automaticamente

# Lista para armazenar entradas de notas fiscais
notas_fiscais_entries = []

def validar_entrada():
    # Valida se todos os campos obrigatórios estão preenchidos
    if not motorista_entry.get().strip():
        messagebox.showerror("Erro", "O campo 'Nome do Motorista' é obrigatório.")
        return False
    if not cpf_rg_entry.get().strip():
        messagebox.showerror("Erro", "O campo 'CPF/RG do Motorista' é obrigatório.")
        return False
    if not telefone_entry.get().strip():
        messagebox.showerror("Erro", "O campo 'Telefone do Motorista' é obrigatório.")
        return False
    if not cidade_entry.get().strip():
        messagebox.showerror("Erro", "O campo 'Cidade' é obrigatório.")
        return False
    if not transportadora_entry.get().strip():
        messagebox.showerror("Erro", "O campo 'Nome da Transportadora' é obrigatório.")
        return False
    if not cnpj_transportadora_entry.get().strip():
        messagebox.showerror("Erro", "O campo 'CNPJ da Transportadora' é obrigatório.")
        return False
    if not placa_entry.get().strip():
        messagebox.showerror("Erro", "O campo 'Placa do Veículo' é obrigatório.")
        return False
    if not destinatario_entry.get().strip():
        messagebox.showerror("Erro", "O campo 'Nome do Destinatário' é obrigatório.")
        return False
    return True

def coletar_dados_interface():
    # Valida as entradas antes de continuar
    if not validar_entrada():
        return

    # Coletar dados das notas fiscais
    notas_fiscais = []
    for entry in notas_fiscais_entries:
        numero = entry['numero'].get()
        peso = entry['peso'].get()
        volumes = entry['volumes'].get()
        observacao = entry['observacao'].get()
        if numero and peso and volumes:
            notas_fiscais.append({
                'numero': numero,
                'peso': peso,
                'volumes': volumes,
                'observacao': observacao
            })

    # Coletar dados da interface gráfica
    dados = {
        'Motorista': motorista_entry.get(),
        'CPF_RG': cpf_rg_entry.get(),
        'Telefone': telefone_entry.get(),
        'Cidade': cidade_entry.get(),
        'Transportadora': transportadora_entry.get(),
        'CNPJ_Transportadora': cnpj_transportadora_entry.get(),
        'Placa': placa_entry.get(),
        'Destinatario': destinatario_entry.get(),
        'Data': datetime.datetime.now().strftime("%d/%m/%Y"),
        'Hora': datetime.datetime.now().strftime("%H:%M"),
        'Notas_Fiscais': notas_fiscais
    }

    # Caminho do modelo e saída do Excel
    modelo_path = "TEST (1).xlsm"
    output_excel_path = f"decl_transporte_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsm"

    # Geração do Excel
    gerar_excel_com_modelo(modelo_path, output_excel_path, dados)

    # Abrir o Excel gerado automaticamente
    abrir_excel(output_excel_path)

    messagebox.showinfo("Sucesso", f"Documento Excel gerado com sucesso: {output_excel_path}")

def abrir_excel(caminho):
    """
    Função para abrir automaticamente o arquivo Excel gerado.
    """
    try:
        os.startfile(caminho)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o arquivo Excel.\nErro: {e}")

def adicionar_nota_fiscal():
    # Adiciona um conjunto de campos para uma nova nota fiscal
    row = len(notas_fiscais_entries) + 12

    nota_fields = {
        'numero': ttk.Entry(main_frame, width=10),
        'peso': ttk.Entry(main_frame, width=10),
        'volumes': ttk.Entry(main_frame, width=10),
        'observacao': ttk.Entry(main_frame, width=20)
    }
    ttk.Label(main_frame, text=f"Nota Fiscal {len(notas_fiscais_entries) + 1}").grid(row=row, column=0, columnspan=4, pady=5, sticky="w")
    ttk.Label(main_frame, text="Número:").grid(row=row + 1, column=0, sticky="e")
    nota_fields['numero'].grid(row=row + 1, column=1)
    ttk.Label(main_frame, text="Peso:").grid(row=row + 1, column=2, sticky="e")
    nota_fields['peso'].grid(row=row + 1, column=3)
    ttk.Label(main_frame, text="Volumes:").grid(row=row + 2, column=0, sticky="e")
    nota_fields['volumes'].grid(row=row + 2, column=1)
    ttk.Label(main_frame, text="Observação:").grid(row=row + 2, column=2, sticky="e")
    nota_fields['observacao'].grid(row=row + 2, column=3)

    notas_fiscais_entries.append(nota_fields)

# Configuração da janela principal
root = tk.Tk()
root.title("Declaração de Transporte")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 9))
style.configure("TButton", font=("Arial", 9, "bold"))
style.configure("TEntry", font=("Arial", 9))

# Configuração dos campos principais
ttk.Label(main_frame, text="Dados do Motorista").grid(row=0, column=0, columnspan=4, pady=5, sticky="w")
ttk.Label(main_frame, text="Nome:").grid(row=1, column=0, sticky="e")
motorista_entry = ttk.Entry(main_frame, width=30)
motorista_entry.grid(row=1, column=1, pady=5)

ttk.Label(main_frame, text="CPF/RG:").grid(row=2, column=0, sticky="e")
cpf_rg_entry = ttk.Entry(main_frame, width=15)
cpf_rg_entry.grid(row=2, column=1, pady=5)

ttk.Label(main_frame, text="Telefone:").grid(row=3, column=0, sticky="e")
telefone_entry = ttk.Entry(main_frame, width=15)
telefone_entry.grid(row=3, column=1, pady=5)

ttk.Label(main_frame, text="Cidade:").grid(row=4, column=0, sticky="e")
cidade_entry = ttk.Entry(main_frame, width=15)
cidade_entry.grid(row=4, column=1, pady=5)

ttk.Label(main_frame, text="Dados da Transportadora").grid(row=5, column=0, columnspan=4, pady=10, sticky="w")
ttk.Label(main_frame, text="Nome:").grid(row=6, column=0, sticky="e")
transportadora_entry = ttk.Entry(main_frame, width=30)
transportadora_entry.grid(row=6, column=1, pady=5)

ttk.Label(main_frame, text="CNPJ:").grid(row=7, column=0, sticky="e")
cnpj_transportadora_entry = ttk.Entry(main_frame, width=15)
cnpj_transportadora_entry.grid(row=7, column=1, pady=5)

ttk.Label(main_frame, text="Placa Veículo:").grid(row=8, column=0, sticky="e")
placa_entry = ttk.Entry(main_frame, width=15)
placa_entry.grid(row=8, column=1, pady=5)

ttk.Label(main_frame, text="Nome do Destinatário:").grid(row=9, column=0, sticky="e")
destinatario_entry = ttk.Entry(main_frame, width=30)
destinatario_entry.grid(row=9, column=1, pady=5)

# Seção de Notas Fiscais
ttk.Label(main_frame, text="Notas Fiscais").grid(row=10, column=0, columnspan=4, pady=10, sticky="w")

# Centraliza o botão ao usar columnspan=4 para ocupar o centro da grade
add_nota_button = ttk.Button(main_frame, text="Adicionar Nota Fiscal", command=adicionar_nota_fiscal)
add_nota_button.grid(row=11, column=0, columnspan=4, pady=5, sticky="n")

# Botão para gerar o documento Excel
generate_button = ttk.Button(main_frame, text="Gerar Documento Excel", command=coletar_dados_interface)
generate_button.grid(row=100, column=0, columnspan=4, pady=20)

root.mainloop()
