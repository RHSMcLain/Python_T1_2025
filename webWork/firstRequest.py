import requests, shelve
from bs4 import BeautifulSoup

x = requests.get('https://riverdalehs.com')
soup = BeautifulSoup(x.text)
#print(soup.prettify())
newsSection = soup.find(id="fsEl_3863")
newsTitles = newsSection.find_all(class_="fsTitle")
newNews = []
for title in newsTitles:
    print(title.get_text().strip())
    newNews.append(title.get_text().strip())
with shelve.open("newsFile") as f:
    if 'news' not in f:
        f['news'] = []
    oldNews = f['news']
    if (oldNews == newNews):
        print("No new news")
    else:
        print("That's new")
        f['news'] = newNews



