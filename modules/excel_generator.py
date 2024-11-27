import openpyxl

def gerar_excel_com_modelo(modelo, destino, dados):
    wb = openpyxl.load_workbook(modelo)
    ws = wb.active

    ws['E5'] = f"Cliente: {dados['Codigo_Cliente']}"
    ws['E7'] = f"Transportadora: {dados['Codigo_Transportadora']}"
    ws['D9'] = f"Motorista: {dados['Motorista']}"
    ws['U9'] = f"Telefone: {dados['Telefone']}"
    ws['N9'] = f"CPF: {dados['CPF']}"
    ws['V7'] = f"Placa: {dados['Placa']}"

    row = 8
    for nf in dados["Notas_Fiscais"]:
        ws[f"B13{row}"] = nf["Numero"]
        ws[f"J13{row}"] = nf["Peso"]
        ws[f"N13{row}"] = nf["Volumes"]
        row += 1

    wb.save(destino)
