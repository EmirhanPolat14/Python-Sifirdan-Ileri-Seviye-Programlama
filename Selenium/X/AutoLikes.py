from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def scroll_and_wait(driver, scroll_times=3):
    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="like"]')))



browser = webdriver.Chrome()
browser.get("https://twitter.com/?lang=tr")
time.sleep(3)

giris_yap = browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div")
giris_yap.click()
time.sleep(3)

email = browser.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
email.send_keys("Eposta")
time.sleep(2)

ileri = browser.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
ileri.click()
time.sleep(3)

#Olağandışı haraket
username = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
username.send_keys("Kullanıcıadı")
time.sleep(4)
ileri2 = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
ileri2.click()
time.sleep(3)

password = browser.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys("Şifre")
time.sleep(2)

onayla = browser.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
onayla.click()
time.sleep(5)

searchArea = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]')
searchArea.click()
time.sleep(5)

searchInput = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
searchInput.send_keys("#yazilimayolver")
time.sleep(5)

#Enter tuşu
browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input').send_keys(Keys.ENTER)
time.sleep(5)





wait = WebDriverWait(browser, 30)
scroll_and_wait(browser, scroll_times=3)

like_buttons = browser.find_elements(By.CSS_SELECTOR, 'div[data-testid="like"]')
for like in like_buttons:
    try:
        like.click()
    except:
        pass

browser.close()