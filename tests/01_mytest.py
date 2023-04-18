from pprint import pprint
import requests
import bs4

store_ = []
url = 'http://books.toscrape.com/'
html_doc = requests.get(url)
soup = bs4.BeautifulSoup(html_doc.content, 'html.parser')
books = soup.select('section')[0].find_all(
    "article",  attrs={'class': 'product_pod'})

for book in books:
    book: bs4.element.Tag
    title = book.find("h3").find("a")["title"]
    img_url = f"{url}{book.find('img')['src']}"
    price = float(book.find("p", attrs={"class": "price_color"}).text[1:])
    rating = book.find('p', attrs={'class': 'star-rating'})["class"][1]
    store_.append({
        "title": title,
        "price": price,
        "img_url": img_url
    })

pprint(rating)
pprint(type(rating))
