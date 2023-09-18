from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

navegador = webdriver.Chrome()

navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

navegador.find_element(By.NAME, 'endereco').send_keys("05892387")
pyautogui.sleep(3)

navegador.find_element(By.NAME,"btn_pesquisar").click()
pyautogui.sleep(4)

elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

for linhaTabela in elementoTabela.find_elements(By.TAG_NAME, 'tr'):
    endereco = ""
    for colunaTabela in linhaTabela.find_elements(By.TAG_NAME, 'td'):
        endereco = endereco + ";" + colunaTabela.text
print(endereco)


