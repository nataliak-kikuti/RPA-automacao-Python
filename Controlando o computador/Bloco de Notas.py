import pyautogui

pyautogui.hotkey('win', 'r')
pyautogui.sleep(2)

pyautogui.typewrite('notepad')
pyautogui.sleep(2)

pyautogui.press('enter')
pyautogui.typewrite('Abrindo o bloco de notas ')

fecharBlocoNotas = pyautogui.getActiveWindow()
pyautogui.sleep(2)

fecharBlocoNotas.close()
pyautogui.press('tab')
pyautogui.sleep(2)
pyautogui.press('enter')

#permite pegar a janela que esta ativa

#aciona a opacao para fechar a janela ativa