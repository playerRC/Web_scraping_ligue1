# Web scraping Ligue 1

Dans le cadre de mon cursus universitaire, j'ai réalisé un projet permettant de récuperer les données de tous les matchs de ligue 1 depuis la saison 1993-1994.

# Installation

Pour pouvoir utiliser mon projet, il vous suffit de télecharger tout le répertoire ou de cloner le répertoire avec la commande suivante:
 * <code>git clone https://github.com/playerRC/Web_scraping_ligue1.git</code>

# Utilisation et résultats

En exécutant le fichier web_scraping_ligue1.py pendant quelques heures, vous obtiendrez le fichier all_ligue1_matches.csv contenant les résultats de toutes les confrontations jusqu'à la 35ème journée incluse de la saison 2021-2022.

La deuxième partie du projet consiste à établir un classement général des clubs français triés suivant les statistiques suivantes :
  * 'Points' : nombre de points gagnés au total
  * 'Diff' : différence entre le nb total de buts marqués et le nb total de buts encaissés
  * 'GF' : nb total de buts marqués
  * 'GA' : nb total de buts encaissés

Pour obtenir ce résultat, il suffit d'éxecuter le fichier ranking.py et vous obtiendrez le résultat final dans le fichier historical_ranking.csv

# Site scrapé

* https://www.ligue1.fr/calendrier-resultats
