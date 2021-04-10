from datetime import datetime
import requests
from bs4 import BeautifulSoup

#Data Fecha
date = input("Hola, registra una fecha en formato 2021-04-10: ")
dt = datetime.strptime(date, '%Y-%m-%d')
print('Registraste la fecha:', dt.year,'-',dt.month,'-',dt.day)

#urls_inputs
#URL_ori_laudes = 'http://fraynelson.com/blog/2021/04/10/laudes-2021-04-11/'
#URL_ori_visperas = 'https://fraynelson.com/blog/2021/04/10/visperas-2021-04-10/'
#URL_ori_completas = 'https://fraynelson.com/blog/2021/04/10/completas-20210410/'
url_input_laudes = str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day-1)
url_input_visperas = str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day)
url_input_completas = str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day)

#Url_Dates
url_date_laudes = date
url_date_visperas = date
url_date_completas =  date.replace("-","")

#str(dt.year)+str(dt.month)+str(dt.day)

dict_inputs={
    'laudes': [url_input_laudes,url_date_laudes],
    'visperas': [url_input_visperas,url_date_visperas],
    'completas': [url_input_completas,url_date_completas]
}

#urls_finales
url_base='http://fraynelson.com/blog/'

dict_urls = {}
for oracion, inputs_urls in dict_inputs.items():
    dict_urls[oracion] = url_base+inputs_urls[0]+'/'+oracion+'-'+inputs_urls[1]+'/'

for oracion, url in dict_urls.items():
    print('Empezamos con: ',oracion)
    print('Accederemos a la url:',url)
    print('Procesando ...................')
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    #print('todo correcto hasta aca')

    #results = soup.find(id='ResultsContainer')
    title_elem = soup.find('h1', class_='title entry-title')
    body = soup.find('div', class_='nv-content-wrap entry-content')

    description = body.find_all('p')
    audio = body.find('a', class_='powerpress_link_d',href=True, title='Download')

    print(title_elem.text)
    print(description[0].text)
    print(audio['href'])
