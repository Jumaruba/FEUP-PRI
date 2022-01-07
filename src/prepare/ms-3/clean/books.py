from collections import defaultdict
import sqlite3
import csv
import json

class BooksClean:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def get_authors(self, authors_arr):
        authors_ids = []
        for author_obj in authors_arr:
            authors_ids.append(int(author_obj["author_id"]))
        return authors_ids


    def get_series(self, series_arr):
        series_ids = []
        for series_id in series_arr:
            series_ids.append(int(series_id))
        return series_ids

    def recentBook(self, bookList):
        older = bookList[0]
        if(len(bookList) != 1): 
            for book in bookList:  
                if older[5] > book[5]: older = book
        return older

    def book_to_store(self, book):
        return bool(book["publication_day"]) and bool(book["publication_month"]) \
        and bool(book["publication_year"]) and book['description'] \
        and book['isbn'] and book['book_id'] and \
        (book['language_code'] == 'eng') and bool(book['num_pages'])

    def clean(self, path):
        print("Cleaning Books")
        # -- Table book
        self.cursor.execute("DROP TABLE IF EXISTS book")
        self.cursor.execute('''CREATE TABLE book (
                            book_id INTEGER,
                            title VARCHAR(255),
                            image_url VARCHAR(255),
                            num_pages VARCHAR(255),
                            format VARCHAR(255),
                            publisher VARCHAR(255),
                            date VARCHAR(255),
                            description VARCHAR(255),
                            isbn INTEGER);''')
        # -- Table that relates an author to a book
        self.cursor.execute("DROP TABLE IF EXISTS book_author")
        self.cursor.execute('''CREATE TABLE book_author (
                            book_id INTEGER,
                            author_id INTEGER,
                            FOREIGN KEY(book_id) REFERENCES book(book_id),
                            FOREIGN KEY(author_id) REFERENCES author(author_id));''')
        
        # -- Table that relates a series to a book
        self.cursor.execute("DROP TABLE IF EXISTS book_series")
        self.cursor.execute('''CREATE TABLE book_series (
                            book_id INTEGER,
                            series_id INTEGER,
                            FOREIGN KEY(book_id) REFERENCES book(book_id),
                            FOREIGN KEY(series_id) REFERENCES series(series_id));''')

        book_insert = defaultdict(list)
        books_raw = open(path, "r")
        for books_obj in books_raw: 
            book = json.loads(books_obj)
            if self.book_to_store(book):   
                day = int(book["publication_day"])
                month = int(book["publication_month"])
                year = int(book["publication_year"])
                
                book_id = book['book_id']
                title = book['title']
                image_url = book['image_url']
                num_pages = int(book['num_pages']) 
                format = book['format']
                publisher = book['publisher']
                date = "%04d-%02d-%02d" % (year,month,day)
                authors = self.get_authors(book["authors"])
                series_arr = self.get_series(book["series"])
                description = book['description']
                isbn = book['isbn']
                book_insert[title].append([book_id, title, image_url, num_pages, format, publisher, date, authors, series_arr, description, isbn])
        books_raw.close()

        insert_books = []
        insert_book_authors = []
        insert_book_series = []
        for key in book_insert:
            new_book = self.recentBook(book_insert[key])
            insert_books.append([new_book[0], new_book[1], new_book[2], new_book[3], new_book[4], new_book[5], new_book[6], new_book[9], new_book[10]])

            authors_arr = new_book[7]
            for author in authors_arr:
                insert_book_authors.append([new_book[0],author])

            series_arr = new_book[8]
            for series in series_arr:
                insert_book_series.append([new_book[0],series])
            
        insert_book_records = "INSERT INTO book(book_id,title,image_url,num_pages,format,publisher,date,description,isbn) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        insert_book_authors_records = "INSERT INTO book_author(book_id,author_id) VALUES (?, ?)"
        insert_book_series_records = "INSERT INTO book_series(book_id,series_id) VALUES (?, ?)"
        self.cursor.executemany(insert_book_records, insert_books)
        self.cursor.executemany(insert_book_authors_records, insert_book_authors)
        self.cursor.executemany(insert_book_series_records, insert_book_series)
        self.connection.commit()
        print("Finished Cleaning Books")
        