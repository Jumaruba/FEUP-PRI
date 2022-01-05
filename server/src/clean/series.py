import sqlite3
import csv
import json

class SeriesClean:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def clean(self, path):
        self.cursor.execute("DROP TABLE IF EXISTS series") 
        self.cursor.execute('''CREATE TABLE series (
                            series_id PRIMARY KEY,
                            series_name VARCHAR(255));''')

        insert = []
        series_raw = open(path, 'r')
        for series_obj in series_raw: 
            series = json.loads(series_obj)
            insert.append([int(series['series_id']), series['title']])           
        series_raw.close()
        
        insert_records = "INSERT INTO series(series_id, series_name) VALUES(?, ?)"
        self.cursor.executemany(insert_records, insert)
        self.connection.commit()
        


    