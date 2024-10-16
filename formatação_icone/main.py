import xlsxwriter as opcoesDoXlsxWriter
import os

nome_arquivo = 'c:\\Users\\Wesley\\Desktop\\python RPA\\python_excel\\formataçaocondicional.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(nome_arquivo)
sheetDados = workbook.add_worksheet()

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
    
sheetDados.conditional_format('B4:E8', {'type': 'icon_set',
                                        'icon_style': '3_traffic_lights'})

sheetDados.conditional_format('B4:E8', {'type': 'icon_set',
                                        'icon_style': '3_traffic_lights',
                                        'reverse_icons': True})

sheetDados.conditional_format('B4:E8', {'type': 'icon_set',
                                        'icon_style': '3_arrows'})

sheetDados.conditional_format('B4:E8', {'type': 'icon_set',
                                        'icon_style': '4_arrows'})

sheetDados.conditional_format('B4:E8', {'type': 'icon_set',
                                        'icon_style': '5_ratings'})


workbook.close()

os.startfile(nome_arquivo)