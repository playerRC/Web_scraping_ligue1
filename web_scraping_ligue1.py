import requests
import csv
from bs4 import BeautifulSoup
from lxml import etree

def Xpath(soup,path):
    documentObjectModel = etree.HTML(str(soup)) 
    return (documentObjectModel.xpath(path)[0].text)

def nbListes(soup):
    s = soup.find('div', class_='calendar-widget-container')
    s2 = s.find_all('ul')
    return len(s2)

def nbElementsDansChaqueListe(soup):
    l = []
    s = soup.find('div', class_='calendar-widget-container')
    s2 = s.find_all('ul')
    for ul in s2:
        s3 = ul.find_all('li')
        l.append(len(s3))
    return l
        
def homeTeam(soup):
    l = []
    for i in range(1, nbListes(soup)+1):
        for j in range(1, nbElementsDansChaqueListe(soup)[i-1]+1):
            l.append(Xpath(soup, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[1]/div/span[1]'))
    return l

def awayTeam(soup):
    l = []
    for i in range(1, nbListes(soup)+1):
        for j in range(1, nbElementsDansChaqueListe(soup)[i-1]+1):
            l.append(Xpath(soup, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[3]/div/span[1]'))
    return l

def homeGoal(soup):
    l = []
    for i in range(1, nbListes(soup)+1):
        for j in range(1, nbElementsDansChaqueListe(soup)[i-1]+1):
            HTG = Xpath(soup, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[2]/span/span[1]')
            if HTG == 'Reporté' or HTG == 'Annulé' or HTG == None:
                l.append(HTG)
            else:
                l.append(int(HTG))
    return l

def awayGoal(soup):
    l = []
    for i in range(1, nbListes(soup)+1):
        for j in range(1, nbElementsDansChaqueListe(soup)[i-1]+1):
            ATG = Xpath(soup, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[2]/span/span[3]')
            if ATG == None:
                l.append(ATG)
            else:
                l.append(int(ATG))
    return l

def rowWriting(fwriter, matchday, annee):
    url = f'https://www.ligue1.fr/calendrier-resultats?seasonId={annee}-{annee+1}&matchDay={matchday}'
    r = requests.get(url, Dict_Headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    for j in range(0,sum(nbElementsDansChaqueListe(soup))):
        if type(homeGoal(soup)[j]) != int:
            pass
        else:
            fwriter.writerow([f'{annee}-{annee+1}', i, homeTeam(soup)[j], awayTeam(soup)[j], homeGoal(soup)[j], awayGoal(soup)[j]])
            

header = ['Season','Matchday','HomeTeam', 'AwayTeam', 'HTG', 'ATG']
Dict_Headers = ({'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
        'Accept-Language': 'en-US, en;q=0.5'})

with open('all_ligue1_matches.csv', 'w', encoding='UTF-8', newline='') as f:
    fwriter = csv.writer(f)
    fwriter.writerow(header)
    for annee in range(1993, 2022):
        if annee == 2019:
            # annee covid seulement 28 journees terminees
            for i in range(1,29):
                rowWriting(fwriter, i, 2019)
        elif annee == 1997 or annee == 1998 or annee == 1999 or annee == 2000 or annee == 2001:
            # annees ligue 1 composee de 18 equipes donc 34 journees
            for i in range(1,35):
                rowWriting(fwriter, i, annee)
        elif annee == 2021:
            # annee actuel seulement 35 journees terminees le 8 mai 2022
            for i in range(1,36):
                rowWriting(fwriter, i, 2021)
        else:
            for i in range(1,39):
                rowWriting(fwriter, i, annee)
                    
