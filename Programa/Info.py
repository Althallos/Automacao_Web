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

# Essa automação pode ser feita de 2 maneiras
#   Opção 1 : Usando uma função do selenium
"""from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://medium.com/dev-cave/webdriverwait-fazendo-o-selenium-esperar-a093abeb747b')

segundos = 50
elemento = WebDriverWait(driver, segundos).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/button')))
elemento.click()
"""
#   Opção 2 : criar uma função
"""while len(driver.find_elements(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/button'))==0:
    sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/button').click()"""
sleep(1000)