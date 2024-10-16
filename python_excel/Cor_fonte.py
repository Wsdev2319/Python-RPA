import xlsxwriter as opcoesDoXlsxWriter
import os

nome_arquivo = 'c:\\Users\\Wesley\\Desktop\\python RPA\\python_excel\\fórmulas.xlsx'
minhaplanilha = opcoesDoXlsxWriter.Workbook(nome_arquivo)

sheet_Dados = minhaplanilha.add_worksheet('Dados')


sheet_Dados.write("A1", "Número 1")
sheet_Dados.write("B1", "Número 2")
sheet_Dados.write("C1", "Fórmula")


sheet_Dados.write("A2", 10)
sheet_Dados.write("A3", 6)
sheet_Dados.write("A4", 8)
sheet_Dados.write("A5", 6)
sheet_Dados.write("A8", "Ana")

sheet_Dados.write("B2", 7)
sheet_Dados.write("B3", 5)
sheet_Dados.write("B4", 3)
sheet_Dados.write("B5", 1)
sheet_Dados.write("B8", "Paula")

sheet_Dados.write_formula("C2", "=A2+B2")
sheet_Dados.write_formula("C3", "=A3-B3")
sheet_Dados.write_formula("C4", "=A4*B4")
sheet_Dados.write_formula("C5", "=A5/B5")
sheet_Dados.write_formula("C8", '=CONCATENATE(A8, " ",B8)')

sheet_Dados.set_column('A:C', 15)



minhaplanilha.close()

os.startfile(nome_arquivo)