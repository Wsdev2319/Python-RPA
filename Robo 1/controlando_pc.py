import pyautogui as posicaoMouse
# aguarda tempo para pc pensar
posicaoMouse.sleep(2)

# print(posicaoMouse.position())

#mover o mouse
posicaoMouse.moveTo(x=27, y=749)

#clicamos no botao start
posicaoMouse.click(x=27, y=749)


posicaoMouse.sleep(4)

print(posicaoMouse.position())
# posicaoMouse.typewrite('excel')
