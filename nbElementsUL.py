import requests
import XPath as xp
from bs4 import BeautifulSoup

#nb de ul dans le div
def nbListes():
    s = soup.find('div', class_='calendar-widget-container')
    s2 = s.find_all('ul')
    return len(s2)

def nbElementsDansChaqueListe():
    l = []
    s = soup.find('div', class_='calendar-widget-container')
    s2 = s.find_all('ul')
    for ul in s2:
        s3 = ul.find_all('li')
        l.append(len(s3))
    return l
