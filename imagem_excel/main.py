import xlsxwriter as opcoesDoXlsxWriter
import os

nome_arquivo = 'c:\\Users\\Wesley\\Desktop\\python RPA\\python_excel\\arquivoImagem.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(nome_arquivo)
sheetPadrao = workbook.add_worksheet()
 
sheetPadrao.write("B3", "")
sheetPadrao.insert_imagem('B5' 'c:\\Users\\Wesley\\Desktop\\python RPA\\python_excel\\arquivoImagem.xlsx')

workbook.close()

os.startfile(nome_arquivo)