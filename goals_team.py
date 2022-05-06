import requests
import XPath as xp
from bs4 import BeautifulSoup
import nbElementsUL as nbu.

def homeGoal(url):
  l = []
  for i in range(1, nbu.nbListes(url)+1):
    for j in range(1, nbu.nbElementsDansChaqueListe(url)[i-1]+1):
        if Xpath(url, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[2]/span/span[3]') == None:
              l.append(None)
        else:
              l.append(int(xp.Xpath(url, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[2]/span/span[1]')))
  return l


def awayGoal(url):
  l = []
  for i in range(1, nbu.nbListes(url)+1):
    for j in range(1, nbu.nbElementsDansChaqueListe(url)[i-1]+1):
      if Xpath(url, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[2]/span/span[3]') == None:
              l.append(None)
      else:
              l.append(int(xp.Xpath(url, f'/html/body/main/div[3]/div[2]/div/div[2]/ul[{i}]/li[{j}]/a/div[2]/span/span[3]')))
  return l
