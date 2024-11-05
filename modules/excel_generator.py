# modules/excel_generator.py

from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment
import datetime

def gerar_excel_com_modelo(modelo_path, output_excel_path, dados):
    """
    Preenche um modelo Excel existente com os dados fornecidos.
    
    Parâmetros:
    - modelo_path: Caminho do arquivo Excel modelo (por exemplo, TEST (1).xlsm).
    - output_excel_path: Caminho para salvar o documento Excel preenchido.
    - dados: Dicionário com os dados a serem inseridos no documento.
    """
    # Carrega o arquivo modelo
    wb = load_workbook(modelo_path, keep_vba=True)  # `keep_vba=True` mantém macros, se houver
    ws = wb.active  # Seleciona a primeira planilha ativa, ajuste se necessário

    # Preenche os dados na primeira célula da área mesclada
    ws["B2"].value = dados['Motorista']             # Ajuste as células conforme o layout do modelo
    ws["B3"].value = dados['CPF_RG']
    ws["B4"].value = dados['Telefone']
    ws["B5"].value = dados['Cidade']
    ws["B6"].value = dados['Placa']
    ws["B7"].value = dados['Transportadora']
    ws["B8"].value = dados['CNPJ_Transportadora']
    ws["B9"].value = dados['Data']
    ws["B10"].value = dados['Hora']

    # Tabela de Notas Fiscais (assumindo que começa na linha 12)
    start_row = 12
    for i, nota in enumerate(dados['Notas_Fiscais'], start=start_row):
        ws[f"A{i}"].value = nota['numero']
        ws[f"B{i}"].value = nota['peso']
        ws[f"C{i}"].value = nota['volumes']
        ws[f"D{i}"].value = nota['observacao']

    # Salva o documento Excel com os dados preenchidos
    wb.save(output_excel_path)
    print(f"Documento Excel gerado e salvo em: {output_excel_path}")
