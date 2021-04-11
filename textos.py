from datetime import datetime
import requests
from bs4 import BeautifulSoup



url='https://liturgiadelashoras.github.io/sync/2021/abr/11/laudes.htm'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
body = soup.find('div', id='cuerpo')

print(body.text)
