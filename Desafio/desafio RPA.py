from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui

navegador = webdriver.Chrome()
navegador.get("https://rpachallenge.com/")

pyautogui.sleep(3)

navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys("Amanda")
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys("Silva")
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys("amanda.silva@gmail.com")
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys("DevPython")
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys("Dev")
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys("(43)9999-9999")
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys("Avenida Maringa 123")
navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
pyautogui.sleep(3)
print("Dados enviados com sucesso!")



