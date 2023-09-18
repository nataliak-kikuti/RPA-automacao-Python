from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui

navegador = opcoesSelenium.Chrome()

navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

navegador.find_element(By.NAME, 'endereco').send_keys("05892387")
pyautogui.sleep(3)

navegador.find_element(By.NAME,"btn_pesquisar").click()
pyautogui.sleep(4)

rua = navegador.find_element(By. XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]   ').text
print("Rua:", rua)

bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2] ').text
print("Bairro: ", bairro)

cidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3] ').text
print("Cidade: ", cidade)

cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4] ').text
print("CEP: ", cep)




