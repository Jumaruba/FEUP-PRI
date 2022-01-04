import sqlite3
import csv
import json

from collections import defaultdict

def get_authors(authors_arr):
    authors_names = []

    for author_obj in authors_arr:
        authors_names.append(int(author_obj["author_id"]))

    return authors_names

def recentBook(bookList):
    older = bookList[0]
    if(len(bookList) != 1): 
        for book in bookList:  
            if older[5] < book[5]: older = book
    return older

def clean_books():
    connection = sqlite3.connect(f'./data/books.db')
    cursor = connection.cursor()

    # -- Table book
    cursor.execute("DROP TABLE IF EXISTS book")
    cursor.execute('''CREATE TABLE book (
                        id INTEGER,
                        name VARCHAR(255),
                        image_url VARCHAR(255),
                        pagesNumber VARCHAR(255),
                        publisher VARCHAR(255),
                        date VARCHAR(255),
                        language VARCHAR(255),
                        author VARCHAR(255),
                        description VARCHAR(255),
                        isbn INTEGER);
                    ''')

    books_raw = open('./data/raw/goodreads_books.json', "r")
    insert_records = "INSERT INTO book(id,name,image_url,pagesNumber,publisher,date,language,author,description,isbn) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    book_insert = defaultdict(list)
    for index, books_obj in enumerate(books_raw): 
        book = json.loads(books_obj)
        if book['description'] and book['book_id'] and (book['language_code'] == 'eng' or book['language_code'] == 'pt' or book['language_code'] == 'en-US'):   
            day = 1 if not bool(book["publication_day"]) else int(book["publication_day"])
            month = 1 if not bool(book["publication_month"]) else int(book["publication_month"])
            
            if not bool(book["publication_year"]):
                continue
            else: 
                year = int(book["publication_year"])
            
            book_id = book['book_id']
            name = book['title']
            image_url = book['image_url']
            pagesNumber = int(book['num_pages'] if book['num_pages'] != '' else 0) 
            publisher = book['publisher']
            date = "%04d-%02d-%02d" % (year,month,day)
            language  = book['language_code']
            author = get_authors(book["authors"])
            description = book['description']
            isbn = book['isbn']

            book_insert[name].append([book_id, name, image_url, pagesNumber, publisher, date, language, author, description, isbn])
    
    insert = []
    for key in book_insert:
        new_book = recentBook(book_insert[key])
        authors = new_book[7]
        for author in authors:
            insert.append([new_book[0], new_book[1], new_book[2], new_book[3], new_book[4], new_book[5], new_book[6], author, new_book[8], new_book[9]])
        

    cursor.executemany(insert_records, insert)
    connection.commit()
    connection.close()
    books_raw.close()

def clean_authors():
    connection = sqlite3.connect(f'./data/books.db')
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS author")
    cursor.execute('''CREATE TABLE author (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR(255));
                    ''')

    authors_raw = open('./data/raw/goodreads_authors.json', 'r')

    insert_records = "INSERT INTO author(id,name) VALUES(?, ?)"
    insert = []
    for author_obj in authors_raw: 
        author = json.loads(author_obj)
        
        author_id = author['author_id']
        name = author['name']

        insert.append([author_id, name])

    cursor.executemany(insert_records, insert)
    connection.commit()
    connection.close()
    authors_raw.close() 

def clean_reviews():
    connection = sqlite3.connect(f'./data/books.db')
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS review")
    cursor.execute('''CREATE TABLE review (
                        id VARCHAR(255) PRIMARY KEY,
                        book_id INTEGER,
                        rating REAL,
                        review_text VARCHAR(255),
                        date_added VARCHAR(255));
                    ''')

    reviews_raw = open('./data/raw/goodreads_reviews.json', 'r')

    insert_records = "INSERT INTO review(id, book_id, rating, review_text, date_added) VALUES(?, ?, ?, ?, ?)"
    insert = []
    for review_obj in reviews_raw: 
        review = json.loads(review_obj)
        
        review_id = review['review_id']
        book_id = review['book_id']
        rating = review['rating']
        review_text = review['review_text']
        date_added = review['date_added']
        insert.append([review_id, book_id, rating, review_text, date_added])

    cursor.executemany(insert_records, insert)
    connection.commit()
    connection.close()
    reviews_raw.close() 

def get_genres(genres_groups):
    genres = []
    for genres_group in genres_groups: 
        genres += get_names(genres_group)
    return genres 

def get_names(group_names: str):
    arr = group_names.split(",")
    arr = list(map(str.strip, arr))
    return arr 


def clean_genres():
    connection = sqlite3.connect(f'./data/books.db')
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS genres") 
    cursor.execute('''CREATE TABLE genres (
                        book_id PRIMARY KEY,
                        genres VARCHAR(255));
                    ''')

    genres_raw = open('./data/raw/goodreads_genres.json', 'r')
    
    insert_records = "INSERT INTO genres(book_id, genres) VALUES(?, ?)"
    insert = []
    for genres_obj in genres_raw: 
        genres = json.loads(genres_obj)

        if bool(genres['genres']):  
            genres_arr = get_genres(list(genres["genres"].keys()))
            insert.append([genres['book_id'], str(genres_arr)])
    
    cursor.executemany(insert_records, insert)
    connection.commit()
    connection.close()
    genres_raw.close()

def clean_database():
    # Clean the database
    clean_authors()
    print("Finished Authors Cleaning")

    clean_books()
    print("Finished Books Cleaning")

    clean_reviews()
    print("Finished Reviews Cleaning")

    clean_genres()
    print("Finished Genres Cleaning")

def combine_books_genres():
    connection = sqlite3.connect(f'./data/books.db')
    cursor = connection.cursor()

    cursor.execute("DROP VIEW IF EXISTS books_genres") 
    cursor.execute('''CREATE VIEW books_genres AS
                        SELECT book.*, genres.genres as genres
                        FROM book
                        JOIN genres ON book.id = genres.book_id;''')

def combine_books_authors():
    connection = sqlite3.connect(f'./data/books.db')
    cursor = connection.cursor()

    cursor.execute("DROP VIEW IF EXISTS books_author_name") 
    cursor.execute('''CREATE VIEW books_author_name AS
                        SELECT books_genres.id, books_genres.name, books_genres.image_url, books_genres.pagesNumber, books_genres.publisher, books_genres.date, books_genres.language, books_genres.description, books_genres.isbn, books_genres.genres, author.name as author
                        FROM books_genres
                        JOIN author ON books_genres.author = author.id;''')

    cursor.execute("DROP TABLE IF EXISTS books_combined") 
    cursor.execute('''CREATE TABLE books_combined AS
                        SELECT id, name, image_url, pagesNumber, publisher, date, language, description, isbn, genres, group_concat(author, ';') as author
                        FROM books_author_name
                        GROUP BY id, name, image_url, pagesNumber, publisher, date, language, description, isbn;''')

    cursor.execute("DROP VIEW IF EXISTS books_genres") 
    cursor.execute("DROP VIEW IF EXISTS books_author_name") 

def dump():
    connection = sqlite3.connect(f'./data/books.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books_combined") 
    rows = cursor.fetchall()
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == '__main__':
    # clean_database()
    # print("Finished Cleaning")

    # combine_books_genres()
    # combine_books_authors()
    # print("Finished Combine")

    print("Start writing as csv")
    dump()
    print("Finished")