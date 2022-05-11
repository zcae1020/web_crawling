import requests
import urllib
from bs4 import BeautifulSoup

res = requests.get('https://peakedu.tistory.com/62')

#print(res.content)

soup = BeautifulSoup(res.content, "html.parser")

aset=soup.select('div.tt_article_useless_p_margin p > a')

for a in aset:
    r = requests.get(a.attrs["href"])
    s = BeautifulSoup(r.content, "html.parser")
    print(s.find('title'))