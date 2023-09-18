from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui
import pandas as pd

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

pyautogui.sleep(4)

#Dicionário
dicionarioCEPS = {
    "CEP 1": "05892387",
    "CEP 2": "23548057",
    "CEP 3": "01153000"
}

listaDataFrame = []


navegador.find_element(By.NAME, "endereco").send_keys("05892387")
pyautogui.sleep(2)

navegador.find_element(By.NAME, "btn_pesquisar").click()

for contador in dicionarioCEPS.values():
    pyautogui.sleep(4)

    navegador.find_element(By.ID, 'btn_nbusca').click()

    pyautogui.sleep(3)

    navegador.find_element(By.NAME, "endereco").send_keys(contador)

    pyautogui.sleep(2)

    navegador.find_element(By.NAME, "btn_pesquisar").click()

    pyautogui.sleep(4)

    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

    endereco = ""
    for linhaTabela in elementoTabela.find_elements(By.TAG_NAME, "tr"):

        for colunaTabela in linhaTabela.find_elements(By.TAG_NAME, "td"):

            endereco = endereco + ";" + colunaTabela.text

    listaDataFrame.append(endereco)

arquivoExcel = pd.ExcelWriter('enderecosBuscaCep.xlsx',engine='xlsxwriter')
arquivoExcel._save()

dataFrame = pd.DataFrame(listaDataFrame, columns=[';Rua;Bairro;Cidade;CEP'])

arquivoExcel = pd.ExcelWriter('enderecosBuscaCep.xlsx',engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

arquivoExcel._save()



