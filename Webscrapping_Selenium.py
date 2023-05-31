from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
import time

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("https://www.kaskus.co.id/channel/5/news")

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(15):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

html = driver.page_source
soup = BeautifulSoup (html, 'html.parser')
toko = soup.find_all("div","P(15px) Bd(borderSolidLightGrey) Mb(15px) Bgc(c-white) Pos(r) Ov(h) jsThreadCard")


nama = []
isi = []

for t in toko:
    topik = t.find("div", "Ov(h) Tov(e) Whs(nw) Fz(14px)").get_text()
    berita = t.find("div", "Fw(500) Fz(18px) Mb(10px)").get_text()
    berita = berita.strip("\n ")
    nama.append(topik)
    isi.append(berita)
    
informasi = {'topik':nama,'berita':isi}
df = pandas.DataFrame(informasi, columns = ['topik','berita'])
df.sort_values('topik',axis = 0, ascending=True, inplace = True)   
df.to_csv("kaskus.csv",sep=',')

df.head()
