from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pyautogui as funcoesTeclado
import pandas as pd

navegador = opcoesSelenium.Chrome()

navegador.get('https://www.magazineluiza.com.br/')

navegador.find_element(By.ID, 'input-search').send_keys('geladeira')

tempoEspera.sleep(2)

funcoesTeclado.press("enter")
tempoEspera.sleep(10)

listaDataFrame = []


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


    if precoProduto == '':
        #sc-kpDqfm eCPtRw
        try:
            precoProduto = item.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[4]/div/ul/li[1]/a/div[3]/div[2]/div/div/p').text
        except Exception:
            pass

    else:
        precoProduto = '0'
#_____________________________________________________________________________________#

    if urlProduto == '':
        #sc-kpDqfm eCPtRw
        try:
            urlProduto = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except Exception:
            pass

    else:
        urlProduto = '-'

    print(nomeProduto, " ", precoProduto)
    print(urlProduto)

    dadosLinhas = nomeProduto + ';' + precoProduto + ';' + urlProduto
    listaDataFrame.append(dadosLinhas)
    arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
    arquivoExcel._save()

    dataFrame = pd.DataFrame(listaDataFrame, columns=['Descricao; Preco; Url'])
    arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
    dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

    arquivoExcel._save()

