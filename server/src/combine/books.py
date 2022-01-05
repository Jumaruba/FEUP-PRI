import sqlite3
import csv
import json

class BooksCombine:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def combine(self):
        # Combine books with genres in books_genres
        self.cursor.execute("DROP VIEW IF EXISTS books_genres") 
        self.cursor.execute('''CREATE VIEW books_genres AS
                            SELECT book.*, genres.genres as genres
                            FROM book
                            JOIN genres ON book.book_id = genres.book_id;''')

        print("Combine 1")
        # Combine books_genres with authors in books_author_name
        self.cursor.execute("DROP VIEW IF EXISTS books_author_name") 
        self.cursor.execute('''CREATE VIEW books_author_name AS
                            SELECT books_genres.book_id, books_genres.title, books_genres.image_url, books_genres.num_pages, books_genres.publisher, books_genres.date, books_genres.description, books_genres.isbn, books_genres.genres, group_concat(author.name, ';') as authors
                            FROM books_genres
                            JOIN book_author ON books_genres.book_id = book_author.book_id
                            JOIN author ON author.author_id = book_author.author_id
                            GROUP BY books_genres.book_id;''')

        print("Combine 2")
        self.cursor.execute("DROP TABLE IF EXISTS books_combined") 
        self.cursor.execute('''CREATE TABLE books_combined AS
                            SELECT books_author_name.*, group_concat(series.series_name, ';') as series
                            FROM books_author_name
                            JOIN book_series ON books_author_name.book_id = book_series.book_id
                            JOIN series ON series.series_id = book_series.series_id
                            GROUP BY books_author_name.book_id;''')
        self.connection.commit()