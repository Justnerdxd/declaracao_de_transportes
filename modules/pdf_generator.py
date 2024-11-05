<<<<<<< Updated upstream
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
=======
# modules/pdf_generator.py

from pdfrw import PdfReader, PdfWriter

def preencher_pdf_campos(input_pdf_path, output_pdf_path, dados):
    """
    Preenche os campos de um PDF usando o pdfrw.
    
    Parâmetros:
    - input_pdf_path: Caminho do PDF modelo com campos de formulário.
    - output_pdf_path: Caminho para salvar o PDF preenchido.
    - dados: Dicionário com os dados a serem preenchidos nos campos do PDF. 
             As chaves devem corresponder aos nomes dos campos do PDF.
    """
    # Carrega o PDF modelo
    template = PdfReader(input_pdf_path)
    
    # Itera sobre as páginas do PDF
    for page in template.pages:
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                field = annotation.getObject()
                
                # Nome do campo
                field_name = field['/T'][1:-1]  # Remove os parênteses do nome do campo

                # Verifica se o campo está no dicionário de dados
                if field_name in dados:
                    # Atualiza o campo com o valor correspondente em `dados`
                    field.update({
                        '/V': dados[field_name],  # Valor a ser inserido no campo
                        '/Ff': 1  # Define o campo como somente leitura após preenchido
                    })

    # Salva o PDF preenchido no caminho especificado
    writer = PdfWriter()          # Cria uma instância do PdfWriter
    writer.addpages(template.pages)  # Adiciona as páginas do PDF modelo
    writer.write(output_pdf_path)     # Salva o arquivo preenchido no caminho de saída
    print(f"PDF preenchido e salvo em: {output_pdf_path}")
>>>>>>> Stashed changes
