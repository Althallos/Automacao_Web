from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from time import sleep

#   Mostrar o link dos videos do YouTube sobre Python

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.youtube.com/')
driver.find_elements(by=By.ID, value="search")[1].send_keys("Python")
driver.find_elements(by=By.ID, value="search")[1].send_keys(Keys.ENTER)

#   Dar um scroll na página(Usado para carregar informações da página não carregada)
for i in range(15):         #   Da um scroll para baixo 15x
    scroll = 4000 * i
    driver.execute_script(f"window.scroll(0, {scroll})")    # Executa um script em JavaScript
    sleep(2)
lista_videos = driver.find_elements(by=By.ID, value="thumbnail")
for video in lista_videos:
    print(video.get_attribute("href"))
