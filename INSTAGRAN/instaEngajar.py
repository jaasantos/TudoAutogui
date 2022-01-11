import time
import pyautogui
import random

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(executable_path=r"/Users/josealexsandroalmeidadossantos/PycharmProjects/TudoAutogui
# /TESTES/chromedriver")
# driver.get("https://www.google.com")
# "#ps4br", "#ps5br", "#playstationbr", "#sonybr" "#console", "#gamerbr", "#gamebr", "#xboxbr", "#xboxseriesxbr",
# "#videogamebr", "#play", "#primeirapessoa", "#ps3brasil"]

realtime = random.random()
tempo1 = realtime * 2 + 1
tempo2 = realtime * 4 + 3
tempo3 = realtime * 4 + 4
tempo4 = realtime * 4 + 5
tempolongo = random.random()
templong = tempolongo * 20 + 3
doloop = random.randint(2,3)          # vezes que o programa vai dar voltas       #linha 42
paracurtir = random.randint(40, 80)
vezesstory = random.randint(40, 80)    # define quantidade de loops para curtir os storyes   #linha 73
luvas = random.randint(15, 19)         # define quantas vezes o programa vai rodar em novos contatos  #
reali = random.random()
tempo5 = reali * 3 + 1
tempo6 = reali * 4 + 2
tempo7 = reali * 4 + 4
tempostore = tempolongo * 9 + 8

for i in range(doloop):   # ref linnha 33

    tag = ["#atitude", "#corrida", "#caminhar", "#estreladealagoas", "#emforma", "#fitnes", "#vidafitnes",
           "#aracaju", "#vaquejada", "#familia", "#nordeste",
           "#determinacao", "#festa", "#deusnocomando", "#resenha", "#viagem", "#fe", "#decoracao",
           "#garanhuns", "#pernambuco", "#vaquejada", "#brasil", "#running", "correr", "#deus", "#esperanca",
           "#correr", "#comedia", "#memebr", "#vida", "#atleta", "#filho"]

    tagss = random.choice(tag)       # funcao de busca aleatoria em uma lista
    realismo = random.randint(3, 7)  # funcao entre um numero e outro
    realis = random.random()
    tempo = realis * 4


    def likecoment():
        time.sleep(tempo2)
        pyautogui.moveTo(482, 864)  # ir para pesquisar
        pyautogui.click()
        time.sleep(tempo4)
        pyautogui.write('https://www.instagram.com/')
        pyautogui.hotkey('enter')
        pyautogui.moveTo(100, 500)
        pyautogui.click()
        time.sleep(tempo2)

        # para histories

        pyautogui.moveTo(625, 269)  # ir para histories
        pyautogui.click()
        time.sleep(tempo1)

        for isso in range(vezesstory):    # ref linha 35
            def curtirstory():
                time.sleep(tempostore)    # ref linha 40
                pyautogui.moveTo(604, 785)  # ir para pesquisar
                pyautogui.click()
                time.sleep(tempo1)
                pyautogui.moveTo(646, 726)  # ir para pesquisar
                pyautogui.click()
                time.sleep(tempo2)
                # botpalm = pyautogui.locateOnScreen('botpalm.png')
                # pyautogui.click(botpalm)

            curtirstory()

        pyautogui.moveTo(1403, 170)
        pyautogui.click()
        time.sleep(tempo3)

        # para curtir as fotos do feed

        for isso in range(paracurtir):
            pyautogui.moveTo(100, 500)
            pyautogui.vscroll(-18)
            time.sleep(tempo1)
            botlike = pyautogui.locateOnScreen('like.png')
            pyautogui.click(botlike)
            time.sleep(tempo1)

        time.sleep(5)
        pyautogui.moveTo(723, 160)  # ir para pesquisarf
        pyautogui.click()
        pyautogui.write(f'{tagss}')
        time.sleep(tempo2)
        pyautogui.hotkey('enter')
        time.sleep(tempo1)
        pyautogui.hotkey('enter')
        time.sleep(tempo4)
        pyautogui.moveTo(400, 662)
        pyautogui.click()
        time.sleep(tempo2)

    likecoment()

    pyautogui.moveTo(27, 45)
    pyautogui.click()
    templong = tempolongo * 10 + 10
    time.sleep(templong)
