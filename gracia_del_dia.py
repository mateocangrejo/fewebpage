from datetime import datetime
import requests
from bs4 import BeautifulSoup


def get_gracia_dia(date):

    url='https://fraynelson.com/blog/categorias/homilias/'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    #body = soup.find('div', class_='posts-wrapper row')
    body = soup.find('div', class_='content-area')
    articles = body.find_all('article')

    max = 3
    urls = []
    for i, article in enumerate(articles):
        title = article.find('h2', class_='entry-title')
        url = title.find('a')
        print(url)
        if date in url['href']:
            urls.append(url['href'])
            print(url['href'])
        if i >=max:
            break

    for url in urls:
        #print('.........................')
        #print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup_day)

        title = soup.find('h1', class_='entry-title')
        body = soup.find('div', class_='entry-content')
        p_alls = body.find_all('p',attrs={'class': None})
        #print(len(p_alls))
        texto = p_alls[0]
        description = p_alls[1]

        if len(p_alls) >=3:
            dict_prov = {
                'titulo': title.text,
                'texto': texto.text,
                'descripcion': description.text,
            }
        else:
            dict_prov = {
                'titulo': title.text,
                'texto': "",
                'descripcion': texto.text,
            }

        audio = body.find('a', class_='powerpress_link_pinw')#,title='Download')
        youtube = body.find('iframe') #, class_='youtube-player')
        #print(audio)

        #print('titulo',title.text)
        #print('texto',texto.text)
        #print('descripcion',description.text)
        if audio is not None:
            dict_prov['audio'] = audio['href']
            #print('audio',audio['href'])

        else:
            dict_prov['audio'] = ""
        if youtube is not None:
            dict_prov['youtube'] = youtube['src']
            #print('youtube',youtube['src'])
        else:
            dict_prov['youtube'] = ""
        return dict_prov
#print(get_gracia_dia('2022-03-17'))
