import os
import customtkinter as ctk
from tkinter import messagebox
from modules.database import buscar_cliente, buscar_transportadora
from modules.excel_generator import gerar_excel_com_modelo

def iniciar_interface():
    def atualizar_nome_cliente():
        codigo = cliente_entry.get().strip()
        resultado = buscar_cliente(codigo)
        if resultado.empty:
            nome_cliente_label.configure(text="Cliente não encontrado", text_color="red")
        else:
            nome_cliente_label.configure(text=resultado.iloc[0]['nome'], text_color="green")

    def atualizar_nome_transportadora():
        codigo = transportadora_entry.get().strip()
        resultado = buscar_transportadora(codigo)
        if resultado.empty:
            nome_transportadora_label.configure(text="Transportadora não encontrada", text_color="red")
        else:
            nome_transportadora_label.configure(text=resultado.iloc[0]['nome'], text_color="green")

    def gerar_excel():
        if not os.path.exists("output"):
            os.makedirs("output")

        modelo_path = "assets/modelo_declaracao.xlsx"
        if not os.path.exists(modelo_path):
            messagebox.showerror("Erro", f"Modelo Excel não encontrado: {modelo_path}")
            return

        # Busca as informações adicionais do cliente e transportadora
        cliente_codigo = cliente_entry.get().strip()
        transportadora_codigo = transportadora_entry.get().strip()

        cliente_info = buscar_cliente(cliente_codigo)
        transportadora_info = buscar_transportadora(transportadora_codigo)

        # Verifica se as informações foram encontradas
        cliente_nome = cliente_info.iloc[0]['nome'] if not cliente_info.empty else "Não encontrado"
        cliente_cidade = cliente_info.iloc[0]['cidade'] if not cliente_info.empty else "Não encontrado"
        transportadora_nome = transportadora_info.iloc[0]['nome'] if not transportadora_info.empty else "Não encontrado"
        transportadora_cnpj = transportadora_info.iloc[0]['cnpj'] if not transportadora_info.empty else "Não encontrado"

        # Monta o dicionário de dados
        dados = {
            "Codigo_Cliente": cliente_codigo,
            "Cliente_Nome": cliente_nome,
            "Cliente_Cidade": cliente_cidade,
            "Codigo_Transportadora": transportadora_codigo,
            "Transportadora_Nome": transportadora_nome,
            "Transportadora_CNPJ": transportadora_cnpj,
            "Motorista": motorista_entry.get().strip() or "N/A",
            "Telefone": telefone_entry.get().strip() or "N/A",
            "CPF": cpf_entry.get().strip() or "N/A",
            "Placa": placa_entry.get().strip() or "N/A",
            "Notas_Fiscais": []
        }

        # Adiciona as notas fiscais ao dicionário
        for entry in notas_fiscais_entries:
            numero = entry['numero'].get().strip()
            peso = entry['peso'].get().strip()
            volumes = entry['volumes'].get().strip()
            if numero and peso and volumes:
                dados["Notas_Fiscais"].append({
                    "Numero": numero,
                    "Peso": peso,
                    "Volumes": volumes
                })

        # Gera o Excel com o dicionário atualizado
        try:
            output_path = os.path.abspath("output/decl_transporte.xlsx")
            gerar_excel_com_modelo(modelo_path, output_path, dados)
            messagebox.showinfo("Sucesso", f"Arquivo Excel gerado com sucesso em:\n{output_path}")
            os.startfile(output_path)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar Excel: {e}")

    def adicionar_nota_fiscal():
        row = len(notas_fiscais_entries) + 6
        nota_fields = {
            'numero': ctk.CTkEntry(frame_notas, width=150),
            'peso': ctk.CTkEntry(frame_notas, width=100),
            'volumes': ctk.CTkEntry(frame_notas, width=100)
        }

        # Alinhamento da nova linha de notas fiscais
        ctk.CTkLabel(frame_notas, text=f"Nota Fiscal {len(notas_fiscais_entries) + 1}:").grid(
            row=row, column=0, pady=5, padx=10, sticky="e"
        )
        nota_fields['numero'].grid(row=row, column=1, pady=5, padx=10, sticky="w")
        ctk.CTkLabel(frame_notas, text="Peso:").grid(row=row, column=2, pady=5, padx=10, sticky="e")
        nota_fields['peso'].grid(row=row, column=3, pady=5, padx=10, sticky="w")
        ctk.CTkLabel(frame_notas, text="Volumes:").grid(row=row, column=4, pady=5, padx=10, sticky="e")
        nota_fields['volumes'].grid(row=row, column=5, pady=5, padx=10, sticky="w")

        notas_fiscais_entries.append(nota_fields)

    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.title("Declaração de Transporte")
    root.geometry("900x700")

    # Frame Principal para Dados Gerais
    frame_top = ctk.CTkFrame(root, corner_radius=15, fg_color="gray25")
    frame_top.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    # Frame para Notas Fiscais
    frame_notas = ctk.CTkFrame(root, corner_radius=15, fg_color="gray25")
    frame_notas.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    # Frame para Botões
    frame_botoes = ctk.CTkFrame(root, corner_radius=15, fg_color="gray25")
    frame_botoes.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    # Campos principais
    ctk.CTkLabel(frame_top, text="Código do Cliente:").grid(row=0, column=0, pady=5, padx=10, sticky="e")
    cliente_entry = ctk.CTkEntry(frame_top, width=200)
    cliente_entry.grid(row=0, column=1, pady=5, padx=10)
    cliente_entry.bind("<KeyRelease>", lambda event: atualizar_nome_cliente())
    nome_cliente_label = ctk.CTkLabel(frame_top, text="", text_color="white")
    nome_cliente_label.grid(row=0, column=2, pady=5, padx=10)

    ctk.CTkLabel(frame_top, text="Código da Transportadora:").grid(row=1, column=0, pady=5, padx=10, sticky="e")
    transportadora_entry = ctk.CTkEntry(frame_top, width=200)
    transportadora_entry.grid(row=1, column=1, pady=5, padx=10)
    transportadora_entry.bind("<KeyRelease>", lambda event: atualizar_nome_transportadora())
    nome_transportadora_label = ctk.CTkLabel(frame_top, text="", text_color="white")
    nome_transportadora_label.grid(row=1, column=2, pady=5, padx=10)

    # Campos para motorista e placa
    ctk.CTkLabel(frame_top, text="Nome do Motorista:").grid(row=2, column=0, pady=5, padx=10, sticky="e")
    motorista_entry = ctk.CTkEntry(frame_top, width=200)
    motorista_entry.grid(row=2, column=1, pady=5, padx=10)

    ctk.CTkLabel(frame_top, text="Telefone do Motorista:").grid(row=3, column=0, pady=5, padx=10, sticky="e")
    telefone_entry = ctk.CTkEntry(frame_top, width=200)
    telefone_entry.grid(row=3, column=1, pady=5, padx=10)

    ctk.CTkLabel(frame_top, text="CPF do Motorista:").grid(row=4, column=0, pady=5, padx=10, sticky="e")
    cpf_entry = ctk.CTkEntry(frame_top, width=200)
    cpf_entry.grid(row=4, column=1, pady=5, padx=10)

    ctk.CTkLabel(frame_top, text="Placa do Veículo:").grid(row=5, column=0, pady=5, padx=10, sticky="e")
    placa_entry = ctk.CTkEntry(frame_top, width=200)
    placa_entry.grid(row=5, column=1, pady=5, padx=10)

    # Botões
    ctk.CTkButton(frame_botoes, text="Adicionar Nota Fiscal", command=adicionar_nota_fiscal, width=200).grid(
        row=0, column=0, pady=10, padx=10
    )
    ctk.CTkButton(frame_botoes, text="Gerar Excel", command=gerar_excel, width=200).grid(row=0, column=1, pady=10, padx=10)

    notas_fiscais_entries = []
    root.mainloop()
