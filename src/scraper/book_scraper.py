from scraper.scraper import Scraper

from typing import List
from bs4 import BeautifulSoup as bs
import re

class BookScraper(Scraper):

    def __init__(self, url):
        Scraper.__init__(self, url)

    def retrieve_info(self) -> List[str]:
        [isbn10, isbn13] = self.get_isbn()
        self.info = [self.get_book_title(), ", ".join(self.get_book_authors()), self.get_description(), self.get_number_pages(),
                     self.get_publisher(), isbn10, isbn13, self.get_rating(), self.get_last_date(), 
                     self.get_first_date(), self.get_author_url()]


    def get_book_title(self):
        series = self.soup.find('h2', attrs={'id': 'bookSeries'}).get_text()
        print(self.soup.find('h1', attrs={'id': 'bookTitle'}).get_text().strip())
        return self.soup.find('h1', attrs={'id': 'bookTitle'}).get_text().strip() + " " + series.strip()

    def get_book_authors(self):
        div_authors = self.soup.find('div', attrs={'id': 'bookAuthors'})
        a_authors = div_authors.find_all('a', attrs={'class': 'authorName'})
        authors = []
        for a_tag in a_authors:
            author = self.replace_multiple_spaces(a_tag.span.get_text())
            authors.append(author)

        return authors

    # May in the future return some error.
    def get_description(self):
        div_desc = self.soup.find('div', attrs={'id': 'description'})
        desc = div_desc.find_all('span')[1]
        return desc.get_text()

    def get_number_pages(self):
        pages = self.soup.find(
            'span', attrs={'itemprop': 'numberOfPages'}).text
        # Removing pages string.
        return pages.split(" ")[0]

    def get_publisher(self):
        details = self.soup.find('div', attrs={'id': 'details'})
        publication_details = details.find_all(
            'div', attrs={'class': 'row'})[1].get_text()
        # Removing original publication date
        return publication_details.split('by')[1].split("(")[0].strip()

    def get_last_date(self):
        details = self.soup.find('div', attrs={'id': 'details'})
        publication_details = details.find_all('div', attrs={'class': 'row'})[1].get_text()
        date_text = publication_details.split('by')[0].strip('\n')
        return date_text.split('Published')[1].strip()

    def get_first_date(self):
        details = self.soup.find('div', attrs={'id': 'details'})
        original_date = details.find_all('div', attrs={'class': 'row'})[1].find('nobr')
        return '' if original_date is None else re.search('\(first published ([^)]+)', original_date.get_text()).group(1)

    def get_isbn(self):
        details = self.soup.find('div', attrs={'id': 'bookDataBox'})
        details_titles = details.find_all('div', attrs={'class': 'infoBoxRowTitle'})
        details_titles_texts = [x.get_text().strip() for x in details_titles]

        try:
            isbn_idx = details_titles_texts.index("ISBN")
        except ValueError:
            return '', ''

        isbn_text = details.find_all('div', attrs={'class': 'infoBoxRowItem'})[isbn_idx].get_text()
        isbn_parts = re.split('(\([^\)]*\))', isbn_text)

        isbn10 = isbn_parts[0].strip()
        isbn13 = '' if len(isbn_parts) == 1 else re.search('\(ISBN13: ([^)]+)', isbn_parts[1]).group(1)
        return isbn10, isbn13

    def get_rating(self):
        meta = self.soup.find('div', attrs={'id': 'bookMeta'})
        rating_span = meta.find('span', attrs={'itemprop': 'ratingValue'})
        return rating_span.get_text().strip()

    def get_author_url(self):
        return self.soup.find('div', attrs={'class': 'bookAuthorProfile__name'}).a['href']


# TODO: reviews?
