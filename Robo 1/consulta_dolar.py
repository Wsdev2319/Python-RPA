import pyautogui as posicaoAbrirGoogle

#tempo para pc pensar
posicaoAbrirGoogle.sleep(4)
#print(posicaoAbrirGoogle.position())

#clicamos no botao Start

posicaoAbrirGoogle.doubleClick(x=997, y=138)

posicaoAbrirGoogle.sleep(6)

posicaoAbrirGoogle.typewrite('https://www.google.com')
posicaoAbrirGoogle.sleep(3)
posicaoAbrirGoogle.typewrite('dolar hoje')
posicaoAbrirGoogle.sleep(3)

posicaoAbrirGoogle.press('enter')

