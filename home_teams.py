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
        
def homeTeam(url):
    l = []
    for i in range(1, nbListes()+1):
        for j in range(1, nbElementsDansChaqueListe()[i-1]+1):
            l.append(xp.Xpath(url, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[1]/div/span[1]'))
    return l


