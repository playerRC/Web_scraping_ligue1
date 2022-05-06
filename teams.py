import requests
import XPath as xp
from bs4 import BeautifulSoup

def homeTeam(url):
    l = []
    for i in range(1, nbListes()+1):
        for j in range(1, nbElementsDansChaqueListe()[i-1]+1):
            l.append(xp.Xpath(url, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[1]/div/span[1]'))
    return l

def awayTeam(url):
    l = []
    for i in range(1, nbListes()+1):
        for j in range(1, nbElementsDansChaqueListe()[i-1]+1):
            l.append(xp.Xpath(url, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[3]/div/span[1]'))
    return l
