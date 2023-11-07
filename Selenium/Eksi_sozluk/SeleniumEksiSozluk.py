
from selenium import webdriver

import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = "https://eksisozluk1923.com/mustafa-kemal-ataturk--34712"

browser.get(url)

elements = browser.find_elements(By.CSS_SELECTOR, '.content') #CSS
#elements = browser.find_elements(By.XPATH, "//*[@id='entry-item']/div[1]") #Xpath


for element in elements:
    print("***************************************************")
    print(element.text)

browser.close()