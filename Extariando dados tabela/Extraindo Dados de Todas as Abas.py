import time
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui

navegador = opcoesSelenium.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")
time.sleep(1)

linha = 1

i = 1

while i < 4:
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

    for linhaAtual in linhas:
        print(linhaAtual.text)
        linha += 1
    i +=1

    pyautogui.sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    pyautogui.sleep(2)

else:
    print("Dados extraidos com sucesso!")
