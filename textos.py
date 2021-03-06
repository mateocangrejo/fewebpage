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
    date_str = str(dt.year)+'/'+meses[str(dt.month)]+'/'+str(dt.strftime('%d'))

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
        try:
            url=url_base+date_str+'/'+oracion+'.htm'
            #print('............\n')
            print('Accederemos al URL de',oracion,':',url)

            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            body = soup.find('div', id='cuerpo')

            dict_salida[oracion]=str(body.decode_contents()).replace("#000000","")
            dict_salida[oracion]=dict_salida[oracion].replace('CÁNTICO EVANGÉLICO<br/><br/>','CÁNTICO EVANGÉLICO<br/><br/></font>')
        except:
            url=url_base+date_str+'/2/'+oracion+'.htm'
            #print('............\n')
            print('Accederemos al URL de',oracion,':',url)

            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            body = soup.find('div', id='cuerpo')

            dict_salida[oracion]=str(body.decode_contents()).replace("#000000","")
            dict_salida[oracion]=dict_salida[oracion].replace('CÁNTICO EVANGÉLICO<br/><br/>','CÁNTICO EVANGÉLICO<br/><br/></font>')

        #print(body.decode_contents())
        #input('Siguiente, dale enter:')
    oficio_text = dict_salida['oficio']
    lectio_post = oficio_text.split("SEGUNDA LECTURA",1)[1]
    lectio_seg_lect = lectio_post.split("RESPONSORIO",1)[0]
    dict_salida['oficio']=lectio_seg_lect
    return dict_salida
#a = get_textos_liturgia('2021-05-16')
