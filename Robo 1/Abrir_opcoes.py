import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm('Clique no botão desejado', buttons = ['Excel', 'Word', 'Notepad'])

if opcao == 'Excel':
    
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    
    escolha_opcao.typewrite('Excel')
    
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(4)
    
    escolha_opcao.click(x=600, y=241)
    
    escolha_opcao.sleep(3)
    escolha_opcao.typewrite('Escolhi abrir o Excel')
    
    # print(escolha_opcao.position())
    
elif opcao == 'Word':
    
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    
    escolha_opcao.typewrite('Word')
    
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(6)
    
    escolha_opcao.click(x=447, y=334)
    
    escolha_opcao.sleep(5)
    escolha_opcao.typewrite('Escolhi abrir o Word')
    
    # print(escolha_opcao.position())
    
elif opcao == 'Notepad':
    
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    
    escolha_opcao.typewrite('Notepad')
    
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(6)
    
    escolha_opcao.click(x=447, y=334)
    
    escolha_opcao.sleep(5)
    escolha_opcao.typewrite('Escolhi abrir o Notepad')