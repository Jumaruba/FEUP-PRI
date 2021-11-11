import json
import csv
import os 

MAX_BOOKS = 11000
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
RAW_PATH = CURRENT_PATH + "/../../data/raw/books.json"
CLEAN_PATH = CURRENT_PATH + "/../../data/clean/books.csv"


def get_authors(authors_arr):
    authors_names = []

    for author_obj in authors_arr:
        authors_names.append(int(author_obj["author_id"]))

    return authors_names

def get_series(series_arr):
    series = []
    for series_obj in series_arr:
        series.append(int(series_obj))
    return series

def clean_books():
    books_raw = open(RAW_PATH ,"r")
    books_clean = open(CLEAN_PATH ,"w", newline="\n", encoding="utf-8")
    writer = csv.writer(books_clean)

    header = ["isbn", "series", "language_code", "is_ebook", "average_rating", "description", "format", "authors", 
    "publisher", "num_pages", "publication_day", "isbn13", "publication_month", "edition_information", "publication_year", 
    "image_url", "book_id", "title"]
    writer.writerow(header)

    n_books = 0
    for books_obj in books_raw: 
        if n_books == MAX_BOOKS:
            break
        book = json.loads(books_obj)
        book.pop("text_reviews_count", None)
        book.pop("country_code", None)
        book.pop("popular_shelves", None)
        book.pop("asin", None)
        book.pop("kindle_asin", None)
        book.pop("link", None)
        book.pop("url", None)
        book.pop("work_id", None)
        book.pop("ratings_count", None)
        book.pop("similar_books", None)
        book.pop("title_without_series", None) # TODO - keep this; Must change header

        if book['description'] and book['book_id']: 
            book['authors'] = get_authors(book["authors"])
            book['series'] = get_series(book["series"])   

            writer.writerow(list(book.values()))
            n_books += 1
        
    books_raw.close()
    books_clean.close() 


if __name__ == '__main__':
    clean_books()