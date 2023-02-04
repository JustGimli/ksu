from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout, TooManyRedirects, ConnectionError

def get_habr():

    resp = requests.get("https://habr.com/ru/flows/develop/")

    soup = BeautifulSoup(resp.content, "lxml")

    result = {}

    for news in soup.find_all("a", class_="tm-article-snippet__title-link"):
        news_name = news.span.text
        news_link = news.get('href')
        result.update({"news_name": news_name, "news_link": news_link})
        
        return result


get_habr()