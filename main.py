import json
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://quotes.toscrape.com'
urls = []
urls.append(BASE_URL)


def about_author_dict(url_about_author, author):
    response = requests.get(url_about_author)
    soup = BeautifulSoup(response.text, 'html.parser')

    born_date = soup.find("span", class_="author-born-date").text
    born_location = soup.find("span", class_="author-born-location").text
    description = soup.find("div", class_="author-description").text.strip()

    author_dict = {
        "fullname": author,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }
    return author_dict


def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    next_page = soup.find("li", class_="next")

    if next_page:
        next_url = BASE_URL + next_page.a["href"]
        urls.append(next_url)
        get_urls(next_url)
    return urls


def tags_for_quote(tags):
    tags_for_quote = []
    tagsforquote = tags.find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        tags_for_quote.append(tagforquote.text)
    return tags_for_quote


def spider(urls):
    authors_for_js = []
    quotes_for_js = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        tags = soup.find_all('div', class_='tags')
        urls_about_author = soup.find_all("a", string="(about)")

        for i in range(0, len(quotes)):
            url_about_author = BASE_URL + urls_about_author[i]["href"]

            if authors[i].text not in [author["fullname"] for author in authors_for_js]:
                authors_for_js.append(about_author_dict(
                    url_about_author, authors[i].text))

            quotes_for_js.append({
                "tags": tags_for_quote(tags[i]),
                "author": authors[i].text,
                "quote": quotes[i].text.strip("“”")
            })

    return quotes_for_js, authors_for_js


def write_date_in_filejs(name_file, date):
    with open(name_file, "w") as fh:
        json.dump(date, fh, indent=4)


if __name__ == "__main__":
    urls_for_scraping = get_urls(BASE_URL)
    quotes, authors = spider(urls_for_scraping)
    write_date_in_filejs("qoutes.json", quotes)
    write_date_in_filejs("authors.json", authors)
