from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import configparser as cp
import itertools
from typing import List

from info.book_info import BookInfo


books_fields =  ['title','authors','description','number_pages','publisher','isbn','isbn13','rating','last_date','first_date','author_url'] 

def get_soup(url) -> bs:
    page = requests.get(url)
    return bs(page.content, 'html.parser')


def add_csv(fields: List[str], file: str) -> None:  
    fields_str = ",".join(fields)
    with open(file, 'a') as fd:
        fd.write(fields_str+"\n")


def get_books(soup) -> str:
    for a in soup.find_all('a', {'class': 'bookTitle'}, href=True):
        yield a['href']


def retrieve_all_books(config) -> None:
    for i in range(1, 101): 
        seed_url = config.get('webpages', 'seed_url').format(i)
        soup = get_soup(seed_url)

        for book in get_books(soup):
            url_page = config.get('webpages', 'goodreads') + book
            retrieve_one_book(config, url_page)


def retrieve_one_book(config, url_page: str) -> None:
    book = BookInfo(url_page)
    add_csv(book.info, config.get('paths', 'books_csv'))                       # Adds the information


if __name__ == "__main__": 
    # Read configurations.
    config = cp.ConfigParser()
    config.read("../config.ini")
    debug = eval(config.get('default', 'debug'))
    books_csv = config.get('paths', 'books_csv')
    open(config.get('paths', 'books_csv'), "w")                                # Create the file  
    add_csv(books_fields, books_csv)  
                                             # Add header
    if debug:
        one_book_page = config.get('webpages', 'one_book') 
        retrieve_one_book(config, one_book_page)
    else:
        retrieve_all_books(config)


# https://www.goodreads.com/book/show/13130963-seven-databases-in-seven-weeks
# https://www.goodreads.com/book/show/45153160-a-black-women-s-history-of-the-united-states
