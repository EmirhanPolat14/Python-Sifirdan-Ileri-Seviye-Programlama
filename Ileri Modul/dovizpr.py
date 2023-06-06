import requests
from bs4 import BeautifulSoup
url = "https://www.doviz.com/"
respone = requests.get(url)
doviz = respone.content
icerik = BeautifulSoup(doviz,"html.parser")

for i,j in zip(icerik.find_all("span",{"class":"name"}),icerik.find_all("span",{"class":"value"})):
    print("{} = {}".format(i.text,j.text))