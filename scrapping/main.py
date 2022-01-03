import sqlite3
import csv
import json

def get_authors(authors_arr):
    authors_names = []

    for author_obj in authors_arr:
        authors_names.append(int(author_obj["author_id"]))

    return authors_names

def clean_books():
    connection = sqlite3.connect(f'./data/books.db')
    cursor = connection.cursor()

    # -- Table book
    cursor.execute("DROP TABLE IF EXISTS book")
    cursor.execute('''CREATE TABLE book (
                        id INTEGER PRIMARY KEY,
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

    insert = []
    for index, books_obj in enumerate(books_raw): 
        if index % 1000000 == 0:
            print(index)
            connection.commit()
            
        book = json.loads(books_obj)
        if book['description'] and book['book_id'] and (book['language_code'] == 'eng' or book['language_code'] == 'pt' or book['language_code'] == 'en-US'):   
            day = 0 if not bool(book["publication_day"]) else int(book["publication_day"])
            month = 0 if not bool(book["publication_month"]) else int(book["publication_month"])
            year = 0 if not bool(book["publication_year"]) else int(book["publication_year"])
            
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

            insert.append([book_id, name, image_url, pagesNumber, publisher, date, language, str(author), description, isbn])
            
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

    cursor.execute("DROP TABLE IF EXISTS review") #" ", "review_id", "rating", "review_text", "date_added"
    cursor.execute('''CREATE TABLE review (
                        id VARCHAR(255) PRIMARY KEY,
                        book_id INTEGER,
                        rating REAL,
                        review_text VARCHAR(255),
                        date_added VARCHAR(255));
                    ''')

    reviews_raw = open('./data/raw/goodreads_reviews.json', 'r')

    #insert_records = "INSERT INTO review(id, book_id) VALUES(?, ?)"
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

def clean_genres():
    pass

if __name__ == '__main__':
    # Clean Database

    #clean_authors()
    clean_books()
    clean_reviews()
    clean_genres()