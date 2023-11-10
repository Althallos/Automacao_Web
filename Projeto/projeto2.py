from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

    #   Automação Que Baixa As Cotações Do Dólar americano

#   Abrindo o Navegador no Modo Privado
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.investing.com/currencies/usd-brl-historical-data')

dowload = driver.find_element(by=By.CLASS_NAME, value='download-data_text__dP80i')
dowload.click()
driver.find_element(by=By.CLASS_NAME, value='signup_link__0v8io').click()

#   Fazendo login no site(
email = driver.find_element(by=By.CLASS_NAME, value='input_input__WivCD')
senha = driver.find_element(by=By.CLASS_NAME, value='input_password__2qtWo')

email.send_keys('email')    #   Seu E-mail de conta do site
senha.send_keys('senha')    #   Sua Senha da conta do site

driver.find_element(by=By.CLASS_NAME, value='signin_primaryBtn__54rGh').click()
sleep(5)

#   Baixando o arquivo
driver.find_element(by=By.CLASS_NAME, value='download-data_text__dP80i').click()
sleep(1000)