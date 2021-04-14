from datetime import datetime
import requests
from bs4 import BeautifulSoup


date = input("Hola, registra una fecha en formato 2021/abr/10: ")
#dt = datetime.strptime(date, '%Y/%m/%d')
#print('Registraste la fecha:', dt.year,'-',dt.month,'-',dt.day)
print('Registraste la fecha:', date)

#URL_ori='https://liturgiadelashoras.github.io/sync/2021/abr/11/laudes.htm'

url_base = 'https://liturgiadelashoras.github.io/sync/'
dict_oraciones = {
    'laudes': 'laudes',
    'visperas': 'visperas',
    'completas': 'completas',
    'oficio': 'oficio'
}

for oracion, name in dict_oraciones.items():
    url=url_base+date+'/'+oracion+'.htm'
    print('............\n')
    print('Accederemos al URL de',oracion,':',url)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find('div', id='cuerpo')

    print(body.decode_contents())
    input('Siguiente, dale enter:')
