import xlsxwriter as opcoesDoXlsxWriter
import os

caminho_arquivo = 'c:\\Users\\Wesley\\Desktop\\Python RPA\\Grafico.xlsx'
planilhaExcel = opcoesDoXlsxWriter.Workbook(caminho_arquivo)


sheetDados = planilhaExcel.add_worksheet("Resumo")

linhaNegrito = planilhaExcel.add_format({'bold': 1})

Titulos = ['Vendedores', 'Total Vendas']
dadosTabela = [
    ["Ana", "Pedro", "Allan", "Francisco", "Rosa", "Amanda"],
    [400, 300, 89, 34, 350, 120]
]

sheetDados.write_row('A1', Titulos, linhaNegrito)
sheetDados.write_column('A2', dadosTabela[0])
sheetDados.write_column('B2', dadosTabela[1])

graficoColuna = planilhaExcel.add_chart({'type': 'column'})

graficoColuna.add_series({
    'nome': '=Resumo!$B$1',
    'categoria': '=Resumo!$A$2:$A$7',
    'valor': '=Resumo!$B$2:$B$7',
})

graficoColuna.set_title({'nome': 'Gráfico total de Vendas'})
graficoColuna.set_x_axis({'nome': 'Vendedores'})
graficoColuna.set_y_axis({'nome': 'Vendas'})

graficoColuna.set_style(11)
sheetDados.insert_chart('D2', graficoColuna, {'x_offset': 25, 'y_offset': 10})

##############################################################################              
graficoEmpilhado = planilhaExcel.add_chart({'type': 'area', 'subtype': 'starket'})

graficoEmpilhado.add_series({
    'nome': '=Resumo!$B$1',
    'categoria': '=Resumo!$A$2:$A$7',
    'valor': '=Resumo!$B$2:$B$7',
})

graficoEmpilhado.set_title({'nome': 'Grafico Empilhado'})
graficoEmpilhado.set_x_axis({'nome': 'fucionarios'})
graficoEmpilhado.set_y_axis({'nome': 'Vendas'})

graficoEmpilhado.set_style(11)
sheetDados.insert_chart('L2', graficoColuna, {'x_offset': 25, 'y_offset': 10})


planilhaExcel.close()

os.startfile(caminho_arquivo)