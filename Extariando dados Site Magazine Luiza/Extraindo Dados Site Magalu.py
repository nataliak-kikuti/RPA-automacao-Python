from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pyautogui as funcoesTeclado

navegador = opcoesSelenium.Chrome()

navegador.get('https://www.magazineluiza.com.br/')

navegador.find_element(By.ID, 'input-search').send_keys('notebook')

tempoEspera.sleep(2)

funcoesTeclado.press("enter")
tempoEspera.sleep(10)

listaProdutos = navegador.find_elements(By.CLASS_NAME, 'gjCMbP')

for item in listaProdutos:
    nomeProduto = ''
    precoProduto = ''
    urlProduto = ''
    if nomeProduto == '':
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, 'ypydh').text
        except Exception:
            pass

    elif nomeProduto == '':
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, 'sc-ijtseF').text
        except Exception:
            pass

    print(nomeProduto)