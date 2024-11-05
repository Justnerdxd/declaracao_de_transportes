import fitz  # PyMuPDF

def preencher_pdf(input_pdf_path, output_pdf_path, dados, notas_fiscais):
    # Abrir o PDF original
    pdf_document = fitz.open(input_pdf_path)
    page = pdf_document[0]  # Considerando que os dados estão na primeira página

    # Dados para preencher
    campos = {
        "Motorista": (100, 150),  # Ajuste as coordenadas para a posição correta
        "CPF/RG": (100, 170),
        "Telefone": (100, 190),
        "Cidade": (100, 210),
        "Transportadora": (100, 230),
        "CNPJ Transportadora": (100, 250),
        "Placa": (100, 270),
        "Data": (100, 290),
        "Hora": (100, 310)
    }

    # Preencher os campos principais
    for campo, valor in dados.items():
        if campo in campos:
            x, y = campos[campo]
            page.insert_text((x, y), valor, fontsize=10, fontname="helv")

    # Preencher a tabela de notas fiscais
    y = 340  # Início da tabela de notas fiscais
    for nota in notas_fiscais:
        page.insert_text((50, y), nota['numero'], fontsize=10, fontname="helv")
        page.insert_text((150, y), nota['peso'], fontsize=10, fontname="helv")
        page.insert_text((250, y), nota['volumes'], fontsize=10, fontname="helv")
        page.insert_text((350, y), nota['observacao'], fontsize=10, fontname="helv")
        y += 20  # Incrementar para a próxima linha da tabela

    # Salvar o PDF preenchido
    pdf_document.save(output_pdf_path)
    pdf_document.close()
