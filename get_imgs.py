from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(requests.get("https://szbi-pg.hu/index.php/hu/").content.decode(), features="lxml")
#print(soup)

GALLERY_I = 1

imgs = soup.findAll("div", class_="sigplus-gallery")[GALLERY_I].findAll("img")
urls = [x["src"] for x in imgs]
print("\n".join([f"<img src=\"https://szbi-pg.hu{x}\">" for x in urls]))
