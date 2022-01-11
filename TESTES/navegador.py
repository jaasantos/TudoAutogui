from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r"/Users/josealexsandroalmeidadossantos/PycharmProjects/TudoAutogui/TESTES/chromedriver")
driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys('CRiar boot')
driver.find_element_by_name("q").send_keys(Keys.RETURN)
