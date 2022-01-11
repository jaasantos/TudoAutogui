import time
import pyautogui


time.sleep(2)


comentario = "sensacional!"
tagss = "#family"


def likecoment():
    time.sleep(1)
    pyautogui.moveTo(238, 864)  # ir para pesquisar
    pyautogui.click()
    time.sleep(6)
    pyautogui.write('https://www.instagram.com/')
    pyautogui.hotkey('enter')
    time.sleep(10)
    pyautogui.moveTo(723, 136)    # ir para pesquisarf
    pyautogui.click()
    pyautogui.write(f'{tagss}')
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(7)
    pyautogui.moveTo(400, 662)
    pyautogui.click()
    time.sleep(2)

    for i in range(3):
        def inscrevasse():
            pyautogui.vscroll(-10)
            time.sleep(1)
            botlike = pyautogui.locateOnScreen('like.png')
            pyautogui.click(botlike)
            time.sleep(2.5)
            botcomentar = pyautogui.locateOnScreen('comentar.png')
            pyautogui.click(botcomentar)
            time.sleep(3.5)
            pyautogui.write(f'{comentario}')
            time.sleep(5)
            pyautogui.hotkey("enter")
            time.sleep(5)
            pyautogui.hotkey("right")
            time.sleep(2)

        inscrevasse()
        time.sleep(1)


likecoment()
