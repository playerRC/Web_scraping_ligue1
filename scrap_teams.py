import requests
from bs4 import BeautifulSoup

# r = requests.get('https://www.ligue1.fr/calendrier-resultats')
r = requests.get('https://www.ligue1.fr/calendrier-resultats?seasonId=2021-2022&matchDay=6')
soup = BeautifulSoup(r.content, 'html.parser')

def Xpath(url,path):
    Dict_Headers = ({'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
        'Accept-Language': 'en-US, en;q=0.5'})
    # Gets the requried data https browser's address bar
    webPage = requests.get(url,Dict_Headers)
    # Creating a soup Object from the html content
    Scraping = BeautifulSoup(webPage.content, "html.parser") 
    # Conveting Soup object to etree object for Xpath processing
    documentObjectModel = etree.HTML(str(Scraping)) 
    return (documentObjectModel.xpath(path)[0].text)

#nb de ul dans le div
def nbListes():
    s = soup.find('div', class_='calendar-widget-container')
    s2 = s.find_all('ul')
    return len(s2)

def nbElementsDansChaqueListe():
    l = []
    for ul in s2:
        s3 = ul.find_all('li')
        l.append(len(s3))
        
def homeTeam():
    for i in range(1, len(s2)+1):
        for j in range(1, l[i-1]+1):
            print(Xpath('https://www.ligue1.fr/calendrier-resultats?seasonId=2021-2022&matchDay=6', f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[1]/div/span[1]'))

s = soup.find('div', class_='calendar-widget-container')
teams = s.find_all('div', class_ = 'club home')
team_name = s.find_all('span')

for team in team_name:
    print(team.text)
