from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera


navegador_formulario = opcoesSelenium.Chrome()
navegador_formulario.get('https://pt.surveymonkey.com/r/WLXYDX2')

tempoEspera.sleep(6)
nome = navegador_formulario.find_element(By.NAME, "166517069")
tempoEspera.sleep(1)
nome.send_keys("Amanda Martins")
tempoEspera.sleep(1)

email = navegador_formulario.find_element(By.NAME, "166517069")
tempoEspera.sleep(1)
email.send_keys("Amanda.Martins2024@gmail.com")
tempoEspera.sleep(1)

telefone = navegador_formulario.find_element(By.NAME, "166517070")
tempoEspera.sleep(1)
telefone.send_keys("(55) 5555 - 5555")
tempoEspera.sleep(1)

sobre = navegador_formulario.find_element(By.NAME, "166517073")
tempoEspera.sleep(1)
sobre.send_keys("Sei automatizar processos e planilhas em Python")
tempoEspera.sleep(1)

radio_button = navegador_formulario.find_element(By.ID, "166517071_1215509813_label")

tempoEspera.sleep(1)

radio_button.click()

tempoEspera.sleep(2)

enviar = navegador_formulario.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button' )

enviar.click()