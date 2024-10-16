import xlsxwriter as opcoesDoXlsxWriter
import os

nome_arquivo = 'c:\\Users\\Wesley\\Desktop\\python RPA\\python_excel\\arquivo.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(nome_arquivo)
sheetPadrao = workbook.add_worksheet()

sheetPadrao.write("A1", "Nome")
sheetPadrao.write("B1", "Idade")
sheetPadrao.write("A2", "Amanda")
sheetPadrao.write("B2", 21)
sheetPadrao.write("A3", "Allan")
sheetPadrao.write("B3", 28)

workbook.close()

os.startfile(nome_arquivo)