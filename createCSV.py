import csv
import nbElementsUL as nbu
import goals_team as gt
import teams as t
import requests
from bs4 import BeautifulSoup

header = ['Season','Matchday','HomeTeam', 'AwayTeam', 'HTG', 'ATG']
with open('all_ligue1_matches.csv', 'w', encoding='UTF8', newline='') as f:
    fwriter = csv.writer(f)
    fwriter.writerow(header)
    for annee in range(1993, 2022):
        if annee == 2019:
            # annee covid seulement 28 journees terminees
            for i in range(1,29):
                url = f'https://www.ligue1.fr/calendrier-resultats?seasonId=2019-2020&matchDay={i}'
                for j in range(0,sum(nbu.nbElementsDansChaqueListe(url))):
                    fwriter.writerow(['2019-2020', i, t.homeTeam(url)[j], t.awayTeam(url)[j], gt.homeGoal(url)[j], gt.awayGoal(url)[j]])
        elif annee == 1997 or annee == 1998 or annee == 1999 or annee == 2000 or annee == 2001:
            # annees ligue 1 composee de 18 equipes donc 34 journees
            for i in range(1,35):
                url = f'https://www.ligue1.fr/calendrier-resultats?seasonId={annee}-{annee+1}&matchDay={i}'
                for j in range(0,sum(nbu.nbElementsDansChaqueListe(url))):
                    fwriter.writerow([f'{annee}-{annee+1}', i, t.homeTeam(url)[j], t.awayTeam(url)[j], gt.homeGoal(url)[j], gt.awayGoal(url)[j]])
        elif annee == 2021:
            # annee actuel seulement 35 journees terminees le 7 mai 2022
            for i in range(1,36):
                url = f'https://www.ligue1.fr/calendrier-resultats?seasonId=2021-2022&matchDay={i}'
                for j in range(0,sum(nbu.nbElementsDansChaqueListe(url))):
                    fwriter.writerow(['2021-2022', i, t.homeTeam(url)[j], t.awayTeam(url)[j], gt.homeGoal(url)[j], gt.awayGoal(url)[j]])
        else:
            for i in range(1,39):
                url = f'https://www.ligue1.fr/calendrier-resultats?seasonId={annee}-{annee+1}&matchDay={i}'
                for j in range(0,sum(nbu.nbElementsDansChaqueListe(url))):
                    fwriter.writerow([f'{annee}-{annee+1}', i, t.homeTeam(url)[j], t.awayTeam(url)[j], gt.homeGoal(url)[j], gt.awayGoal(url)[j]])
