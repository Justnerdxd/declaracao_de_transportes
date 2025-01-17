import os
import customtkinter as ctk
from tkinter import messagebox, Canvas, Scrollbar
from modules.database import buscar_por_codigo
from modules.excel_generator import gerar_excel_com_modelo


def iniciar_interface():
    def atualizar_nome_destinatario():
        """Atualiza o nome do destinatário com base no código digitado."""
        codigo = cliente_entry.get().strip()
        destinatario = buscar_por_codigo(codigo)
        if not destinatario:
            nome_cliente_label.configure(text="Destinatário não encontrado", text_color="red")
        else:
            nome_cliente_label.configure(text=destinatario["nome"], text_color="green")

    def atualizar_nome_transportadora():
        """Atualiza o nome da transportadora com base no código digitado."""
        codigo = transportadora_entry.get().strip()
        transportadora = buscar_por_codigo(codigo)
        if not transportadora:
            nome_transportadora_label.configure(text="Transportadora não encontrada", text_color="red")
        else:
            nome_transportadora_label.configure(text=transportadora["nome"], text_color="green")

    def gerar_excel():
        """Gera o arquivo Excel com os dados fornecidos."""
        try:
            cliente_codigo = cliente_entry.get().strip()
            transportadora_codigo = transportadora_entry.get().strip()
            motorista = motorista_entry.get().strip()

            if not cliente_codigo or not transportadora_codigo or not motorista:
                messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
                return

            destinatario = buscar_por_codigo(cliente_codigo)
            transportadora = buscar_por_codigo(transportadora_codigo)

            if not destinatario:
                messagebox.showerror("Erro", "Cliente não encontrado.")
                return

            if not transportadora:
                messagebox.showerror("Erro", "Transportadora não encontrada.")
                return

            dados = {
                "Codigo_Cliente": cliente_codigo,
                "Cliente_Nome": destinatario.get("nome", "Não encontrado"),
                "Cliente_Cidade": destinatario.get("cidade", "Não encontrado"),
                "Codigo_Transportadora": transportadora_codigo,
                "Transportadora_Nome": transportadora.get("nome", "Não encontrado"),
                "Transportadora_CNPJ": transportadora.get("cnpj", "Não encontrado"),
                "Motorista": motorista,
                "Telefone": telefone_entry.get().strip(),
                "CPF": cpf_entry.get().strip(),
                "Placa": placa_entry.get().strip(),
                "Notas_Fiscais": [
                    {"Numero": e["numero"].get(), "Peso": e["peso"].get(), "Volumes": e["volumes"].get()}
                    for e in notas_fiscais_entries
                ],
            }

            if not os.path.exists("output"):
                os.makedirs("output")

            modelo_path = "assets/modelo_declaracao.xlsx"
            if not os.path.exists(modelo_path):
                messagebox.showerror("Erro", f"Modelo Excel não encontrado: {modelo_path}")
                return

            output_path = os.path.abspath("output/decl_transporte.xlsx")
            gerar_excel_com_modelo(modelo_path, output_path, dados)
            messagebox.showinfo("Sucesso", f"Arquivo Excel gerado com sucesso em:\n{output_path}")
            os.startfile(output_path)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar Excel: {e}")

    def criar_secao_rolavel(master):
        """Cria uma seção rolável para adicionar widgets dinamicamente."""
        canvas = Canvas(master, bg="gray25", highlightthickness=0)
        scrollbar = Scrollbar(master, orient="vertical", command=canvas.yview)
        frame = ctk.CTkFrame(canvas, corner_radius=15, fg_color="gray25")

        # Configurar a rolagem
        frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return frame

    def adicionar_nota_fiscal():
        """Adiciona campos de entrada para uma nova nota fiscal."""
        row = len(notas_fiscais_entries) + 1
        nota_fields = {
            'numero': ctk.CTkEntry(frame_notas, width=150),
            'peso': ctk.CTkEntry(frame_notas, width=100),
            'volumes': ctk.CTkEntry(frame_notas, width=100),
        }

        ctk.CTkLabel(frame_notas, text=f"Nota Fiscal {row}:").grid(
            row=row, column=0, pady=5, padx=10, sticky="e"
        )
        nota_fields['numero'].grid(row=row, column=1, pady=5, padx=10, sticky="w")
        ctk.CTkLabel(frame_notas, text="Peso:").grid(row=row, column=2, pady=5, padx=10, sticky="e")
        nota_fields['peso'].grid(row=row, column=3, pady=5, padx=10, sticky="w")
        ctk.CTkLabel(frame_notas, text="Volumes:").grid(row=row, column=4, pady=5, padx=10, sticky="e")
        nota_fields['volumes'].grid(row=row, column=5, pady=5, padx=10, sticky="w")

        notas_fiscais_entries.append(nota_fields)

    # Configuração inicial da interface gráfica
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.title("Declaração de Transporte")
    root.geometry("900x700")

    # Frames para organizar os elementos
    frame_top = ctk.CTkFrame(root, corner_radius=15, fg_color="gray25")
    frame_top.pack(padx=20, pady=10, fill="x")

    frame_notas_container = ctk.CTkFrame(root, corner_radius=15, fg_color="gray25")
    frame_notas_container.pack(padx=20, pady=10, fill="both", expand=True)
    frame_notas = criar_secao_rolavel(frame_notas_container)

    frame_botoes = ctk.CTkFrame(root, corner_radius=15, fg_color="gray25")
    frame_botoes.pack(padx=20, pady=10, fill="x")

    # Campos para cliente e transportadora
    ctk.CTkLabel(frame_top, text="Código do Cliente:").grid(row=0, column=0, pady=5, padx=10, sticky="e")
    cliente_entry = ctk.CTkEntry(frame_top, width=200)
    cliente_entry.grid(row=0, column=1, pady=5, padx=10)
    cliente_entry.bind("<KeyRelease>", lambda e: atualizar_nome_destinatario())
    nome_cliente_label = ctk.CTkLabel(frame_top, text="", text_color="white")
    nome_cliente_label.grid(row=0, column=2, pady=5, padx=10)

    ctk.CTkLabel(frame_top, text="Código da Transportadora:").grid(row=1, column=0, pady=5, padx=10, sticky="e")
    transportadora_entry = ctk.CTkEntry(frame_top, width=200)
    transportadora_entry.grid(row=1, column=1, pady=5, padx=10)
    transportadora_entry.bind("<KeyRelease>", lambda e: atualizar_nome_transportadora())
    nome_transportadora_label = ctk.CTkLabel(frame_top, text="", text_color="white")
    nome_transportadora_label.grid(row=1, column=2, pady=5, padx=10)

    # Campos para motorista e veículo
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

    # Seção de notas fiscais
    notas_fiscais_entries = []  # Lista para armazenar as entradas de notas fiscais
    adicionar_nota_fiscal()  # Adiciona a primeira nota fiscal automaticamente

    # Botão para adicionar mais notas fiscais
    adicionar_button = ctk.CTkButton(frame_notas, text="Adicionar Nota Fiscal", command=adicionar_nota_fiscal)
    adicionar_button.grid(row=0, column=0, pady=20, padx=20, columnspan=6)

    # Botão para gerar Excel
    gerar_button = ctk.CTkButton(frame_botoes, text="Gerar Excel", command=gerar_excel)
    gerar_button.pack(pady=20, padx=20)

    root.mainloop()
