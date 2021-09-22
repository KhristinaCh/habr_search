import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com'

response = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(response.text, features='html.parser')

# preview = soup.find(class_='tm-article-snippet')
previews = soup.find_all(class_='tm-article-snippet')

# основное задание
for p in previews:
    for word in KEYWORDS:
        if word in p.text:
            time = p.find('time').attrs.get('title')
            title = p.find('h2').find('a').find('span').text
            href = p.find('h2').find('a').attrs.get('href')
            print(f'{time} - {title} - {URL+href}')

# дополнительное задание
for p in previews:
    href = URL + p.find('h2').find('a').attrs.get('href')
    res_article = requests.get(href)
    soup_article = BeautifulSoup(res_article.text, features='html.parser')
    full_text = soup_article.find(id="post-content-body").text
    for word in KEYWORDS:
        if word in full_text:
            time = p.find('time').attrs.get('title')
            title = p.find('h2').find('a').find('span').text
            print(f'{time} - {title} - {href}')
