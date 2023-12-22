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
    dict_input_oraciones = {
        'laudes': 'laudes',
        'visperas': 'visperas',
        'completas': 'completas',
        'oficio': 'oficio'
    }
    dict_info = {
        'url_base':url_base,
        'date_str':date_str
    }
    dict_salida  = get_dict_oraciones(dict_info, dict_input_oraciones)
    return dict_salida

def get_dict_oraciones(dict_info, dict_input_oraciones):
    """"
    Devuelve un diccionario de oraciones dependiendo del las oraciones en dict_input_oraciones.
    Diccionario helper: dict_info
    """
    #get variables
    url_base = dict_info.get('url_base')
    date_str = dict_info.get('date_str')
    dict_salida = {}
    for oracion, name in dict_input_oraciones.items():
        try:
            url=url_base+date_str+'/'+oracion+'.htm'
            #print('............\n')
            print('Accederemos al URL de',oracion,':',url)
            body_oracion = get_one_body_oracion(url,oracion)
        except:
            try:
                url=url_base+date_str+'/2/'+oracion+'.htm'
                #print('............\n')
                print('Accederemos al URL de',oracion,':',url)
                body_oracion = get_one_body_oracion(url,oracion)
            except Exception as e:
                print('No pude extraer el texto para la oracion',oracion, 'en', url)
                print('error:',e)
                body_oracion=''
        
        dict_salida[oracion]=body_oracion

    return dict_salida

def get_one_body_oracion(url,oracion):
    """
    Retorna el cuerpo de texto dada una url y un tipo de oracion
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find('div', id='cuerpo')
    body_oracion = str(body.decode_contents()).replace("#000000","")
    body_oracion = body_oracion.replace('CÁNTICO EVANGÉLICO<br/><br/>','CÁNTICO EVANGÉLICO<br/><br/></font>')
    if oracion=='oficio':
        #solo queremos la Segunda lectura del oficio
        lectio_post = body_oracion.split("SEGUNDA LECTURA",1)[1]
        lectio_seg_lect = lectio_post.split("RESPONSORIO",1)[0]
        body_oracion = lectio_seg_lect
    return body_oracion

#a = get_textos_liturgia('2023-12-21')
#print(a)