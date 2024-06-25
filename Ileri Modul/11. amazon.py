import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com.tr/gp/bestsellers/computers/12601898031?ref_=Oct_d_obs_S&pd_rd_w=o6rTN&content-id=amzn1.sym.54027afa-4e84-447f-ac8b-0d69d179421f&pf_rd_p=54027afa-4e84-447f-ac8b-0d69d179421f&pf_rd_r=XSYJNBP20Z6E38C39YP5&pd_rd_wg=jd9Fs&pd_rd_r=4800ce1a-d118-4a78-ad8e-66edaa7e2f7e"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

html = requests.get(url=url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find_all("div", {"id":"gridItemRoot"}, limit=10)

count=1
for item in liste:
    link = "https://www.amazon.com.tr/"+ item.a.get("href")
    p_name = item.find("div", {"class":"_cDEzb_p13n-sc-css-line-clamp-3_g3dy1"}).text
    image = item.img.get("src")
    price = item.find("span", {"class":"_cDEzb_p13n-sc-price_3mJ9Z"}).text
    star = item.find("span", {"class":"a-icon-alt"}).text
    rating_count = item.find("span", {"class":"a-size-small"}).text
    
    print(f"{count}.{p_name} \n\türün linki:{link}\n\türün resmi:{image}\n\türün fiyatı:{price}\n\türün puanı:{star}\n\türün dğerlendirme sayısı:{rating_count}")

    count += 1

    
