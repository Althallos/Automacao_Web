from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

#   Abrindo um navegador
"""driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)"""

#   Abrir o Navegador sem mostrar
"""chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://google.com")
print(driver.title)"""

#   Abrir um Navegador no Modo Privado (Anônima) 
"""chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://google.com")
print(driver.title)"""

#   Esperar Uma Informação Carregar Na Tela
"""from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://medium.com/dev-cave/webdriverwait-fazendo-o-selenium-esperar-a093abeb747b')

segundos = 50
elemento = WebDriverWait(driver, segundos).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/button')))

elemento.click()"""
sleep(1000)