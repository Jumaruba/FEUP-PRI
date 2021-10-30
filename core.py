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
    publication_details = details.find_all('div', attrs={'class': 'row'})[1].get_text()
    # Removing original publication date
    return publication_details.split('by')[1].split("(")[0].strip() 


def get_last_date(soup):
    details = soup.find('div', attrs={'id': 'details'})
    publication_details = details.find_all('div', attrs={'class': 'row'})[1].get_text()
    date_text = publication_details.split('by')[0].strip('\n')
    return date_text.split('Published')[1].strip()


def get_first_date(soup):
    details = soup.find('div', attrs={'id': 'details'})
    original_date = details.find_all('div', attrs={'class': 'row'})[1].find('nobr')
    return '' if original_date is None else re.search('\(first published ([^)]+)', original_date.get_text()).group(1)


def get_isbn(soup):
    details = soup.find('div', attrs={'id': 'bookDataBox'})
    detail_div = details.find_all('div', attrs={'class': 'clearFloats'})[1]
    detail_title = detail_div.find('div', attrs={'class': 'infoBoxRowTitle'}).get_text()
  
    if detail_title.strip() != 'ISBN':
        return ''

    isbn_text = detail_div.find('div', attrs={'class': 'infoBoxRowItem'}).get_text()
    isbn_parts = re.split('(\([^\)]*\))', isbn_text)
    return isbn_parts[0].strip()


def get_isbn13(soup):
    details = soup.find('div', attrs={'id': 'bookDataBox'})
    detail_div = details.find_all('div', attrs={'class': 'clearFloats'})[1]
    detail_title = detail_div.find('div', attrs={'class': 'infoBoxRowTitle'}).get_text()
    
    if detail_title.strip() != 'ISBN':
        return ''

    isbn_div = detail_div.find('div', attrs={'class': 'infoBoxRowItem'})
    return '' if isbn_div is None else re.search('\(ISBN13: ([^)]+)',isbn_div.get_text()).group(1)


def get_rating(soup):
    meta = soup.find('div', attrs={'id':'bookMeta'})
    rating_span = meta.find('span', attrs={'itemprop':'ratingValue'})
    return rating_span.get_text().strip()

# https://www.goodreads.com/book/show/13130963-seven-databases-in-seven-weeks - no series
# https://www.goodreads.com/book/show/45153160-a-black-women-s-history-of-the-united-states - no first date
# https://www.goodreads.com/book/show/22628.The_Perks_of_Being_a_Wallflower - no isbn
html = get_html(
    br, "https://www.goodreads.com/book/show/2767052-the-hunger-games")


soup = bs(html, "html.parser")
# prettify was adding extra spaces between and after paragraphs
# soup = bs(bs(html, "html.parser").prettify())

print(get_book_title(soup))
print(get_book_authors(soup))
print(get_description(soup))
print(get_number_pages(soup))
print(get_publisher(soup))
print(get_isbn(soup))
print(get_isbn13(soup))
print(get_rating(soup))
print(get_last_date(soup))
print(get_first_date(soup))

# TODO: 
# - reviews?
# - category?
# - get isbn from other website when it does no exist in good reads