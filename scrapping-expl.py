import requests
from bs4 import BeautifulSoup

url = 'http://example.webscraping.com/'

response = requests.get(url)
print(response)
if response.ok:
    print(response.headers)
    print(response.text)# voir le code html #

if response.ok:
    soup = BeautifulSoup(response.text,'lxml')
    title = soup.find('title')
    print(title)#avec balise html affiche title
    print(title.text)#sans balise html affiche title

if response.ok:
    links = [] #liste link <a></a>#
    soup = BeautifulSoup(response.text,'lxml')
    tds = soup.findAll('td')
    print(tds)#table
    print(len(tds))#logneur de cellules et 
    [print(str(td) +'\n\n') for td in tds]#exmple boucle for td  conv str#
    for td in tds:
        a = td.find('a')
        link = a['href']
        links.append('http://example.webscraping.com/'+link)#ajoute content a href dans le liste 
    print(links)