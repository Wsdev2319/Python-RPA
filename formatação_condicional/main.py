import xlsxwriter as opcoesDoXlsxWriter
import os

nome_arquivo = 'c:\\Users\\Wesley\\Desktop\\python RPA\\python_excel\\formataçaocondicional.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(nome_arquivo)
sheetDados = workbook.add_worksheet()
 
formatoMaior = planilhaExcel.add_format({'bg_color': 'green',
                                         'font_color': 'white'})

formatoMenor = planilhaExcel.add_format({'bg_color': 'red',
                                         'font_color': 'white'})

inserirDados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 50, 12,34],
    [23, 32, 76, 51],
    [43, 29, 34, 12],
    [29, 58, 73, 19],
]

sheetDados.write('A1', "Células com valores >= 50 estao em verdee < 50 estao em vermelho")

for linha, range in enumerate(inserirDados):
    sheetDados.write_row(linha + 2, 1, range)
    
sheetDados.conditional_format('B4:E8', {'type': 'cell',
                                        'criteria': '>=',
                                        'value': 50,
                                        'format':formatoMaior})

sheetDados.conditional_format('B4:E8', {'type': 'cell',
                                        'criteria': '>=',
                                        'value': 50,
                                        'format':formatoMenor})


workbook.close()

os.startfile(nome_arquivo)