from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#       Entrando no Site do Módulo Selenium Através da Navegação do Google

#   Abrindo o Navegador no Modo Privado
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

#   Entrando no site
driver.get("https://www.google.com/")

#   Escrevendo na barra de pesquisa
elemento = driver.find_element(by=By.ID, value='APjFqb')
elemento.send_keys('Selenium')

#   clicando no Botão de Pesquisar
botao = driver.find_element(by=By.CLASS_NAME, value='gNO89b')
botao.submit()

#   Clicando em um link
link = driver.find_element(by=By.CSS_SELECTOR, value="[jsname='UWckNb']")
link.click()

#   Clicando na opção Documentation
driver.find_element(by=By.LINK_TEXT, value='Documentation').click()
time.sleep(10000)
