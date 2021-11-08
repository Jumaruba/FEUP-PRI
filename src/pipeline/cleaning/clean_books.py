import json
import csv

def clean_books():
    books_raw = open("../../data/raw/books.json" ,"r")
    books_clean = open("../../data/clean/books.csv" ,"w", newline="\n", encoding="utf-8")
    writer = csv.writer(books_clean)

    header = ["isbn", "series", "language_code", "is_ebook", "average_rating", "description", "format", "authors", 
    "publisher", "num_pages", "publication_day", "isbn13", "publication_month", "edition_information", "publication_year", "image_url", "book_id", "title"]
    writer.writerow(header)

    for books_obj in books_raw: 
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
        if book['description']: writer.writerow(book.values())
        
    books_raw.close()
    books_clean.close() 


if __name__ == '__main__':
    clean_books()