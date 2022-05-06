import requests
from bs4 import BeautifulSoup

# r = requests.get('https://www.ligue1.fr/calendrier-resultats')
r = requests.get('https://www.ligue1.fr/calendrier-resultats?seasonId=2021-2022&matchDay=6')
soup = BeautifulSoup(r.content, 'html.parser')

#nb de ul dans le div
def nbListes():
    s = soup.find('div', class_='calendar-widget-container')
    s2 = s.find_all('ul')
    return len(s2)

s = soup.find('div', class_='calendar-widget-container')
teams = s.find_all('div', class_ = 'club home')
team_name = s.find_all('span')

for team in team_name:
    print(team.text)
