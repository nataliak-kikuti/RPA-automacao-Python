from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

from selenium.webdriver.support.select import Select

navegador = webdriver.Chrome()

navegador.get("https://pt.surveymonkey.com/r/7GX9XRZ")
pyautogui.sleep(5)

navegador.find_element(By.NAME, '72542598').send_keys("Pedro")
navegador.find_element(By.NAME, '72542821').send_keys("pedro.silva@gmail.com")
pyautogui.sleep(3)

sexo = "masculino"
if sexo == "masculino":
    navegador.find_element(By.XPATH, '//*[@id="72542994_583517054_label"]/span[1]').click()
else:
    navegador.find_element(By.XPATH, '//*[@id="72542994_583517055_label"]/span[1]').click()

pyautogui.sleep(3)

pegaDropDown = navegador.find_element(By.ID, '72543178')
itemSelecionado = Select(pegaDropDown)
itemSelecionado.select_by_index(2)

pyautogui.sleep(3)

navegador.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()
pyautogui.sleep(3)