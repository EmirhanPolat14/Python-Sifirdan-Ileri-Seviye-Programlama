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
time.sleep(10)

#profile girme
profileButton = browser.find_element(By.CSS_SELECTOR, f'a[href="/{LogınInfo.username}/?next=%2F"]')
profileButton.click()
time.sleep(5)

#takip edilenlerin bulunduğu li elementini seçme ve tıklama
buttons = browser.find_elements(By.CSS_SELECTOR, '.xl565be.x1m39q7l.x1uw6ca5.x2pgyrj')
followsButton = buttons[2]
followsButton.click()
time.sleep(5)

#js ile scroll
js_command = """
follows = document.querySelector("._aano");
follows.scrollTo(0, follows.scrollHeight);
var lenOfPage = follows.scrollHeight;
return lenOfPage;
"""
lenOfPage = browser.execute_script(js_command)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(js_command)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

#takip edilebler listesini dosyaya yazdırma
liste = list()
follows = browser.find_elements(By.CSS_SELECTOR, '._ap3a._aaco._aacw._aacx._aad7._aade')
for follow in follows:
    liste.append(follow)

with open("takipEdilen.txt", "w", encoding="UTF-8") as file:
    for i in liste:
        file.write(i.text + "\n")



browser.close()
