import sqlite3
import csv
import json

class GenresClean:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def get_names(self, group_names):
        arr = group_names.split(",")
        arr = list(map(str.strip, arr))
        return arr 
        
    def get_genres(self, genres_groups):
        genres = []
        for genres_group in genres_groups: 
            genres += self.get_names(genres_group)
        return genres 

    def clean(self, path):
        self.cursor.execute("DROP TABLE IF EXISTS genres") 
        self.cursor.execute('''CREATE TABLE genres (
                            book_id PRIMARY KEY,
                            genres VARCHAR(255));''')

        insert = []
        genres_raw = open(path, 'r')
        for genres_obj in genres_raw: 
            genres = json.loads(genres_obj)

            if bool(genres['genres']):  
                genres_arr = self.get_genres(list(genres["genres"].keys()))
                insert.append([genres['book_id'], str(genres_arr)])           
        genres_raw.close()
        
        insert_records = "INSERT INTO genres(book_id, genres) VALUES(?, ?)"
        self.cursor.executemany(insert_records, insert)
        self.connection.commit()
        


    