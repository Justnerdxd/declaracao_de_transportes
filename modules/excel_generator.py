import openpyxl

def gerar_excel_com_modelo(modelo_path, output_path, dados):
    try:
        # Carrega o modelo do Excel
        workbook = openpyxl.load_workbook(modelo_path)
        sheet = workbook.active

        # Função auxiliar para evitar erros com células mescladas
        def set_value(cell_address, value):
            cell = sheet[cell_address]
            # Verifica se a célula é mesclada
            if cell.coordinate in sheet.merged_cells:
                # Apenas a célula superior esquerda da mesclagem pode receber o valor
                for merged_range in sheet.merged_cells.ranges:
                    if cell.coordinate in merged_range:
                        top_left_cell = sheet[merged_range.min_row][merged_range.min_col - 1]
                        top_left_cell.value = value
                        return
            else:
                cell.value = value

        # Preenche os dados gerais
        set_value("V5", dados.get("Codigo_Cliente", "N/A"))
        set_value("V6", dados.get("Codigo_Transportadora", "N/A"))
        set_value("D9", dados.get("Motorista", "N/A"))
        set_value("U9", dados.get("Telefone", "N/A"))
        set_value("N9", dados.get("CPF", "N/A"))
        set_value("V7", dados.get("Placa", "N/A"))
        set_value("E5", dados.get("Cliente_Nome", "N/A"))
        set_value("D6", dados.get("Cliente_Cidade", "N/A"))
        set_value("E7", dados.get("Transportadora_Nome", "N/A"))
        set_value("D8", dados.get("Transportadora_CNPJ", "N/A"))

        # Preenche as notas fiscais
        linha_inicial = 13  # Define a linha inicial no Excel para as notas fiscais
        for nf in dados.get("Notas_Fiscais", []):
            sheet[f"B{linha_inicial}"] = nf.get("Numero", "N/A")
            sheet[f"J{linha_inicial}"] = nf.get("Peso", "N/A")
            sheet[f"N{linha_inicial}"] = nf.get("Volumes", "N/A")
            linha_inicial += 1  # Incrementa a linha para a próxima nota fiscal

        # Salva o arquivo preenchido
        workbook.save(output_path)
        print(f"Arquivo gerado com sucesso: {output_path}")

    except Exception as e:
        raise RuntimeError(f"Erro ao gerar Excel: {e}")
