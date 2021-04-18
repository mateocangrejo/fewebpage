from datetime import datetime
import requests
from bs4 import BeautifulSoup

#Data Fecha

def get_oraciones_liturgia(date):
    dt = datetime.strptime(date, '%Y-%m-%d')
    #print('Registraste la fecha:', dt.year,'-',dt.month,'-',dt.day)

    #urls_inputs
    #URL_ori_laudes = 'http://fraynelson.com/blog/2021/04/10/laudes-2021-04-11/'
    #URL_ori_visperas = 'https://fraynelson.com/blog/2021/04/10/visperas-2021-04-10/'
    #URL_ori_completas = 'https://fraynelson.com/blog/2021/04/10/completas-20210410/'
    #URL_ori_lectio = 'http://fraynelson.com/blog/2021/04/10/lectio-2021-04-11/'
    url_input_laudes = str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day-1)
    url_input_visperas = str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day)
    url_input_completas = str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day)
    url_input_lectio = str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day-1)

    #Url_Dates
    url_date_laudes = date
    url_date_visperas = date
    url_date_completas =  date.replace("-","")
    url_date_lectio = date

    #str(dt.year)+str(dt.month)+str(dt.day)

    dict_inputs={
        'laudes': [url_input_laudes,url_date_laudes],
        'visperas': [url_input_visperas,url_date_visperas],
        'completas': [url_input_completas,url_date_completas],
        'lectio': [url_input_lectio,url_date_lectio],
    }

    #urls_finales
    url_base='http://fraynelson.com/blog/'

    dict_urls = {}
    for oracion, inputs_urls in dict_inputs.items():
        dict_urls[oracion] = url_base+inputs_urls[0]+'/'+oracion+'-'+inputs_urls[1]+'/'

    dict_salida = {}
    for oracion, url in dict_urls.items():
        #print('\nEmpezamos con: ',oracion)
        #print('Accederemos a la url:',url)
        #print('Procesando ...................\n')
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            title_elem = soup.find('h1', class_='title entry-title')
            body = soup.find('div', class_='nv-content-wrap entry-content')
            description = body.find_all('p')
            youtube = body.find('iframe', class_='youtube-player')
            audio = body.find('a', class_='powerpress_link_d',href=True, title='Download')
            dict_prov = {
                'titulo': title_elem.text,
                'texto': description[0].text,
                'descripcion': description[1].text,
                'audio': audio['href']
            }
            #hacks
            if oracion == 'lectio':
                dict_prov['texto']=description[1].text
            if oracion == 'completas':
                dict_prov['texto']='#'+dict_prov['texto'].split("#",1)[1]
            #print('titulo:',title_elem.text)
            #print('p_0:', description[0].text)
            #print('p_1:',description[1].text)
            #print('p_2:',description[2].text)
            3print('p_3:',description[3].text)
            #print('audio:',audio['href'])
            if youtube is not None:
                dict_prov['youtube']=youtube['src']
                #print('youtube:',youtube['src'])
            else:
                dict_prov['youtube']=''
            dict_salida[oracion] = dict_prov
        except:
            continue

    return dict_salida
#get_oraciones_liturgia('2021-04-18')
