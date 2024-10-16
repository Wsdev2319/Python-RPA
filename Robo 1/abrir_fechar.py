import pyautogui as posicaoAbreArquivos

posicaoAbreArquivos.hotkey('win', 'r')

posicaoAbreArquivos.sleep(2)

posicaoAbreArquivos.typewrite('notepad')

posicaoAbreArquivos.press('enter')

posicaoAbreArquivos.sleep(3)

posicaoAbreArquivos.typewrite('Abrimos um notepad  com um robo ou Script')

posicaoAbreArquivos.sleep(2)

# peaga a janela
fecharjanelaNotepad = posicaoAbreArquivos.getActiveWindow()

posicaoAbreArquivos.sleep(2)

#fechar janela
fecharjanelaNotepad.close()

posicaoAbreArquivos.sleep(2)

posicaoAbreArquivos.press('tab')

posicaoAbreArquivos.sleep(2)

posicaoAbreArquivos.press('enter')