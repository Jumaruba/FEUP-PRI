import sqlite3
import csv
import json
from time import strptime
class ReviewsClean:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def clean(self, path):
        self.cursor.execute("DROP TABLE IF EXISTS review")
        self.cursor.execute('''CREATE TABLE review (
                            review_id VARCHAR(255) PRIMARY KEY,
                            book_id INTEGER,
                            rating REAL,
                            review_text VARCHAR(255),
                            date_added VARCHAR(255));''')

        insert = []
        reviews_raw = open(path, 'r')
        for review_obj in reviews_raw: 
            review = json.loads(review_obj)
            _, month, day, time, _, year = review['date_added'].split(' ')
            review['date_added'] = "%04d-%02d-%02d %s" % (int(year),int(strptime(month,'%b').tm_mon),int(day),time)
            review['review_text'] = review['review_text'].replace("(view spoiler)[", "")
            review['review_text'] = review['review_text'].replace("(hide spoiler)]", "") 
            if review['review_text'][0] != '\"':
                review['review_text'] = "\"" + review['review_text']
            if review['review_text'][-1] != '\"':
                review['review_text'] += "\""

            review_id = review['review_id']
            book_id = review['book_id']
            rating = review['rating']
            review_text = review['review_text']
            date_added = review['date_added']
            insert.append([review_id, book_id, rating, review_text, date_added])

        insert_records = "INSERT INTO review(review_id, book_id, rating, review_text, date_added) VALUES(?, ?, ?, ?, ?)"
        self.cursor.executemany(insert_records, insert)
        self.connection.commit()
        reviews_raw.close() 
