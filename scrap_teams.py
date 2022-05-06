import requests
from bs4 import BeautifulSoup

# r = requests.get('https://www.ligue1.fr/calendrier-resultats')
r = requests.get('https://www.ligue1.fr/calendrier-resultats?seasonId=2021-2022&matchDay=6')
soup = BeautifulSoup(r.content, 'html.parser')
