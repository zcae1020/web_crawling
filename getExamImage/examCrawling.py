import requests
from urllib.request import urlopen
import os
from bs4 import BeautifulSoup

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

res = requests.get('https://peakedu.tistory.com/62')

#print(res.content)

soup = BeautifulSoup(res.content, "html.parser")

aset=soup.select('div.tt_article_useless_p_margin > p > a')

for a in aset:
    r = requests.get(a.attrs["href"])
    s = BeautifulSoup(r.content, "html.parser")
    #print(s.select('title'))
    title = s.select_one('title')
    createFolder('./img/'+ title.text)
    imgset = s.select('figure.imageblock span > img'); 
    n = 1
    for img in imgset:
        imgUrl = img['src'] 
        with urlopen(imgUrl) as f:
            with open('./img/' + title.text + '/' + title.text + str(n) +'.jpg','wb') as h:
                img = f.read()
                h.write(img)
        n += 1
    print('다운로드 완료')
