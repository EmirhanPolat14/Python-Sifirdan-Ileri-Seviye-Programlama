from selenium import webdriver

import time

from selenium.webdriver.common.by import By

import random

browser = webdriver.Chrome()

url =
"https://eksisozluk1923.com/mustafa-kemal-ataturk--34712?p="
entries = []
entryCount = 1
pageCount = 1
while pageCount <=10:
    randomPage = random.randint(1,2780)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements = browser.find_elements(By.CSS_SELECTOR, '.content')
    time.sleep(3)
    for element in elements:
        entries.append(element.text)
    pageCount += 1

for entry in entries:
    print(str(entryCount) + "************************************************************************")
    print(entry)
    entryCount += 1
browser.close()