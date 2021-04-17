from datetime import datetime
import requests
from bs4 import BeautifulSoup



def get_textos_liturgia(date):
    #date = input("Hola, registra una fecha en formato 2021/abr/10: ")
    dt = datetime.strptime(date, '%Y-%m-%d')
    #print('Registraste la fecha:', dt.year,'-',dt.month,'-',dt.day)
    meses = {
        '1':'ene',
        '2':'feb',
        '3':'mar',
        '4':'abr',
        '5':'may',
        '6':'jun',
        '7':'jul',
        '8':'ago',
        '9':'sep',
        '10':'oct',
        '11':'nov',
        '12':'dic',
    }
    date_str = str(dt.year)+'/'+meses[str(dt.month)]+'/'+str(dt.day)

    #URL_ori='https://liturgiadelashoras.github.io/sync/2021/abr/11/laudes.htm'
    url_base = 'https://liturgiadelashoras.github.io/sync/'
    dict_oraciones = {
        'laudes': 'laudes',
        'visperas': 'visperas',
        'completas': 'completas',
        'oficio': 'oficio'
    }
    dict_salida = {}
    for oracion, name in dict_oraciones.items():
        url=url_base+date_str+'/'+oracion+'.htm'
        print('............\n')
        print('Accederemos al URL de',oracion,':',url)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        body = soup.find('div', id='cuerpo')

        dict_salida[oracion]=str(body.decode_contents())
        print(body.decode_contents())
        #input('Siguiente, dale enter:')
    return dict_salida
