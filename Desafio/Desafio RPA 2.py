from openpyxl import load_workbook

arquivo = "D:\\Usuários\\Natalia\\Desktop\\RPA\\Desafio\\Arquivo_Challenge.xlsx"

planilha = load_workbook(arquivo)

sheet_selecionado = planilha["Dados"]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui

navegador = webdriver.Chrome()
navegador.get("https://rpachallenge.com/")

pyautogui.sleep(3)

for linha in range(2,len(sheet_selecionado['A']) + 1):

    pyautogui.sleep(3)
    firstName = sheet_selecionado['A%s' % linha].value
    lastName = sheet_selecionado['B%s' % linha].value
    email = sheet_selecionado['F%s' % linha].value
    companyName = sheet_selecionado['C%s' % linha].value
    role = sheet_selecionado['D%s' % linha].value
    phone = sheet_selecionado['G%s' % linha].value
    address = sheet_selecionado['E%s' % linha].value


    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(firstName)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(lastName)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(email)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(companyName)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(role)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(phone)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(address)
    navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
    pyautogui.sleep(3)

print("Dados enviados com sucesso!")




