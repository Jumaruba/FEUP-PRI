from collections import defaultdict
import sqlite3
import csv
import json

class BooksClean:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def get_authors(self, authors_arr):
        authors_names = []
        for author_obj in authors_arr:
            authors_names.append(int(author_obj["author_id"]))
        return authors_names

    def recentBook(self, bookList):
        older = bookList[0]
        if(len(bookList) != 1): 
            for book in bookList:  
                if older[5] > book[5]: older = book
        return older

    def clean(self, path):
        # -- Table book
        self.cursor.execute("DROP TABLE IF EXISTS book")
        self.cursor.execute('''CREATE TABLE book (
                            id INTEGER,
                            title VARCHAR(255),
                            image_url VARCHAR(255),
                            num_pages VARCHAR(255),
                            publisher VARCHAR(255),
                            date VARCHAR(255),
                            language_code VARCHAR(255),
                            author VARCHAR(255),
                            description VARCHAR(255),
                            isbn INTEGER);''')

        book_insert = defaultdict(list)
        books_raw = open(path, "r")
        for index, books_obj in enumerate(books_raw): 
            book = json.loads(books_obj)
            if book['description'] and book['book_id'] and (book['language_code'] == 'eng' or book['language_code'] == 'pt' or book['language_code'] == 'en-US'):   
                day = 1 if not bool(book["publication_day"]) else int(book["publication_day"])
                month = 1 if not bool(book["publication_month"]) else int(book["publication_month"])
                if not bool(book["publication_year"]): continue
                else: year = int(book["publication_year"])
                
                book_id = book['book_id']
                title = book['title']
                image_url = book['image_url']
                num_pages = int(book['num_pages'] if book['num_pages'] != '' else 0) 
                publisher = book['publisher']
                date = "%04d-%02d-%02d" % (year,month,day)
                language_code  = book['language_code']
                author = self.get_authors(book["authors"])
                description = book['description']
                isbn = book['isbn']
                book_insert[title].append([book_id, title, image_url, num_pages, publisher, date, language_code, author, description, isbn])
        books_raw.close()

        insert = []
        for key in book_insert:
            new_book = self.recentBook(book_insert[key])
            authors = new_book[7]
            for author in authors:
                insert.append([new_book[0], new_book[1], new_book[2], new_book[3], new_book[4], new_book[5], new_book[6], author, new_book[8], new_book[9]])
            
        insert_records = "INSERT INTO book(id,title,image_url,num_pages,publisher,date,language_code,author,description,isbn) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.executemany(insert_records, insert)
        self.connection.commit()
        

