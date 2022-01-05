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
                            JOIN genres ON book.id = genres.book_id;''')

        # Combine books_genres with authors in books_author_name
        self.cursor.execute("DROP VIEW IF EXISTS books_author_name") 
        self.cursor.execute('''CREATE VIEW books_author_name AS
                            SELECT books_genres.id, books_genres.title, books_genres.image_url, books_genres.num_pages, books_genres.publisher, books_genres.date, books_genres.description, books_genres.isbn, books_genres.genres, author.name as author
                            FROM books_genres
                            JOIN author ON books_genres.author = author.id;''')

        # Concact book authors from same book in one row
        self.cursor.execute("DROP TABLE IF EXISTS books_combined") 
        self.cursor.execute('''CREATE TABLE books_combined (
                            id INTEGER,
                            title VARCHAR(255),
                            image_url VARCHAR(255),
                            num_pages VARCHAR(255),
                            publisher VARCHAR(255),
                            date VARCHAR(255),
                            description VARCHAR(255),
                            isbn INTEGER,
                            genres VARCHAR(255),
                            author VARCHAR(255));''')

        self.cursor.execute('''INSERT INTO books_combined(id, title, image_url, num_pages, publisher, date, description, isbn, genres, author)
                            SELECT id, title, image_url, num_pages, publisher, date, description, isbn, ('"' || genres || '"') as genres, group_concat(author, ';') as author
                            FROM books_author_name
                            GROUP BY id, title, image_url, num_pages, publisher, date, description, isbn;''')

        self.cursor.execute("DROP VIEW IF EXISTS books_genres") 
        self.cursor.execute("DROP VIEW IF EXISTS books_author_name") 
        self.connection.commit()
