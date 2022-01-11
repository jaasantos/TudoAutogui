import pyautogui
import time
#import random


time.sleep(3)

#botrec = pyautogui.locateOnScreen('recap.png')
#pyautogui.click(botrec)

#pyautogui.moveRel(100,100,0.6)   # mover o mouse da posicao atual até a posicao indicada no tempo especificado
#pyautogui.rightClick() #clicar com o botao direito
#pyautogui.mouseDown(700, 600, button ="left") # mantem pressionado o botao esquerdo na posicao indicada
#voce pode indicar aqui destino usando o moveTo
#pyautogui.write('ola como vc esta?? tudo bem?', 0.05) # digita na velocoidade dada

from requests_html import HTMLSession
from bs4 import BeautifulSoup

response = session.get('https://twitter.com/i/api/graphql/vamMfA41UoKXUmppa9PhSw/UserTweets?variables=%7B%22userId%22%3A%2215687962%22%2C%22count%22%3A20%2C%22cursor%22%3A%22HBaIgLLN%2BKGEryYAAA%3D%3D%22%2C%22withHighlightedLabel%22%3Atrue%2C%22withTweetQuoteCount%22%3Atrue%2C%22includePromotedContent%22%3Atrue%2C%22withTweetResult%22%3Afalse%2C%22withUserResults%22%3Afalse%2C%22withVoice%22%3Afalse%2C%22withNonLegacyCard%22%3Atrue%7D')
response.html.render()
s = BeautifulSoup(response.html.html, 'lxml')























