from datetime import datetime
import requests
from bs4 import BeautifulSoup



url='https://fraynelson.com/blog/categorias/homilias/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

body = soup.find('div', class_='posts-wrapper row')
articles = body.find_all('article')

max = 3
urls = []
for i, article in enumerate(articles):
    title = article.find('h2', class_='blog-entry-title entry-title')
    url = title.find('a')
    urls.append(url['href'])
    print(url['href'])
    if i >=3:
        break

for url in urls:
    print(url,'.........................')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup_day)

    title = soup.find('h1', class_='title entry-title')
    body = soup.find('div', class_='nv-content-wrap entry-content')
    p_alls = body.find_all('p')
    description = p_alls[0]
    youtube = body.find('iframe', class_='youtube-player')
    #print(body)
    print(title.text)
    print(description.text)
    print(youtube['src'])
    """
    content_day = soup_day.find_all('p')
    description = content_day[0]
    youtube = soup_day.find('iframe', class_='youtube-player')

    print(title.text)
    print(description.text)
    print(youtube['src'])
    """


#audio = body.find('a', class_='powerpress_link_d',href=True, title='Download')
