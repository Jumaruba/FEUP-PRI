from bs4 import BeautifulSoup as bs
import requests
from core import BookInfo

def get_soup(url):
    page = requests.get(url)
    return bs(page.content, 'html.parser')

def get_books(soup): 
    for a in soup.find_all('a', {'class':'bookTitle'}, href=True):
        yield a['href']

def one_book(url):
    book = BookInfo(url)
    print(book.get_book_title())
    print(book.get_book_authors())
    print(book.get_description())
    print(book.get_number_pages())
    print(book.get_publisher())
    print(book.get_isbn())
    print(book.get_isbn13())
    print(book.get_rating())
    print(book.get_last_date())
    print(book.get_first_date())

def all_books():
    for i in range(1, 101):
        seed_url = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page={}".format(i)
        soup = get_soup(seed_url)
        for book in get_books(soup):
            one_book("https://www.goodreads.com/" + book)

if __name__ == "__main__":
    val_input = input("Type 0 for one book. Another key for all books.\n")
    if val_input == "0":
        one_book("https://www.goodreads.com/book/show/2767052-the-hunger-games")
    else:
        all_books()


# https://www.goodreads.com/book/show/13130963-seven-databases-in-seven-weeks
# https://www.goodreads.com/book/show/45153160-a-black-women-s-history-of-the-united-states
