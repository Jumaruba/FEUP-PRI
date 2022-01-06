import json
import csv
import os 
from pandas.core.frame import DataFrame

MAX_BOOKS = 11000
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
RAW_PATH = CURRENT_PATH + "/../../data/raw/books.json"
RAW_SERIES_PATH = CURRENT_PATH + "/../../data/raw/series.json"
CLEAN_PATH = CURRENT_PATH + "/../../data/clean/books.csv"


def get_authors(authors_arr):
    authors_names = []

    for author_obj in authors_arr:
        authors_names.append(int(author_obj["author_id"]))

    return authors_names

def get_series():
    series = {}
    
    with open(RAW_SERIES_PATH) as f:
        for line in f:
            json_line = json.loads(line)
            series[json_line['series_id']] =  json_line['title']
    
    return series

def clean_books():
    books_raw = open(RAW_PATH ,"r")
    series = get_series()
    books_clean = open(CLEAN_PATH ,"w", newline="\n", encoding="utf-8")
    writer = csv.writer(books_clean)

    header = ["isbn", "series", "language_code", "is_ebook", "average_rating", "description", "format", "authors", 
    "publisher", "num_pages", "isbn13", "edition_information", "image_url", "book_id", "title", "date"]
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
        book.pop("title_without_series", None) 
        
        day = 0 if not bool(book["publication_day"]) else int(book["publication_day"])
        month = 0 if not bool(book["publication_month"]) else int(book["publication_month"])
        year = 0 if not bool(book["publication_year"]) else int(book["publication_year"])
        date = "%04d-%02d-%02d" % (year,month,day)
        book.pop("publication_day", None)
        book.pop("publication_month", None)
        book.pop("publication_year", None) 
        book['num_pages'] = int(book['num_pages'] if book['num_pages'] != '' else 0) 

        if len(book['series']) == 0:
            series_title = []
        else:
            series_titles = []
            for series_id in book['series']:
                series_titles.append(series.get(series_id))
            book['series'] = series_titles
        
        if book['description'] and book['book_id']: 
            book['authors'] = get_authors(book["authors"])
            book_values = list(book.values())
            book_values.append(date)
            writer.writerow(book_values)
            n_books += 1
        
    books_raw.close()
    books_clean.close() 


if __name__ == '__main__':
    clean_books()