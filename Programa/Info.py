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


#   Esperar Uma Informação Carregar Na Tela(Essa automação pode ser feita de 2 maneiras)
"""from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://medium.com/dev-cave/webdriverwait-fazendo-o-selenium-esperar-a093abeb747b')
"""
# Opção 1 : Usando uma função do selenium
"""segundos = 50
elemento = WebDriverWait(driver, segundos).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/button')))
elemento.click()
"""
# Opção 2 : criar um while que verifica se o elemento apareceu
"""while len(driver.find_elements(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/button'))==0:
    sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/button').click()
"""


#   Dar um scroll na página(Usado para carregar informações da página não carregada)
"""chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.youtube.com/')
for i in range(5):      #   Da um scroll para baixo 5x
    sleep(2)
    scroll = 4000 * i   #   Ele Recebe as Posição x, y
    driver.execute_script(f"window.scroll(0, {scroll})")    # Executa um script em JavaScript"""

#   Dar um scroll no iframe
"""chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
url = "https://pbdatatrader.com.br/jogosdodia"
driver.get(url)
sleep(7)

#   Entrando no iframe
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)

for i in range(200):     #   Da um scroll para baixo 200x
    posicao_scroll = 250 * i    #   Ele Recebe as Posição x, y
    driver.execute_script(f"document.getElementsByClassName(['mid-viewport'])[0].scroll(0, {posicao_scroll})")
    sleep(1)
"""


#   Iframe - Páginas Dentro De Páginas
"""chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
link = "https://pbdatatrader.com.br/jogosdodia"
driver.get(link)
sleep(7)
#   Entrando no 1° iframe
iframe = driver.find_element(by=By.TAG_NAME, value='iframe')
driver.switch_to.frame(iframe)

#   Entrando no 2° iframe (Um iframe dentro de outro iframe)
iframe = driver.find_element(by=By.TAG_NAME, value='iframe')
driver.switch_to.frame(iframe)

texto = driver.find_element(by=By.XPATH, value='//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[3]/div/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div[4]')
print(texto.text)

#   Voltando para a página principal (Saindo do iframe)
driver.switch_to.default_content()"""
sleep(1000)