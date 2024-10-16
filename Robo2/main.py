from selenium import webdriver
from selenium import webdriver as opcoes_selenium_aula
from selenium.webdriver.common.keys import Keys
#trabalha com o tempo e teclado
import pyautogui as tempoPausaComputador
import pyautogui as teclasAtalhoTeclado
# Usando o By para atualizaçoes mais recente 
from selenium.webdriver.common.by import By


#abrirNavegador = webdriver.Chrome()

#abrirNavegador.get("https://www.google.com.br/")

#autorização ao acesso ao chrome
meunavegador = opcoes_selenium_aula.Chrome()
meunavegador.get('https://www.google.com.br/')

tempoPausaComputador.sleep(4)

meunavegador.find_element(By.NAME, 'q').send_keys('Dolar hoje')

tempoPausaComputador.sleep(4)

meunavegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)

tempoPausaComputador.sleep(4) 

valor_do_dollar = meunavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valor_do_dollar)

tempoPausaComputador.sleep(47)

meunavegador.find_element(By.NAME, 'q').send_keys('')

tempoPausaComputador.sleep(4)

teclasAtalhoTeclado.press('tab')
tempoPausaComputador.sleep(4)

teclasAtalhoTeclado.press('enter')

tempoPausaComputador.sleep(4)

meunavegador.find_element(By.NAME, 'q').send_keys('euro hoje')

tempoPausaComputador.sleep(4)

meunavegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)

tempoPausaComputador.sleep(4) 

valor_do_euro = meunavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valor_do_euro)

    