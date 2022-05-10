import requests
from bs4 import BeautifulSoup

res = requests.get('https://peakedu.tistory.com/62')

#print(res.content)

soup = BeautifulSoup(res.content, "html.parser")

title = soup.find('title')

print(title.string)