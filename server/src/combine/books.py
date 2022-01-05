import sqlite3
import csv
import json

class BooksCombine:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def combine(self):
        self.cursor.execute("DROP VIEW IF EXISTS books_temp") 
        self.cursor.execute('''CREATE VIEW books_temp AS
                            SELECT book.book_id AS book_id, group_concat(author.name, ';') AS authors, group_concat(series.series_name, ';') AS series, genres.genres AS genres
                            FROM book JOIN genres ON book.book_id = genres.book_id
                            JOIN book_author ON book_author.book_id = book.book_id
                            JOIN book_series ON book_series.book_id = book.book_id
                            JOIN author ON author.author_id = book_author.author_id
                            JOIN series ON series.series_id = book_series.series_id
                            GROUP BY book.book_id;''')

        print("created view")

        # # Combine books with genres in books_genres
        # self.cursor.execute("DROP VIEW IF EXISTS books_genres") 
        # self.cursor.execute('''CREATE VIEW books_genres AS
        #                     SELECT book.book_id AS book_id, title, image_url, num_pages, publisher, date, description, isbn, author, series, genres.genres as genres
        #                     FROM book
        #                     JOIN genres ON book.book_id = genres.book_id;''')

        # # Combine books_genres with authors and series in books_author_series
        # self.cursor.execute("DROP VIEW IF EXISTS books_author_series") 
        # self.cursor.execute('''CREATE VIEW books_author_series AS
        #                     SELECT books_genres.book_id, books_genres.title, books_genres.image_url, books_genres.num_pages, books_genres.publisher, books_genres.date, 
        #                         books_genres.description, books_genres.isbn, books_genres.genres, series_name as series, author.name as author
        #                     FROM books_genres
        #                     JOIN author ON books_genres.author = author.author_id
        #                     JOIN series ON books_genres.series = series.series_id;''')

        # Concatenate book authors and series from same book in one row
        self.cursor.execute("DROP TABLE IF EXISTS books_combined") 
        self.cursor.execute('''CREATE TABLE books_combined (
                            book_id INTEGER,
                            title VARCHAR(255),
                            image_url VARCHAR(255),
                            num_pages VARCHAR(255),
                            publisher VARCHAR(255),
                            date VARCHAR(255),
                            description VARCHAR(255),
                            isbn INTEGER,
                            genres VARCHAR(255),
                            authors VARCHAR(255),
                            series VARCHAR(255));''')

        print("created table books_combined")

        self.cursor.execute('''INSERT INTO books_combined(book_id, title, image_url, num_pages, publisher, date, description, isbn, genres, authors, series)
                            SELECT book.book_id, title, image_url, num_pages, publisher, date, description, isbn, genres, authors, series
                            FROM books_temp JOIN book ON books_temp.book_id = book.book_id;''')
 
        self.connection.commit()

        print("books combine done")