with open('matchs.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Journée','HomeTeam', 'AwayTeam', 'HG', 'AG'])
    for i in range(1,39):
        for j in range(0,10):
            url = f'https://www.ligue1.fr/calendrier-resultats?seasonId=2020-2021&matchDay={i}'
            filewriter.writerow([i, homeTeam(url)[j], awayTeam(url)[j], homeGoal(url)[j], awayGoal(url)[j]])
