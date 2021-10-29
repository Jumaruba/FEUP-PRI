import mechanize as mc
from bs4 import BeautifulSoup as bs
import re

br = mc.Browser()


def replace_multiple_spaces(str):
    return re.sub('\s+', ' ', str)


def get_html(br, url):
    page = br.open(url)
    return page.read()


def get_book_title(soup): 
    series = soup.find('h2', attrs={'id': 'bookSeries'}).get_text()
    return soup.find('h1', attrs={'id': 'bookTitle'}).get_text().strip() + " " + series.strip()


def get_book_authors(soup):
    div_authors = soup.find('div', attrs={'id': 'bookAuthors'})
    a_authors = div_authors.find_all('a', attrs={'class': 'authorName'})
    authors = []
    for a_tag in a_authors:
        author = replace_multiple_spaces(a_tag.span.get_text())
        authors.append(author)

    return authors


# May in the future return some error.
def get_description(soup):
    div_desc = soup.find('div', attrs={'id': 'description'})
    desc = div_desc.find_all('span')[1]
    return desc.get_text()


def get_number_pages(soup):
    pages = soup.find('span', attrs={'itemprop': 'numberOfPages'}).text
    # Removing pages string.
    return pages.split(" ")[0]


def get_publisher(soup):
    details = soup.find('div', attrs={'id': 'details'})
    return details.find_all('div')[1].get_text().split("by") 


# https://www.goodreads.com/book/show/13130963-seven-databases-in-seven-weeks
html = get_html(
    br, "https://www.goodreads.com/book/show/2767052-the-hunger-games")


soup = bs(bs(html, "html.parser").prettify())
print(get_book_title(soup))
print(get_book_authors(soup))
print(get_description(soup))
print(get_number_pages(soup))
print(get_publisher(soup))