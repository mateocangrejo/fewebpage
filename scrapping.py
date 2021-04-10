from datetime import datetime
import requests
from bs4 import BeautifulSoup

date = input("Hola feis, registra una fecha como 2021-04-10: ")
#print(name, type(name))

#date = '2021-04-11'
dt = datetime.strptime(date, '%Y-%m-%d')
print(dt.year,dt.month,dt.day)

URL_ori = 'http://fraynelson.com/blog/2021/04/10/laudes-2021-04-11/'
input_url = str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day-1)
print(input_url)
context_url = 'laudes'
URL = 'http://fraynelson.com/blog/'+input_url+'/'+context_url+'-'+date+'/'
print(URL)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#print('todo correcto hasta aca')

#results = soup.find(id='ResultsContainer')
title_elem = soup.find('h1', class_='title entry-title')
body = soup.find('div', class_='nv-content-wrap entry-content')

description = body.find_all('p')
audio = body.find('a', class_='powerpress_link_d',href=True, title='Download')

print(title_elem.text)
print(len(description[0]))
print(description[0].text)
print(len(audio['href']),audio['href'])
#print(title_elems.prettify())
