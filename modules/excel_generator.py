import openpyxl

def gerar_excel_com_modelo(modelo, destino, dados):
    wb = openpyxl.load_workbook(modelo)
    ws = wb.active

    ws['V5'] = f"{dados['Codigo_Cliente']}"
    ws['V6'] = f"{dados['Codigo_Transportadora']}"
    ws['D9'] = f"{dados['Motorista']}"
    ws['U9'] = f"{dados['Telefone']}"
    ws['N9'] = f"{dados['CPF']}"
    ws['V7'] = f"{dados['Placa']}"
    ws['E5'] = f"{dados['Cliente_Nome']}"
    ws['D6'] = f"{dados['Cliente_Cidade']}"
    ws['E7'] = f"{dados['Transportadora_Nome']}"
    ws['D8'] = f"{dados['Transportadora_CNPJ']}"

    # Preenche as notas fiscais
    linha_inicial =13  # Comece na linha desejada para as notas fiscais
    for nf in dados["Notas_Fiscais"]:
        ws[f"B{linha_inicial}"] = nf["Numero"]
        ws[f"J{linha_inicial}"] = nf["Peso"]
        ws[f"N{linha_inicial}"] = nf["Volumes"]
        inha_inicial +=1
    

    wb.save(destino)
