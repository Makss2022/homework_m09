from pprint import pprint
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://quotes.toscrape.com'

urls = []
urls.append(BASE_URL)


def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    next_page = soup.find("li", class_="next")

    if next_page:
        next_url = BASE_URL + next_page.a["href"]
        urls.append(next_url)
        get_urls(next_url)
    return urls


url = BASE_URL
print(get_urls(url))
