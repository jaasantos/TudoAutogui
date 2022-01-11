from selenium import webdriver
from selenium.webdriver.common.keys import Keys


navegador = webdriver.Chrome(executable_path=r"/Users/josealexsandroalmeidadossantos/Downloads/chromedriver")
navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element_by_xpath('//*[@id="banner"]/a[1]/img').click()
navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/img').click()
navegador.find_element_by_xpath('//*[@id="4zS989en0CKjhpbeCLPGMw=="]').click()

#find
#navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/p').click()

#print('sucesso')
#driver.find_element_by_name("q").send_keys('CRiar boot')
#driver.find_element_by_name("principal").send_keys(Keys.RETURN)