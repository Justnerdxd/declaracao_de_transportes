from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import os

def gerar_pdf_com_dados(dados):
    # Caminho do arquivo PDF
    numero_declaracao = dados["numero_declaracao"]
    caminho_arquivo = os.path.join("assets", f"declaracao_{numero_declaracao}.pdf")

    # Criando o Canvas
    c = canvas.Canvas(caminho_arquivo, pagesize=A4)
    largura, altura = A4

    # Configurações de margem
    margem_x, margem_y = 0.5 * cm, 0.5 * cm
    c.setFont("Helvetica", 10)

    # Cabeçalho - Informações da empresa e título
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margem_x, altura - margem_y, "DECLARAÇÃO DE TRANSPORTES")
    c.setFont("Helvetica", 10)
    c.drawString(margem_x, altura - margem_y - 10, "Screw Ind. Metalmecânica Eireli")
    c.drawString(margem_x, altura - margem_y - 20, "CNPJ: 00.397.908/0001-80")

    # Data e número de declaração
    c.drawString(largura - 4 * cm, altura - margem_y - 10, f"Data: {dados['data']}")
    c.drawString(margem_x + 10 * cm, altura - margem_y, f"Nº Declaração: {numero_declaracao}")

    # Campo de código
    c.drawString(largura - 6 * cm, altura - margem_y - 30, "Código:")
    c.drawString(largura - 4.5 * cm, altura - margem_y - 30, dados["codigo"])

    # Campo de cidade
    c.drawString(margem_x, altura - margem_y - 40, "Cidade:")
    c.drawString(margem_x + 2 * cm, altura - margem_y - 40, dados["cidade"])

    # Campo de transportadora
    c.drawString(margem_x, altura - margem_y - 60, "Transportadora:")
    c.drawString(margem_x + 4.5 * cm, altura - margem_y - 60, dados["transportadora"])

    # Campo de CNPJ da transportadora
    c.drawString(largura - 8 * cm, altura - margem_y - 60, "CNPJ:")
    c.drawString(largura - 6 * cm, altura - margem_y - 60, dados["cnpj_transportadora"])

    # Campo de motorista e CPF/RG
    c.drawString(margem_x, altura - margem_y - 80, "Motorista:")
    c.drawString(margem_x + 3 * cm, altura - margem_y - 80, dados["motorista"])
    c.drawString(largura - 8 * cm, altura - margem_y - 80, "CPF/RG:")
    c.drawString(largura - 6 * cm, altura - margem_y - 80, dados["cpf_motorista"])

    # Tabela de coleta
    tabela_topo = altura - margem_y - 100
    tabela_dados = [
        ["Nº Nota Fiscal", "Peso Descrito", "Nº Volumes", "Observações"],
        [dados["nota_fiscal"], dados["peso"], dados["volumes"], dados["observacoes"]]
    ]

    # Configuração da tabela
    tabela = Table(tabela_dados, colWidths=[5 * cm, 4 * cm, 4 * cm, 7 * cm])
    tabela.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))

    # Desenhar a tabela no PDF
    tabela.wrapOn(c, largura, altura)
    tabela.drawOn(c, margem_x, tabela_topo - 2 * cm)

    # Rodapé: Expedição e Faturamento
    rodape_y = tabela_topo - 7 * cm
    c.drawString(margem_x, rodape_y, "Expedição: ___________________")
    c.drawString(largura - 9 * cm, rodape_y, "Faturamento: ___________________")
    c.drawString(largura - 4 * cm, rodape_y, f"Nº Matrícula: {dados['matricula']}")

    # Salvar o PDF
    c.save()
    return caminho_arquivo  # Retorna o caminho do PDF gerado
