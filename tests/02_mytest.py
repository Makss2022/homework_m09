from pprint import pprint
import requests
from bs4 import BeautifulSoup


url = 'http://quotes.toscrape.com/author/Albert-Einstein/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


born_date = soup.find("span", class_="author-born-date").text
born_location = soup.find("span", class_="author-born-location").text
description = soup.find("div", class_="author-description").text.strip()

author_dict = {
    "born_date": born_date,
    "born_location": born_location,
    "description": description,
}

print(author_dict)
