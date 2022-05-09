import pandas as pd
import csv


def all_teams(df):
    l = []
    for team in df['HomeTeam']:
        if team not in l:
            l.append(team)
    return l

''' donne la liste de tous les indices où l'équipe donné en paramètre a joué à domicile ou à l'extérieur '''
def apparitionTeam(df, team):
    l=[]
    for i in range(0, len(df['Season'])):
        if df['HomeTeam'][i] == team or df['AwayTeam'][i] == team:
            l.append(i)
    return l

''' renvoie une liste dont chaque élément correspond au résultat de l'équipe sous forme [V,N,D] 
    V = victoire , N = match nul , D = défaite
    avec un deuxième élèment correspondant à [buts marqués, buts concédés]
'''
def team_result(df, team):
    m=[]
    for a in apparitionTeam(df, team):
        if (df['ATG'][a] > df['HTG'][a] and df['AwayTeam'][a] == team):
            l = [[1,0,0], [df['ATG'][a], df['HTG'][a]], df['Season'][a]]
        elif (df['ATG'][a] < df['HTG'][a] and df['HomeTeam'][a] == team):
            l = [[1,0,0], [df['HTG'][a], df['ATG'][a]], df['Season'][a]]
        elif (df['ATG'][a] < df['HTG'][a] and df['AwayTeam'][a] == team):
            l = [[0,0,1], [df['ATG'][a], df['HTG'][a]], df['Season'][a]]
        elif (df['ATG'][a] > df['HTG'][a] and df['HomeTeam'][a] == team):
            l = [[0,0,1], [df['HTG'][a], df['ATG'][a]], df['Season'][a]]
        else:
            if df['AwayTeam'][a] == team:
                l = [[0,1,0], [df['ATG'][a], df['HTG'][a]], df['Season'][a]]
            if df['HomeTeam'][a] == team:
                l = [[0,1,0], [df['HTG'][a], df['ATG'][a]], df['Season'][a]]
        m.append(l)
    return m

def nbWins(df, team):
    nb = 0
    for result in team_result(df, team):
        if result[0] == [1,0,0]:
            nb += 1
    return nb

def nbDraws(df, team):
    nb = 0
    for result in team_result(df, team):
        if result[0] == [0,1,0]:
            nb += 1
    return nb

def nbDefeats(df, team):
    nb = 0
    for result in team_result(df, team):
        if result[0] == [0,0,1]:
            nb += 1
    return nb

def nbPoints(df, team):
    pts = 0
    for s in range(0, len(team_result(df, team))):
        if team_result(df, team)[s][2] == '1993-1994':
            pts = 2 * nbWins(df, team) + nbDraws(df, team)
        else:
            pts = 3 * nbWins(df, team) + nbDraws(df, team)
    return pts

def nbGoalsFor(df, team):
    nb = 0
    for result in team_result(df, team):
        nb += result[1][0]
    return nb

def nbGoalsAgainst(df, team):
    nb = 0
    for result in team_result(df, team):
        nb += result[1][1]
    return nb

def goalAverage(df, team):
    return nbGoalsFor(df, team) - nbGoalsAgainst(df, team)

def all_stats(df):
    l = []
    for team in all_teams(df):
        m = []
        m.append(team)
        m.append(len(apparitionTeam(df, team)))
        m.append(nbWins(df, team))
        m.append(nbDraws(df, team))
        m.append(nbDefeats(df, team))
        m.append(nbGoalsFor(df, team))
        m.append(nbGoalsAgainst(df, team))
        m.append(goalAverage(df, team))
        m.append(nbPoints(df, team))
        l.append(m)
    l.sort(key=lambda row: (row[8], row[7], row[5], row[6]), reverse = True)
    return l

    
# Read CSV file into DataFrame df
df = pd.read_csv('all_ligue1_matches.csv')

header = ['Rank','Team','Games','Wins','Draws','Defeats','GF','GA','Diff','Points']
with open('historical_ranking.csv', 'w', encoding='UTF-8', newline='') as f:
    fwriter = csv.writer(f)
    fwriter.writerow(header)
    i = 1
    for stat in all_stats(df):
        fwriter.writerow([i, stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7], stat[8]])
        i += 1


