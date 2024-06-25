import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"  
        self.headers = {"Authorization": self.token}
    
    def getUser(self, username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()
    
    def getRepostories(self,username):
        response = requests.get(self.api_url + "/users/" + username + "/repos")
        return response.json()
    
    def createRepo(self,name):
        url = f"{self.api_url}/user/repos"
        headers = {
            "Authorization": f"token {self.token}"
        }
        payload = {
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
github = Github()

while True:
    secim = input("1- Find user\n2- Get Repostories\n3- Create Repostory\n4- Exit\nSecim: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            username = input("Username: ")
            result= github.getUser(username)
            print(f"name:{result['name']}\npublic repos: {result['public_repos']}\nfollower: {result['followers']}")
        elif secim == "2":
            username = input("Username: ")
            result = github.getRepostories(username)
            a = 1
            for i in result:
                print(f"{a}. repo: {i['name']}")
                a += 1
        elif secim == "3":
            name = input("Repo name? ")
            result = github.createRepo(name)
            print(result)
        else:
            print("Yanlış bir seçim yaptınız.")
 