import time
import pyautogui
import random


realtime = random.random()
tempo1 = realtime * 2 + 1     # tempo de execução do processo ficou entre 1 e 2
tempo2 = realtime * 4 + 3     # tempo de execução do processo ficou entre 3 e 6
tempo3 = realtime * 4 + 4     # tempo de execução do processo ficou entre 4 e 7
tempo4 = realtime * 4 + 5     # tempo de execução do processo ficou entre 5 e 8
templong = realtime * 20 + 3  # tempo de execução do processo ficou entre 3 e 22


doloop = random.randint(4, 6)       # vezes que o programa vai dar voltas > linha 42
paracurtir = random.randint(5, 10)  # vezes rodar em curtir
vezesstory = random.randint(30, 50)  # define quantidade de loops para curtir os storyes   #linha 73
luvas = random.randint(4, 10)       # define quantas vezes o programa vai rodar em novos contatos


for i in range(doloop):  # vezes que o programa vai rodar

    tag = ["batalha, Alagoas,", "estrela de alagoas, alagoas, brasil, estr", "igreja nova, alagoas, br",
           "jaramataia, alagoas, br, ja", "olha agua das flores, ala", "canapi, alagoas, bra",
           "Major Isidoro, alagoas", "#vaquejada", "sao jose da tapera, alagoas, br", "Garanhuns, pernambuco",
           "#determinacao", "Paulo Jacinto, Alagoas, b", "mata grande, alagoas, br", "campo alegre, alagoas, br",
           "#garanhuns", "#pernambuco", "dois riachos, alagoas,", "quebrangulo, alagoas", "arapiraca, alagoas",
           "#deus", "santana do ipanema, alagoas", "aguas belas, perna", "sao Miguel dos campos, alagoas, b",
           "Iati, pe, br", "viçosa, ala", "jacaré dos homens, alagoas, brasil", "#filho", "igaci, alagoas",
           "Bom Conselho, per", "Maceió, aceió, m", "maribondo, alagoas, brasil, mari", "atalaia, alagoas, brasil, ata",
           "sao Sebastião, alagoas, brasil, sao sebast", "Minador do negrão, ala", "major Izidoro, alagoas, brasil, ma"]

    tag2 = ["#pythondeveloper", "#datastructure", "#appdeveloper", "#javaprogramming", "#developerlife",
            "#programminglanguage", "#pythonprogramming", "#programmers", "#coder", "#programmingisfurn", "#html",
            "#css", "#developer", "#javascript", "#programmer", "#coding", "#coder", "#coderlife", "#developerlife",
            "#codinglife", "#computerscience", "#codelife", "#code", "#science", "#softwaredevelopment", "#frontend"]

    tagss = random.choice(tag2)  # funcao de busca aleatoria em uma lista
    realismo = random.randint(3, 7)  # funcao entre um número e outro
    realis = random.random()
    tempo = realis * 4


    def likecoment():
        import webbrowser
        webbrowser.open('https://www.instagram.com')
        time.sleep(tempo2)
        pyautogui.moveTo(100, 500)
        pyautogui.click()  # EM FORMA
        time.sleep(tempo4)

        # para curtir histories #####################################################################################

        pyautogui.moveTo(625, 269)  # ir para histories
        pyautogui.click()
        time.sleep(tempo1)

        for isso in range(vezesstory):  # ref linha 35
            def curtirstory():
                time.sleep(tempo2)
                pyautogui.moveTo(604, 785)  # ir para pesquisar
                pyautogui.click()
                time.sleep(tempo1)
                pyautogui.moveTo(646, 726)  # ir para pesquisar
                pyautogui.click()
                time.sleep(tempo2)
                pyautogui.moveTo(936, 486)  # passar a publicacao
                pyautogui.click()
                time.sleep(tempo2)
                pyautogui.click()
                # botpalm = pyautogui.locateOnScreen('botpalm.png')
                # pyautogui.click(botpalm)

            curtirstory()

        pyautogui.moveTo(1403, 170)
        pyautogui.click()
        time.sleep(tempo1)

        # para curtir as fotos do feed  #############################################################################

        for isso in range(paracurtir):
            pyautogui.moveTo(100, 500)
            pyautogui.click()
            pyautogui.vscroll(-18)
            time.sleep(tempo1)
            botlike = pyautogui.locateOnScreen('imagens/like.png')
            pyautogui.click(botlike)
            time.sleep(tempo1)

        # Para novos contatos ########################################################################################

        time.sleep(tempo2)
        pyautogui.moveTo(723, 160)  # ir para pesquisarf
        pyautogui.click()
        pyautogui.write(f'{tagss}')
        time.sleep(tempo2)
        pyautogui.hotkey('enter')
        time.sleep(tempo1)
        pyautogui.hotkey('enter')
        time.sleep(tempo1)
        pyautogui.moveTo(400, 700)
        pyautogui.click()
        time.sleep(tempo2)

        for isso in range(luvas):         # pyautogui.hotkey('enter')
            def inscrevase():
                tempo5 = realtime * 3 + 1
                botaolike = pyautogui.locateOnScreen('imagens/like.png')
                pyautogui.click(botaolike)
                time.sleep(tempo1)
                botcomentar = pyautogui.locateOnScreen('imagens/comentar.png')
                pyautogui.click(botcomentar)
                time.sleep(tempo1)

                comentar = ["bom!!", "Muito bom!", "Like!!", "Da hora!",
                            "Muito Top!", "Espetacular! Merece mil likes.",
                            "show! Merece varios likes.", "legal!",
                            "Que massa! Merece varios likes!", "Caramba!",
                            "Like! Like! Like!", "muito massa", "extraordinario!", "Shoowww!", "Parabens",
                            "top tua postagem!", "Muito, muito bom!", "chaaama!", " Ta bem!",
                            "show!", "sensacional!", "é isso!!", "Top!", "Legal!!", "Sucesso!"]

                comentario = random.choice(comentar)
                pyautogui.write(f'{comentario}', interval=0.05)
                time.sleep(tempo5)
                pyautogui.hotkey("enter")
                time.sleep(tempo4 + 2)
                pyautogui.hotkey("right")
                time.sleep(tempo4)

            inscrevase()
            time.sleep(tempo1)


    likecoment()

    pyautogui.moveTo(27, 45)
    pyautogui.click()
    templong = tempo4
    time.sleep(templong)
