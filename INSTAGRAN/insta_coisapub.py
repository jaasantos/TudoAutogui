'''

"#direitopublico", "#direitopúblico" #direitopublicomunicipal #direitoadministrativo #planejamentofinanceiro
#planejamentoestratégico #planejamentosemanal #planejamentoestrategico #planejamentoambiental #planejamentoestrategico
#gestaopublica #gestãopública #gestãopublica #gestaopública #direito #municipio #lei #escritorio #patrimonio#prefeito
#governo #governança

'''




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


tempolongo = random.random()
templong = tempolongo * 20 + 3
doloop = random.randint(3, 6)

for i in range(doloop):

    tag = ["#direitopublico", "#direitopratico", "#direitopublicomunicipal", "#direitoadministrativo",
           "#municipal", "#planoplurianual", "#planejamentosemanal", "#planejamentoestrategico",
           "#planejamentoambiental", "#planejamentoestrategico", "#gestaopublica", "#gestaopublica", "#servicopublico",
           "#gestaomunicipal", "#direito", "#municipio", "#prefeitura", "#escritorio", "#patrimonio", "#prefeito",
           "#governo", "#governanca", "contabilidade", "#contabilidadepublica"]

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
        pyautogui.moveTo(322, 864)  # ir para pesquisar
        pyautogui.click()
        time.sleep(tempo4)
        pyautogui.write('https://www.instagram.com/')

        pyautogui.hotkey('enter')
        time.sleep(5)
        pyautogui.moveTo(723, 137)  # ir para pesquisarf
        pyautogui.click()
        pyautogui.write(f'{tagss}')
        time.sleep(tempo2)
        pyautogui.hotkey('enter')
        time.sleep(tempo2)
        pyautogui.hotkey('enter')
        time.sleep(tempo4)
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

                time.sleep(tempo5)
                botlike = pyautogui.locateOnScreen('like.png')
                pyautogui.click(botlike)
                time.sleep(tempo7)
                botcomentar = pyautogui.locateOnScreen('comentar.png')
                pyautogui.click(botcomentar)
                time.sleep(tempo6)

                comentar = ["Que Show!!", "Gostei! Muito Massa!", "Like!!", "uhu da hora.",
                            "Muito Top!", "Espetacular! Merece mil likes.",
                            "Que massa! Merece varios likes", "Caramba! Ta bem em?!",
                            "Like! Like! Like! muito vlw", "extraordinario!", "Showww!",
                            "Isso aí! Show", "top tua postagem. isso ai!", "Muito, muito bom!",
                            "gostei!", "sensacional!", "Amazing!!!","Isso ai","Legal!!",
                            "Aqui que ta o sucesso!"]

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
