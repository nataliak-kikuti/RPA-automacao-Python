import pyautogui as posicaoMouse
import pyautogui as tempoEspera

tempoEspera.sleep(1)

# print(posicaoMouse.position())
posicaoMouse.moveTo(15, 1057)
tempoEspera.sleep(2)

posicaoMouse.click(15, 1057)
tempoEspera.sleep(2)

posicaoMouse.typewrite('calculadora')
tempoEspera.sleep(1)

posicaoMouse.moveTo(294, 375)

posicaoMouse.click(294, 375)
tempoEspera.sleep(2)

print(posicaoMouse.position())

