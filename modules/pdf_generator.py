from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def gerar_pdf(dados):
    numero_declaracao = dados["numero_declaracao"]
    caminho_arquivo = os.path.join("assets", f"declaracao_{numero_declaracao}.pdf")
    
    c = canvas.Canvas(caminho_arquivo, pagesize=A4)
    largura, altura = A4

    margem_x, margem_y = 2 * 72, 2 * 72  # 2 cm de margem (aproximadamente)

    # Cabeçalho do PDF
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margem_x, altura - margem_y, "DECLARAÇÃO DE TRANSPORTES")
    c.setFont("Helvetica", 10)
    c.drawString(margem_x, altura - margem_y - 20, f"Destinatário: {dados['destinatario']}")
    c.drawString(margem_x, altura - margem_y - 40, f"Cidade: {dados['cidade']}")
    c.drawString(margem_x, altura - margem_y - 60, f"Transportadora: {dados['transportadora']}")
    c.drawString(margem_x, altura - margem_y - 80, f"CNPJ: {dados['cnpj_transportadora']}")
    c.drawString(margem_x, altura - margem_y - 100, f"Motorista: {dados['motorista']}")
    c.drawString(margem_x, altura - margem_y - 120, f"CPF/RG: {dados['cpf_motorista']}")
    
    c.save()
    return caminho_arquivo
