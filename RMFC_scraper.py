import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.rmfclassic.pl/radio/repertuar')
soup = bs.BeautifulSoup(source,'lxml')

listaart =[]
listautw = []
for name in soup.find_all('div', {'class':'artist-name cfn'}):    
   listaart.append(name.text)


for song in soup.find_all('div', {'class': 'song-title'}):
   listautw.append(song.text)


for artysta, utwor in zip(listaart, listautw):
   print(artysta, ' - ', utwor)

