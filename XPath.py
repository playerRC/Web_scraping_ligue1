import requests
from bs4 import BeautifulSoup


# r = requests.get('https://www.ligue1.fr/calendrier-resultats')

'''
url = 'https://www.ligue1.fr/calendrier-resultats?seasonId=2021-2022&matchDay=6'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
'''

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
