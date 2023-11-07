from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random

browser = webdriver.Chrome()
url = "https://eksisozluk1923.com/mustafa-kemal-ataturk--34712?p="

entries = []
pageCount = 1
while pageCount <= 10:
    randomPage = random.randint(1, 2780)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements = browser.find_elements(By.CSS_SELECTOR, '.content')
    time.sleep(2)
    for element in elements:
        entries.append(element.text)
    pageCount += 1

with open("entries.txt", "w", encoding="UTF-8") as file:
    pageCount = 1
    for entry in entries:
        file.write(f"{str(pageCount)}.\n{entry}\n")
        file.write("************************************************\n")
        pageCount += 1

browser.close()
