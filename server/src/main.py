import sqlite3
import csv

from clean.authors import AuthorsClean
from clean.books import BooksClean
from clean.genres import GenresClean
from clean.reviews import ReviewsClean

from combine.books import BooksCombine
from combine.reviews import ReviewsCombine

AUTHORS_PATH = '../data/raw/authors.json'
BOOKS_PATH = '../data/raw/books.json'
GENRES_PATH = '../data/raw/genres.json'
REVIEWS_PATH = '../data/raw/reviews.json'

def dump_csv(cursor):
    cursor.execute("SELECT * FROM books_combined") 
    rows = cursor.fetchall()
    with open('../data/search/books.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "image_url", "num_pages", "publisher", "date", "description", "isbn", "genres", "authors"])
        writer.writerows(rows)
    
    cursor.execute("SELECT * FROM reviews_combined") 
    rows = cursor.fetchall()
    with open('../data/search/reviews.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["review_id", "book_id", "rating", "review_text", "date_added", "title", "genres", "authors"])
        writer.writerows(rows)

if __name__ == '__main__':
    connection = sqlite3.connect(f'../data/books.db')
    cursor = connection.cursor()
    
    AuthorsClean(connection, cursor).clean(AUTHORS_PATH)
    BooksClean(connection, cursor).clean(BOOKS_PATH)
    GenresClean(connection, cursor).clean(GENRES_PATH)
    ReviewsClean(connection, cursor).clean(REVIEWS_PATH)
    print("Finished Cleaning")

    BooksCombine(connection, cursor).combine()
    ReviewsCombine(connection, cursor).combine()
    print("Finished Combine")

    dump_csv(cursor)
    print("Finished Dumping CSV File")