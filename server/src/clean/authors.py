import sqlite3
import csv
import json

class AuthorsClean:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def get_authors(self, authors_arr):
        authors_names = []
        for author_obj in authors_arr:
            authors_names.append(int(author_obj["author_id"]))

        return authors_names


    def clean(self, path):
        self.cursor.execute("DROP TABLE IF EXISTS author")
        self.cursor.execute('''CREATE TABLE author (
                            id INTEGER PRIMARY KEY,
                            name VARCHAR(255));''')

        insert = []
        authors_raw = open(path, 'r')
        for author_obj in authors_raw: 
            author = json.loads(author_obj)
            
            author_id = author['author_id']
            name = author['name']

            insert.append([author_id, name])
        authors_raw.close() 

        insert_records = "INSERT INTO author(id,name) VALUES(?, ?)"
        self.cursor.executemany(insert_records, insert)
        self.connection.commit()
        