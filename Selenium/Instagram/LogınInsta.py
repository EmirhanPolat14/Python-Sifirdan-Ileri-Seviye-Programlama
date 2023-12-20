import LogınInfo
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Driver'ı ekleme ve belirtilen url'e gönderme
browser = webdriver.Chrome()
url = "https://www.instagram.com/"
browser.get(url)
time.sleep(2)

#Kullanıcı adı ve şifre bölümlerini Xpasth olarak alma
usernameArea = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
passwordArea = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

#Loginınfo'daki kullanıcı bilgilerimizi alanlara gönderme
usernameArea.send_keys(LogınInfo.username)
passwordArea.send_keys(LogınInfo.password)

#giriş butonu tıklama
girisYap = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
girisYap.click()
time.sleep(20)

browser.close()


