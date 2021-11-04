from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import configparser as cp
import itertools
from typing import List

from info.book_info import BookInfo

def get_soup(url) -> bs:
    page = requests.get(url)
    return bs(page.content, 'html.parser')


def add_csv(fields: List[str], file: str) -> None:  
    print(fields)
    fields_str = ",".join(fields)
    with open(file, 'a') as fd:
        fd.write(fields_str+"\n")


def get_books(soup) -> str:
    for a in soup.find_all('a', {'class': 'bookTitle'}, href=True):
        yield a['href']


def all_books() -> None:
    for i in range(1, 101):
        seed_url = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page={}".format(i)
        soup = get_soup(seed_url)
        for book in get_books(soup):
            BookInfo("https://www.goodreads.com/" + book) 


if __name__ == "__main__": 
    # Read configurations.
    config = cp.ConfigParser()
    config.read("../config.ini")

    if config.get('default', 'debug'):
        books_csv = config.get('paths', 'books_csv') 
        one_book_page = config.get('webpages', 'one_book') 
        book = BookInfo(one_book_page)
        add_csv(book.get_fields_name(), books_csv)          # Adds the header
        add_csv(book.info, books_csv)                 # Adds the information
    else:
        all_books()


# https://www.goodreads.com/book/show/13130963-seven-databases-in-seven-weeks
# https://www.goodreads.com/book/show/45153160-a-black-women-s-history-of-the-united-states
