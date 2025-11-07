import requests
from bs4 import BeautifulSoup
x = requests.get('https://riverdalehs.com')
soup = BeautifulSoup(x.text)
#print(soup.prettify())
newsTitles = soup.find_all(class_="fsTitle")
for title in newsTitles:
    print(title.get_text())
