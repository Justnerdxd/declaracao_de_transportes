from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import os

def gerar_pdf(dados):
    # Define o caminho do arquivo e do layout predefinido
    numero_declaracao = dados["numero_declaracao"]
    caminho_arquivo = os.path.join("assets", f"declaracao_{numero_declaracao}.pdf")
    layout_caminho = os.path.join("assets", "layout_formulario.png")

    # Configura o PDF e o layout de página
    c = canvas.Canvas(caminho_arquivo, pagesize=A4)
    largura, altura = A4

    # Inserindo a imagem de layout predefinido como plano de fundo
    c.drawImage(layout_caminho, 0, 0, width=largura, height=altura)

    # Configurações dos textos para preencher os campos sobre o layout
    margem_x, margem_y = 2 * cm, altura - 3 * cm  # Ajuste conforme a posição do layout

    # Adicionando os dados nos locais corretos sobre o layout
    c.setFont("Helvetica", 10)
    c.drawString(margem_x, margem_y, f"Destinatário: {dados['destinatario']}")
    c.drawString(margem_x, margem_y - 20, f"Cidade: {dados['cidade']}")
    c.drawString(margem_x, margem_y - 40, f"Transportadora: {dados['transportadora']}")
    c.drawString(margem_x, margem_y - 60, f"CNPJ: {dados['cnpj_transportadora']}")
    c.drawString(margem_x, margem_y - 80, f"Motorista: {dados['motorista']}")
    c.drawString(margem_x, margem_y - 100, f"CPF/RG: {dados['cpf_motorista']}")

    # Finaliza e salva o PDF
    c.save()
    return caminho_arquivo  # Retorna o caminho do PDF gerado
