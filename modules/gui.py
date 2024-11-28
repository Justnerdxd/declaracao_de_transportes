import os
import tkinter as tk
from tkinter import ttk, messagebox
from modules.database import buscar_transportadora, buscar_cliente
from modules.excel_generator import gerar_excel_com_modelo

def criar_pasta_output():
    """Certifica-se de que a pasta 'output' exista."""
    try:
        if not os.path.exists("output"):
            os.makedirs("output")
    except Exception as e:
        raise RuntimeError(f"Erro ao criar a pasta 'output': {e}")

def iniciar_interface():
    def atualizar_nome_cliente():
        """Atualiza o nome do cliente com base no código digitado."""
        codigo = cliente_entry.get().strip()
        if not codigo.isdigit() or len(codigo) != 6:
            nome_cliente_label.config(text="Código inválido")
            return
        try:
            resultado = buscar_cliente(codigo)
            if resultado.empty:
                nome_cliente_label.config(text="Cliente não encontrado")
            else:
                nome_cliente_label.config(text=resultado.iloc[0]['nome'])
        except FileNotFoundError:
            messagebox.showerror("Erro", "Base de dados não encontrada.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar cliente: {e}")

    def atualizar_nome_transportadora():
        """Atualiza o nome da transportadora com base no código digitado."""
        codigo = transportadora_entry.get().strip()
        if not codigo.isdigit() or len(codigo) != 6:
            nome_transportadora_label.config(text="Código inválido")
            return
        try:
            resultado = buscar_transportadora(codigo)
            if resultado.empty:
                nome_transportadora_label.config(text="Transportadora não encontrada")
            else:
                nome_transportadora_label.config(text=resultado.iloc[0]['nome'])
        except FileNotFoundError:
            messagebox.showerror("Erro", "Base de dados não encontrada.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar transportadora: {e}")

    def gerar_excel():
        criar_pasta_output()

        modelo_path = "assets/modelo_declaracao.xlsx"
        if not os.path.exists(modelo_path):
            messagebox.showerror("Erro", f"Modelo Excel não encontrado: {modelo_path}")
            return

        # Buscar dados do cliente
        cliente_codigo = cliente_entry.get().strip()
        cliente_dados = buscar_cliente(cliente_codigo)
        cliente_nome = cliente_dados.iloc[0]['nome'] if not cliente_dados.empty else "Cliente não encontrado"
        cliente_cidade = cliente_dados.iloc[0]['cidade'] if not cliente_dados.empty else "N/A"

        # Buscar dados da transportadora
        transportadora_codigo = transportadora_entry.get().strip()
        transportadora_dados = buscar_transportadora(transportadora_codigo)
        transportadora_nome = transportadora_dados.iloc[0]['nome'] if not transportadora_dados.empty else "Transportadora não encontrada"
        transportadora_cnpj = transportadora_dados.iloc[0]['cnpj'] if not transportadora_dados.empty else "N/A"

        # Preenche os dados
        dados = {
            "Codigo_Cliente": cliente_codigo,
            "Codigo_Transportadora": transportadora_codigo,
            "Motorista": motorista_entry.get().strip() or " ",
            "Telefone": telefone_entry.get().strip() or " ",
            "CPF": cpf_entry.get().strip() or " ",
            "Placa": placa_entry.get().strip(),
            "Notas_Fiscais": [],
            "Cliente_Nome": cliente_nome,
            "Cliente_Cidade": cliente_cidade,
            "Transportadora_Nome": transportadora_nome,
            "Transportadora_CNPJ": transportadora_cnpj
        }

        # Gera o Excel com os dados preenchidos
        gerar_excel_com_modelo(modelo_path, "output/decl_transporte.xlsx", dados)

        if not dados["Codigo_Cliente"] or not dados["Codigo_Transportadora"] or not dados["Placa"]:
            messagebox.showerror("Erro", "Os campos Código do Cliente, Código da Transportadora e Placa são obrigatórios.")
            return

        try:
            output_path = os.path.abspath("output/decl_transporte.xlsx")  # Caminho absoluto do arquivo
            gerar_excel_com_modelo(modelo_path, output_path, dados)
            messagebox.showinfo("Sucesso", f"Arquivo Excel gerado com sucesso em:\n{output_path}")

            # Abrir o arquivo Excel gerado automaticamente
            if os.name == 'nt':  # Windows
                os.startfile(output_path)
            else:  # macOS ou Linux
                os.system(f"open {output_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar Excel: {e}")

    def adicionar_nota_fiscal():
        """Adiciona um novo conjunto de campos para uma nova nota fiscal."""
        row = len(notas_fiscais_entries) + 8
        nota_fields = {
            'numero': ttk.Entry(root, width=10),
            'peso': ttk.Entry(root, width=10),
            'volumes': ttk.Entry(root, width=10)
        }
        ttk.Label(root, text=f"Nota Fiscal {len(notas_fiscais_entries) + 1}:").grid(row=row, column=0, pady=2, padx=5, sticky="e")
        nota_fields['numero'].grid(row=row, column=1, pady=2, padx=5)
        ttk.Label(root, text="Peso:").grid(row=row, column=2, pady=2, padx=5, sticky="e")
        nota_fields['peso'].grid(row=row, column=3, pady=2, padx=5)
        ttk.Label(root, text="Volumes:").grid(row=row, column=4, pady=2, padx=5, sticky="e")
        nota_fields['volumes'].grid(row=row, column=5, pady=2, padx=5)
        notas_fiscais_entries.append(nota_fields)


    # Configuração da janela principal
    root = tk.Tk()
    root.title("Declaração de Transporte")
    root.geometry("800x600")

    # Campos principais
    ttk.Label(root, text="Código do Cliente:").grid(row=0, column=0, pady=5, sticky="e")
    cliente_entry = ttk.Entry(root, width=15)
    cliente_entry.grid(row=0, column=1, pady=5)
    cliente_entry.bind("<KeyRelease>", lambda event: atualizar_nome_cliente())
    nome_cliente_label = ttk.Label(root, text="")
    nome_cliente_label.grid(row=0, column=2, padx=10, sticky="w")

    ttk.Label(root, text="Código da Transportadora:").grid(row=1, column=0, pady=5, sticky="e")
    transportadora_entry = ttk.Entry(root, width=15)
    transportadora_entry.grid(row=1, column=1, pady=5)
    transportadora_entry.bind("<KeyRelease>", lambda event: atualizar_nome_transportadora())
    nome_transportadora_label = ttk.Label(root, text="")
    nome_transportadora_label.grid(row=1, column=2, padx=10, sticky="w")

    ttk.Label(root, text="Nome do Motorista:").grid(row=2, column=0, pady=5, sticky="e")
    motorista_entry = ttk.Entry(root, width=30)
    motorista_entry.grid(row=2, column=1, pady=5)

    ttk.Label(root, text="Telefone:").grid(row=3, column=0, pady=5, sticky="e")
    telefone_entry = ttk.Entry(root, width=15)
    telefone_entry.grid(row=3, column=1, pady=5)

    ttk.Label(root, text="CPF:").grid(row=4, column=0, pady=5, sticky="e")
    cpf_entry = ttk.Entry(root, width=15)
    cpf_entry.grid(row=4, column=1, pady=5)

    ttk.Label(root, text="Placa do Veículo:").grid(row=5, column=0, pady=5, sticky="e")
    placa_entry = ttk.Entry(root, width=15)
    placa_entry.grid(row=5, column=1, pady=5)

    # Seção de notas fiscais
    ttk.Label(root, text="Notas Fiscais:").grid(row=6, column=0, pady=10, sticky="w")
    notas_fiscais_entries = []

    ttk.Button(root, text="Adicionar Nota Fiscal", command=adicionar_nota_fiscal).grid(row=7, column=0, pady=10)
    ttk.Button(root, text="Gerar Excel", command=gerar_excel).grid(row=7, column=1, pady=10)

    root.mainloop()
