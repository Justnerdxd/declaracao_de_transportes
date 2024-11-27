import tkinter as tk
from tkinter import ttk, messagebox
from modules.database import buscar_transportadora, buscar_cliente
from modules.excel_generator import gerar_excel_com_modelo

def iniciar_interface():
    # Funções para buscar os nomes de cliente e transportadora
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
        """Coleta os dados da interface e gera um arquivo Excel."""
        dados = {
            "Codigo_Cliente": cliente_entry.get().strip(),
            "Codigo_Transportadora": transportadora_entry.get().strip(),
            "Motorista": motorista_entry.get().strip(),
            "Telefone": telefone_entry.get().strip(),
            "CPF": cpf_entry.get().strip(),
            "Placa": placa_entry.get().strip(),
            "Notas_Fiscais": []
        }

        # Coleta os dados das notas fiscais
        for entry in notas_fiscais_entries:
            numero = entry['numero'].get()
            peso = entry['peso'].get()
            volumes = entry['volumes'].get()
            if numero and peso and volumes:
                dados["Notas_Fiscais"].append({
                    "Numero": numero,
                    "Peso": peso,
                    "Volumes": volumes
                })

        if not all(dados.values()):
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
            return

        try:
            gerar_excel_com_modelo("assets/modelo_declaracao.xlsm", "output/decl_transporte.xlsm", dados)
            messagebox.showinfo("Sucesso", "Arquivo Excel gerado com sucesso!")
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
        ttk.Label(root, text=f"Nota Fiscal {len(notas_fiscais_entries) + 1}:").grid(row=row, column=0, pady=5, sticky="e")
        nota_fields['numero'].grid(row=row, column=1, padx=5)
        ttk.Label(root, text="Peso:").grid(row=row, column=2, padx=5)
        nota_fields['peso'].grid(row=row, column=3, padx=5)
        ttk.Label(root, text="Volumes:").grid(row=row, column=4, padx=5)
        nota_fields['volumes'].grid(row=row, column=5, padx=5)
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
