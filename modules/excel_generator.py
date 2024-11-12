# modules/excel_generator.py

from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment
import datetime

def set_value_in_merged_cell(ws, cell, value):
    """
    Define o valor na célula superior esquerda de um intervalo mesclado.
    
    Parâmetros:
    - ws: Worksheet onde o valor será inserido.
    - cell: Célula alvo para definir o valor.
    - value: Valor a ser inserido na célula.
    """
    for merged_range in ws.merged_cells.ranges:
        if cell in merged_range:
            top_left_cell = merged_range.coord.split(":")[0]
            ws[top_left_cell].value = value
            return
    ws[cell].value = value

def gerar_excel_com_modelo(modelo_path, output_excel_path, dados):
    """
    Preenche um modelo Excel existente com os dados fornecidos.
    
    Parâmetros:
    - modelo_path: Caminho do arquivo Excel modelo (por exemplo, TEST (1).xlsm).
    - output_excel_path: Caminho para salvar o documento Excel preenchido.
    - dados: Dicionário com os dados a serem inseridos no documento.
    """
    wb = load_workbook(modelo_path, keep_vba=True)  # `keep_vba=True` mantém macros, se houver
    ws = wb.active  # Seleciona a primeira planilha ativa, ajuste se necessário

    # Preenche os dados nas células, usando a função auxiliar para células mescladas
    set_value_in_merged_cell(ws, "D9", dados['Motorista'])
    set_value_in_merged_cell(ws, "N9", dados['CPF_RG'])
    set_value_in_merged_cell(ws, "U9", dados['Telefone'])
    set_value_in_merged_cell(ws, "D6", dados['Cidade'])
    set_value_in_merged_cell(ws, "V7", dados['Placa'])
    set_value_in_merged_cell(ws, "E7", dados['Transportadora'])
    set_value_in_merged_cell(ws, "D8", dados['CNPJ_Transportadora'])
    set_value_in_merged_cell(ws, "P8", dados['Data'])
    set_value_in_merged_cell(ws, "V8", dados['Hora'])

    # Preenche a tabela de Notas Fiscais (assumindo que começa na linha 12)
    start_row = 13
    for i, nota in enumerate(dados['Notas_Fiscais'], start=start_row):
        set_value_in_merged_cell(ws, f"B{i}", nota['numero'])
        set_value_in_merged_cell(ws, f"J{i}", nota['peso'])
        set_value_in_merged_cell(ws, f"N{i}", nota['volumes'])
        set_value_in_merged_cell(ws, f"R{i}", nota['observacao'])

    # Salva o documento Excel com os dados preenchidos
    wb.save(output_excel_path)
    print(f"Documento Excel gerado e salvo em: {output_excel_path}")
