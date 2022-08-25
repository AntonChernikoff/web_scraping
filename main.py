import requests
from bs4 import BeautifulSoup

main_url = 'https://habr.com'
base_url = 'https://habr.com/ru/all/'
words = ['google', 'sql', 'биткоин', 'python']
HEADERS = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding':'gzip,deflate,sdch',
           'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
           'Cache-Control':'max-age=0',
           'Origin':'http://site.ru',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.0 Safari/537.36'}


def parser_page(url_page):
    response = requests.get(url_page, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_body = soup.find('div', class_="tm-article-body")
    for word in words:
        if word in article_body.text.lower():
            return True
    return False

def parser():
    response = requests.get(base_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    articls = soup.find_all('article', class_="tm-articles-list__item")
    for article in articls:
        article_url = article.find('a', class_="tm-article-snippet__title-link")
        article_time = article.find('time')
        article_body = article.find('div', class_ = "article-formatted-body article-formatted-body article-formatted-body_version-2")
        article_body = article.find('div', class_ = "tm-article-snippet")
        if not article_url == None:
            # print(f'{main_url}{article_url["href"]} {article_time["title"]} {article_url.text}')
            if parser_page(f'{main_url}{article_url["href"]}'):
                print(f'{article_time["title"]} {article_url.text} {main_url}{article_url["href"]}')

if __name__ == '__main__':
    parser()

