from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

def criar_template_pdf():
    c = canvas.Canvas("H:/teste/teste/assets/template_formulario_exato.pdf", pagesize=A4)
    largura, altura = A4

    # Margens e configuração de fontes
    margem_x, margem_y = 0.5 * cm, 0.5* cm
    c.setFont("Helvetica", 10)

    # Cabeçalho - Título do formulário e dados da empresa
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margem_x, altura - margem_y, "DECLARAÇÃO DE TRANSPORTES")
    c.setFont("Helvetica", 10)
    c.drawString(margem_x, altura - margem_y - 10, "Screw Ind. Metalmecânica Eireli")
    c.drawString(margem_x, altura - margem_y - 20, "CNPJ: 00.397.908/0001-80")

    # Campo de data no canto superior direito
    c.drawString(largura - 4 * cm, altura - margem_y - 10, "out/2024")

    # Campo de código
    c.drawString(largura - 6 * cm, altura - margem_y - 30, "Código:")
    c.line(largura - 4.5 * cm, altura - margem_y - 30, largura - 2 * cm, altura - margem_y - 30)
    
    # Campo de cidade
    c.drawString(margem_x, altura - margem_y - 40, "Cidade:")
    c.line(margem_x + 2 * cm, altura - margem_y - 40, largura - margem_x - 10 * cm, altura - margem_y - 40)
    
    # Campo de transportadora
    c.drawString(margem_x, altura - margem_y - 60, "Transportadora:")
    c.line(margem_x + 4.5 * cm, altura - margem_y - 60, largura - margem_x - 10 * cm, altura - margem_y - 60)
    
    # Campo de CNPJ da transportadora
    c.drawString(largura - 8 * cm, altura - margem_y - 60, "CNPJ:")
    c.line(largura - 6 * cm, altura - margem_y - 60, largura - margem_x, altura - margem_y - 60)

    # Campo de motorista e CPF
    c.drawString(margem_x, altura - margem_y - 80, "Motorista:")
    c.line(margem_x + 3 * cm, altura - margem_y - 80, largura - margem_x - 10 * cm, altura - margem_y - 80)
    
    c.drawString(largura - 8 * cm, altura - margem_y - 80, "CPF/RG:")
    c.line(largura - 6 * cm, altura - margem_y - 80, largura - margem_x, altura - margem_y - 80)

    # Tabela de informações de coleta
    tabela_topo = altura - margem_y - 100
    tabela_dados = [
        ["Nº Nota Fiscal", "Peso Descrito", "Nº Volumes", "Observações"],
        ["", "", "", ""],  # Linha 1 de dados
        ["", "", "", ""],  # Linha 2 de dados
        ["", "", "", ""],  # Linha 3 de dados
        ["", "", "", ""],  # Linha 4 de dados
        ["", "", "", ""]   # Linha 5 de dados
    ]

    # Configuração da tabela
    tabela = Table(tabela_dados, colWidths=[5 * cm, 4 * cm, 4 * cm, 7 * cm])
    tabela.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Cabeçalho em negrito
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Fundo cinza no cabeçalho
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Grade nas células
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centralizar conteúdo
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')  # Centralizar verticalmente
    ]))

    # Desenhar a tabela no PDF
    tabela.wrapOn(c, largura, altura)
    tabela.drawOn(c, margem_x, tabela_topo - 6 * cm)

    # Rodapé: Expedição e Faturamento
    rodape_y = tabela_topo - 7 * cm
    c.drawString(margem_x, rodape_y, "Expedição: ___________________")
    c.drawString(largura - 9 * cm, rodape_y, "Faturamento: ___________________")
    c.drawString(largura - 4 * cm, rodape_y, "Nº Matrícula:")

    # Salvar o PDF
    c.save()

# Criar o layout
criar_template_pdf()
