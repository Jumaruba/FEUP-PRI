from bs4 import BeautifulSoup as bs
import csv
import requests
import pandas as pd
import configparser as cp
from typing import List

from scraper.book_scraper import BookScraper

# Fields to the books.csv
books_fields =  ['title','authors','description','number_pages','publisher','isbn','isbn13','rating','last_date','first_date','author_url']

def get_soup(url) -> bs:
    page = requests.get(url)
    return bs(page.content, 'html.parser')

def get_books(soup) -> str:
    for a in soup.find_all('a', {'class': 'bookTitle'}, href=True):
        yield a['href']


def retrieve_all_books(config, writer) -> None:
    for i in range(1, 101): 
        seed_url = config.get('webpages', 'seed_url').format(i)
        soup = get_soup(seed_url)

        for book in get_books(soup):
            url_page = config.get('webpages', 'goodreads') + book
            retrieve_one_book(config, writer, url_page)


def retrieve_one_book(config, writer, url_page: str) -> None:
    book = BookScraper(url_page)
    writer.writerow(book.info)
    print('.')


if __name__ == "__main__": 
    # Read configurations.
    config = cp.ConfigParser()
    config.read("../config.ini")
    debug = eval(config.get('default', 'debug'))

    books_fd = open(config.get('paths', 'books_csv'), "a")                     # Create the file 
    books_fd.seek(0)
    books_fd.truncate()
    writer = csv.writer(books_fd) 
    writer.writerow(books_fields)                                           # Adds the header to the csv.

    if debug:
        one_book_page = config.get('webpages', 'one_book') 
        retrieve_one_book(config, writer, one_book_page)
    else:
        retrieve_all_books(config, writer)

    books_fd.close()


# https://www.goodreads.com/book/show/13130963-seven-databases-in-seven-weeks
# https://www.goodreads.com/book/show/45153160-a-black-women-s-history-of-the-united-states
