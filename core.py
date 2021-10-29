import mechanize as mc 
from bs4 import BeautifulSoup as bs


br = mc.Browser()

def get_html(br, url):
    page = br.open(url)
    return page.read()

def get_book_title(html):
    soup = bs(html)
    return soup.find('h1', attrs={'id': 'bookTitle'}).get_text()

def get_book_authors(html):
    soup = bs(html)
    div_authors = soup.find('div', attrs={'id': 'bookAuthors'})
    a_authors = div_authors.find_all('a', attrs={'class': 'authorName'})
    authors = []
    for a_tag in a_authors:
        authors.append(a_tag.span.get_text())

    return authors


html = get_html(br, "https://www.goodreads.com/book/show/13130963-seven-databases-in-seven-weeks")
print(get_book_title(html))
print(get_book_authors(html))
