import pyautogui as escolha_opcao

opcao = escolha_opcao.confirm('Clique no botao desejado', buttons=['Excel', 'Word', 'Notepad'])

if opcao == "Excel":
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)

    escolha_opcao.typewrite('Excel')
    escolha_opcao.sleep(2)

    escolha_opcao.press('Enter')
    escolha_opcao.sleep(5)

    escolha_opcao.click(x=392, y=342)
    escolha_opcao.sleep(3)

    escolha_opcao.typewrite('escolhi abrir no Excel')


    # print(escolha_opcao.position())
    # print("Voce escolheu abrir o Excel")
elif opcao == "Word":
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)

    escolha_opcao.typewrite('winword')
    escolha_opcao.sleep(2)

    escolha_opcao.press('Enter')
    escolha_opcao.sleep(5)

    escolha_opcao.press('Enter')
    escolha_opcao.sleep(3)

    escolha_opcao.typewrite('escolhi abrir no word')
    print("Voce escolheu abrir o Word")
else:
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)

    escolha_opcao.typewrite('notepad')
    escolha_opcao.sleep(2)

    escolha_opcao.press('Enter')
    escolha_opcao.sleep(5)

    escolha_opcao.press('Enter')
    escolha_opcao.sleep(3)

    escolha_opcao.typewrite('escolhi abrir no bloco de notas')
    print("Voce escolheu abrir o Bloco de notas")