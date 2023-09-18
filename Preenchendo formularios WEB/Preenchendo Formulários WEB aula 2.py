from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.support.select import Select

navegador = webdriver.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

pyautogui.sleep(5)

navegador.find_element(By.NAME, 'q3_nome[first]').send_keys("Ana Paula")
pyautogui.sleep(1)

navegador.find_element(By.NAME, 'q3_nome[last]').send_keys("Marino")
pyautogui.sleep(1)

navegador.find_element(By.NAME, 'q4_email').send_keys("ana.paula@gmail.com")
pyautogui.sleep(3)

pegaDropDown = navegador.find_element(By.ID, 'input_5')
itemSelecionado = Select(pegaDropDown)
itemSelecionado.select_by_index(1)
pyautogui.sleep(3)

selecionarFilho = 'Não'

if selecionarFilho == 'Sim':
    navegador.find_element(By.ID, "label_input_6_0").click()
else:
    navegador.find_element(By.ID, "label_input_6_1").click()

pyautogui.sleep(3)
navegador.find_element(By.ID, 'label_input_7_2').click()
navegador.find_element(By.ID, 'label_input_7_4').click()
pyautogui.sleep(3)

navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[5]').click()
pyautogui.sleep(3)

navegador.find_element(By.ID, "input_9_0_3").click()
navegador.find_element(By.ID, "input_9_1_0").click()
pyautogui.sleep(3)
#navegador.find_element(By.ID, "input_2").click()
pyautogui.sleep(3)