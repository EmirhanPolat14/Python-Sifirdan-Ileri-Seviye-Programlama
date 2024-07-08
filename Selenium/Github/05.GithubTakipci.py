from GithubUserinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def SignIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()
    
    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")
        time.sleep(2)
        try:
            for i in items:
                self.followers.append(i.find_element(By.CSS_SELECTOR, ".Link--secondary").text)
        except Exception as e:
            print(e)
        
        time.sleep(2)
    
    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}")
        time.sleep(2)

        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/a[1]").click()
        time.sleep(2)

        self.loadFollowers()
        a = 0
        while a <= 10:
            links = self.browser.find_element(By.CLASS_NAME, "pagination").find_elements(By.TAG_NAME, "a")
            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(2)
                    self.loadFollowers()
                    a += 1
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        self.loadFollowers()
                        a += 1
                    else:
                        pass
               
github = Github(username, password)
github.SignIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)
