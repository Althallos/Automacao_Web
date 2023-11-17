from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
#       Extrair Informação de um Iframe para um arquivo Excel
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
link = "https://pbdatatrader.com.br/jogosdodia"
driver.get(link)
sleep(7)
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)

#   Ler a tabela da pagina
tabela = driver.find_element(by=By.CLASS_NAME, value='innerContainer')
texto = tabela.text

#   Remove palavras que não precisa
def remover_palavra(lista_palavras, palavras):
    lista = []
    for i in lista_palavras:
        if i not in palavras:
            lista.append(i)
    return lista

lista_texto = texto.split('\n')
lista_texto = remover_palavra(lista_texto, ['Seleção de Linha', 'Selecionar Linha'])
lista_colunas = lista_texto[:10]
lista_valores = lista_texto[10:]

#   Separa os valores correspondente a coluna
def separador_lista(lista_colunas, lista_valores):
    dic = {}
    cont = 0
    for coluna in lista_colunas:
        dic[coluna] = []
    for i in range(len(lista_valores)):
        dic[lista_colunas[cont]].append(lista_valores[0])
        lista_valores.pop(0)
        cont += 1
        if cont == len(lista_colunas):
            cont = 0
    return dic
dic = separador_lista(lista_colunas, lista_valores)

tabela_df = pd.DataFrame.from_dict(dic)
for i in range(200):
    #   Dar um scroll no iframe 
    posicao_scroll = 250 * i
    driver.execute_script(f"document.getElementsByClassName('mid-viewport')[0].scroll(0, {posicao_scroll})")

    #   Ler a tabela da pagina
    tabela = driver.find_element(by=By.CLASS_NAME, value='innerContainer')
    texto = tabela.text

    #   Separar valores e colunas
    lista_texto = texto.split('\n')
    lista_texto = remover_palavra(lista_texto, ['Seleção de Linha', 'Selecionar Linha'])
    lista_colunas = lista_texto[:10]
    lista_valores = lista_texto[10:]
    #   Criar uma tabela python
    dic = separador_lista(lista_colunas, lista_valores)
    tabela_temporaria = pd.DataFrame.from_dict(dic)
    tabela_df = tabela_df._append(tabela_temporaria, ignore_index = True)

#   Remover Duplicatas
tabela_df = tabela_df.drop_duplicates()

#   Exibi a minha tabela_df / Armazenar a tabela_df em excel
print(tabela_df)
tabela_df.to_excel('Tabela_Dados_Jogos.xlsx', index=False)
