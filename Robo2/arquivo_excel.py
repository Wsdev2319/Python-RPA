import xlsxwriter
import os 

Caminhoarquivo = 'C:\Users\Wesley\Documents\Excel\ arquivo.xlsx'
planilhaCriada = xlsxwriter.Workbook(Caminhoarquivo)
sheet1 = planilhaCriada.add_worksheet()

#Escrevendo nas Células
sheet1.write('A1', 'Nome')

planilhaCriada.close()

os.startfile(Caminhoarquivo)