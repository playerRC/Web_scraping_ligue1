import pandas as pd
import csv

# fct permettant de connaître les équipes ayant participer au moins une fois à la première division française
def all_teams(df):
    l = []
    for team in df['HomeTeam']:
        if team not in l:
            l.append(team)
    return l

''' fct permettant de connaître les résultats d'une équipe donnée sous forme de liste de liste dont chaque élément s'écrit comme suit
    [ R , [GF, GA], Season] avec R = V ou N ou D
    et GF = buts marqués , GA = buts encaissés
'''
def team_result(df, team):
    app = []
    # d'abord on stocke les indices où l'équipe joue un match
    for i in range(0, len(df['Season'])):
        if df['HomeTeam'][i] == team or df['AwayTeam'][i] == team:
            app.append(i)
    m = []
    for a in app:
        if (df['ATG'][a] > df['HTG'][a] and df['AwayTeam'][a] == team):
            l = ['V', [df['ATG'][a], df['HTG'][a]], df['Season'][a]]
        elif (df['ATG'][a] < df['HTG'][a] and df['HomeTeam'][a] == team):
            l = ['V', [df['HTG'][a], df['ATG'][a]], df['Season'][a]]
        elif (df['ATG'][a] < df['HTG'][a] and df['AwayTeam'][a] == team):
            l = ['D', [df['ATG'][a], df['HTG'][a]], df['Season'][a]]
        elif (df['ATG'][a] > df['HTG'][a] and df['HomeTeam'][a] == team):
            l = ['D', [df['HTG'][a], df['ATG'][a]], df['Season'][a]]
        else:
            if df['AwayTeam'][a] == team:
                l = ['N', [df['ATG'][a], df['HTG'][a]], df['Season'][a]]
            if df['HomeTeam'][a] == team:
                l = ['N', [df['HTG'][a], df['ATG'][a]], df['Season'][a]]
        m.append(l)
    return m

''' fct qui renvoie une liste contenant les statistiques d'une équipe donnée '''
def stats(df, team):
    nbWins = 0
    nbDraws = 0
    nbL = 0
    GF = 0
    GA = 0
    pts = 0
    for result in team_result(df, team):
        if result[0] == 'V':
            nbWins += 1
            # jusqu'à la saison 1993-1994, une victoire rapportait 2 points
            if result[2] == '1993-1994':
                pts += 2
            else:
                pts += 3
        if result[0] == 'N':
            nbDraws += 1
            pts += 1
        if result[0] == 'D':
            nbL += 1
        GF += result[1][0]
        GA += result[1][1]
    
    diff = GF-GA
    return [nbWins, nbDraws, nbL, GF, GA, diff, pts]

def all_stats(df):
    l = []
    for team in all_teams(df):
        m = []
        m.append(team)
        m.append(len(team_result(df,team)))
        m.append(stats(df, team)[0])
        m.append(stats(df, team)[1])
        m.append(stats(df, team)[2])
        m.append(stats(df, team)[3])
        m.append(stats(df, team)[4])
        m.append(stats(df, team)[5])
        m.append(stats(df, team)[6])
        l.append(m)
    l.sort(key=lambda row: (row[8], row[7], row[5], row[6]), reverse = True)
    return l

    
# lecture du fichier CSV --> DataFrame df
df = pd.read_csv('all_ligue1_matches.csv')

header = ['Rank','Team','Games','Wins','Draws','Defeats','GF','GA','Diff','Points']
with open('historical_ranking.csv', 'w', encoding='UTF-8', newline='') as f:
    fwriter = csv.writer(f)
    fwriter.writerow(header)
    i = 1
    for stat in all_stats(df):
        fwriter.writerow([i, stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7], stat[8]])
        i += 1
