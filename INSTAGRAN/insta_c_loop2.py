import time
import pyautogui
import random


tempolongo = random.random()
templong = tempolongo * 20 + 3
doloop = random.randint(3, 6)

for i in range(doloop):

    tag = ["#atitude","#pilar", "#iati", "#estreladealagoas", "macqueen", "#teotoniovilela", "#murici",
           "coruripe, alagoas, brasil", "#aracaju", "#vaquejada","#familia", "#nordeste",
           "#determinacao", "#festa", "#deusnocomando", "#resenha", "#viagem", "#fe", "#decoracao",
           "#garanhuns", "#pernambuco", "#vaquejada", "#brasil", "#favela", "filme","#deus", "#esperanca",
           "#fazenda", "#comedia", "#memebr", "#vida", "#sitio", "#filho"]

    realtime = random.random()
    tempo1 = realtime * 3 + 4
    tempo2 = realtime * 4 + 3
    tempo4 = realtime * 4 + 4

    tagss = random.choice(tag)
    realismo = random.randint(3, 7)  # funcao entre um numero e outro
    realis = random.random()
    tempo = realis * 4


    def likecoment():
        time.sleep(1)
        pyautogui.moveTo(337, 864)  # ir para pesquisar
        pyautogui.click()
        time.sleep(tempo4)
        pyautogui.write('https://www.instagram.com/')
        pyautogui.hotkey('enter')
        time.sleep(5)
        botcard = pyautogui.locateOnScreen('card.png')
        pyautogui.click(botcard)
        #pyautogui.moveTo(723, 137)  # ir para pesquisarf
        #pyautogui.click()
        #pyautogui.write(f'{tagss}')
        time.sleep(tempo2)
        #pyautogui.hotkey('enter')
        #time.sleep(tempo2)
        #pyautogui.hotkey('enter')
        #time.sleep(tempo4)
        pyautogui.vscroll(-10)
        pyautogui.moveTo(400, 662)
        pyautogui.click()
        time.sleep(tempo2)

        luvas = random.randint(12, 19)

        for i in range(luvas):
            def inscrevasse():
                reali = random.random()
                tempo5 = reali * 3 + 1
                tempo6 = reali * 4 + 2
                tempo7 = reali * 4 + 4
                time.sleep(2)

                botsg = pyautogui.locateOnScreen('sgu.png')
                pyautogui.click(botsg)
                time.sleep(tempo5)
                botlike = pyautogui.locateOnScreen('like.png')
                pyautogui.click(botlike)
                time.sleep(tempo7)
                botcomentar = pyautogui.locateOnScreen('comentar.png')
                pyautogui.click(botcomentar)
                time.sleep(tempo6)

                comentar = ["Que Show!!", "Gostei! Muito Massa!", "Like!!", "uhu da hora a foto.",
                            "Muito Top!", "Espetacular! essa foto merece mil likes.",
                            "show! Essa foto merece varios likes.",
                            "Que massa! essa foto merece varios likes. rsrsrsrsr", "Caramba! Ta bem em?!",
                            "Like! Like! Like! muito bom", "extraordinario!", "Showww!"
                            "Isso aí! Show", "top tua postagem. isso ai!", "Muito, muito bom!","chaaama!",
                            "Very good!", "sensacional!", "Amazing!!!","Isso ai","Legal!!","Aqui que ta o sucesso!"]

                comentario = random.choice(comentar)
                pyautogui.write(f'{comentario}')
                time.sleep(tempo5)
                pyautogui.hotkey("enter")
                time.sleep(tempo6 + 2)
                pyautogui.hotkey("right")
                time.sleep(tempo5)

            inscrevasse()
            time.sleep(tempo2)


    likecoment()

    pyautogui.moveTo(27, 45)
    pyautogui.click()
    templong = tempolongo * 20 + 10
    time.sleep(templong)
