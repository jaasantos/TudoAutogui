import pyautogui
import time

# tempolongo = random.random()
# templong = tempolongo * 20 + 3
# doloop = random.randint(3, 6)


time.sleep(2)
pyautogui.moveTo(336, 866)  # ir para pesquisar 482, 866 para safari
pyautogui.click()
time.sleep(2)
pyautogui.write('https://www.tiktok.com/pt-BR?lang=pt-BR')
pyautogui.hotkey('enter')
time.sleep(6)


for i in range(3):
    lik = pyautogui.locateOnScreen('lik.png')
    pyautogui.click(lik)
    time.sleep(1)
    comentar = pyautogui.locateOnScreen('com.png')
    pyautogui.click(comentar)
    time.sleep(2)
    emoji = pyautogui.locateOnScreen('emo.png')
    pyautogui.click(emoji)
    time.sleep(3)
    felic = pyautogui.locateOnScreen('fel.png')
    pyautogui.click(felic)
    time.sleep(3)
pyautogui.hotkey('enter')
time.sleep(3)
segui = pyautogui.locateOnScreen('seg.png')
pyautogui.click(segui)
time.sleep(3)
esc = pyautogui.locateOnScreen('esc.png')
pyautogui.click(esc)
pyautogui.vscroll(-15)
