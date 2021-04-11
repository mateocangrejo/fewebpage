from datetime import datetime
import requests
from bs4 import BeautifulSoup

url_base = 'https://www.ciudadredonda.org/calendario-lecturas/evangelio-del-dia/?f='
#url='https://www.ciudadredonda.org/calendario-lecturas/evangelio-del-dia/?f=2021-04-11'
date = '2021-04-12'

url=url_base+date
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('h1', class_='ar_titulo')
subtitulo = soup.find('div', class_='subtitulo')
body = soup.find('div', class_='lecturas')
lecturas = body.find_all('section')
print(title.text)
print(subtitulo.text)

for lect in lecturas:
    name = lect.find('h2')
    texto = lect.find('div', class_='texto_palabra').decode_contents()
    print(name)
    print(texto)
