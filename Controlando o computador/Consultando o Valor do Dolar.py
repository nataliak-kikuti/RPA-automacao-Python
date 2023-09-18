import pyautogui as posicaoMouse
import pyautogui as tempoEspera

posicaoMouse.moveTo(15, 1057)
tempoEspera.sleep(2)

posicaoMouse.click(15, 1057)
tempoEspera.sleep(2)

posicaoMouse.typewrite('Google Chrome')
tempoEspera.sleep(1)

posicaoMouse.press('enter')
tempoEspera.sleep(5)

posicaoMouse.typewrite('Dolar hoje')
tempoEspera.sleep(2)

posicaoMouse.press('enter')
