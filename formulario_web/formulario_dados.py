from openpyxl import load_workbook
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nome_arquivo = "DadosFormulario.xlsx"
planilha_aberta = load_workbook(filename=nome_arquivo)
sheet_selecionada = planilha_aberta['Dados']

for linha in range(2, len(sheet_selecionada['A']) + 1):

  nome = sheet_selecionada[f'A{linha}']. value
  email = sheet_selecionada[f'B{linha}']. value
  telefone = sheet_selecionada[f'C{linha}']. value
  sexo = sheet_selecionada[f'D{linha}']. value
  sobre = sheet_selecionada[f'e{linha}']. value
  
  
  navegador_formulario = opcoesSelenium.Chrome()
  navegador_formulario.get('https://pt.surveymonkey.com/r/WLXYDX2')
  
  espera = WebDriverWait(navegador_formulario, 10)
  
  campo_nome = espera.until(Ec.present_of_element_located((By.NAME, "166517069")))
  campo_nome.send_keys(nome)
  
  campo_email = espera.until(Ec.present_of_element_located((By.NAME, "166517069")))
  campo_email.send_keys(nome)
  
  campo_telefone = espera.until(Ec.present_of_element_located((By.NAME, "166517069")))
  campo_telefone.send_keys(nome)
  
  campo_sobre = espera.until(Ec.present_of_element_located((By.NAME, "166517069")))
  campo_sobre.send_keys(nome)
  
  if sexo == 'masculino':
    
    botao_masculino = espera.until(Ec.element_to_be_clickable((By.ID, "166517071_1215509812_label")))
    botao_masculino.click()
     
  else:
     botao_feminino = espera.until(Ec.element_to_be_clickable((By.ID, "166517071_1215509813_label")))
     botao_feminino.click()
     
  botao_enviar = espera.until(Ec.element_to_be_clickable((By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')))
  botao_enviar.click()
print('Pronto!')     
  