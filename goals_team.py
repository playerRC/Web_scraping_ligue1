

def homeGoal(url):
  l = []
  for i in range(1, nbListes()+1):
      for j in range(1, nbElementsDansChaqueListe()[i-1]+1):
          l.append(int(Xpath(url, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[2]/span/span[1]')))
  return l


def awayGoal(url):
  l = []
  for i in range(1, nbListes()+1):
      for j in range(1, nbElementsDansChaqueListe()[i-1]+1):
          l.append(int(Xpath(url, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[2]/span/span[3]')))
  return l
