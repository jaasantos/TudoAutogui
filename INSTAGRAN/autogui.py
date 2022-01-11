import pyautogui
import time

'''
pyautogui.PAUSE = 2.5 => Configure uma pausa de 2,5 segundos após cada chamada PyAutoGUI:

pyautogui.FAILSAFE = True =>  Quando o modo de segurança contra falhas é True, mover o mouse
para o canto superior esquerdo levantará um pyautogui.FailSafeExceptionque pode abortar seu programa:

pyautogui.moveTo(x, y, duration= (num de segundos)  # move mouse to XY coordinates over num_second seconds
Ex.: pyautogui.moveTo(10, 20, duration = 1)

A rolagem positiva rolará para cima, a rolagem negativa rolará para baixo:
pyautogui.scroll()

Teclas de atalho do teclado como Ctrl-S ou Ctrl-Shift-1 podem ser feita passando uma lista
de nomes de teclas para hotkey():

pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste

def newTab ():
    cords = pyautogui.locateCenterOnScreen('newTab.png')
    pyautogui.click(cords)

newTab()

'''
time.sleep(2)


for i in range(10):
    def inscrevasse():
        cords = pyautogui.locateOnScreen('like.png')
        pyautogui.click(cords)
        time.sleep(1)
        pyautogui.scroll(-18)


    inscrevasse()
    time.sleep(1)
