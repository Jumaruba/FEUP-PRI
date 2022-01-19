import sqlite3
import csv
import json

class BooksCombine:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def combine(self):
      print("Combining Books")
      self.cursor.execute("DROP TABLE IF EXISTS books_combined;") 
      self.cursor.execute('''CREATE TABLE books_combined (
                              book_id INTEGER,
                              title VARCHAR(255),
                              image_url VARCHAR(255),
                              num_pages VARCHAR(255),
                              format VARCHAR(255),
                              publisher VARCHAR(255),
                              date VARCHAR(255),
                              description VARCHAR(255),
                              isbn INTEGER,
                              genres VARCHAR(255),
                              authors VARCHAR(255),
                              rating REAL DEFAULT 0,
                              series VARCHAR(255) DEFAULT '');''')

      """
      - books_genres => joins book and genres tables
      - book_author_name => joins books_genres with book_author and author, 
      concatenating the authors of each book in a single tuple
      - books_combined => for now it store the same as book_author_name and as NULL series
      """
      self.cursor.execute('''
                  INSERT INTO books_combined(book_id,title,image_url,num_pages,format,publisher,date,description,isbn,genres,authors) 
                  SELECT book_id,title,image_url,num_pages,format,publisher,date,description,isbn,genres,authors 
                  FROM (SELECT books_genres.book_id, books_genres.title, books_genres.image_url, books_genres.num_pages, books_genres.format,
                        books_genres.publisher, books_genres.date, books_genres.description, books_genres.isbn, 
                        books_genres.genres, group_concat(author.name, ';') as authors 
                        FROM (SELECT book.*, genres.genres as genres 
                              FROM book JOIN genres ON book.book_id = genres.book_id) books_genres 
                        JOIN book_author ON books_genres.book_id = book_author.book_id 
                        JOIN author ON author.author_id = book_author.author_id 
                        GROUP BY books_genres.book_id) book_author_name;''')

      """
      - books_combined_series combines the book_series and series tables, concatenating all series of a book in a single tuple
      - updates book_combined, adding the concatenated series to the respective book
      """
      self.cursor.execute('''
                  UPDATE books_combined 
                  SET series = (
                        SELECT books_combined_series.series 
                        FROM (SELECT book_series.book_id, group_concat(series.series_name, ';') as series 
                              FROM book_series JOIN series ON series.series_id = book_series.series_id 
                              GROUP BY book_series.book_id) books_combined_series 
                        WHERE books_combined.book_id = books_combined_series.book_id
                        );''')
      
      self.connection.commit()
      print("Finished Combining Books")

        