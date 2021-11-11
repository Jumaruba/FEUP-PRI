import json
import csv
import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
RAW_PATH = CURRENT_PATH + "/../../data/raw/authors.json"
CLEAN_PATH = CURRENT_PATH + "/../../data/clean/authors.csv"

def clean_authors():
    authors_raw = open(RAW_PATH ,"r")
    authors_clean = open(CLEAN_PATH ,"w",  newline="\n", encoding="utf-8")
    writer = csv.writer(authors_clean)

    header = ["average_rating", "author_id", "name"]
    writer.writerow(header)

    for author_obj in authors_raw: 
        author = json.loads(author_obj)
        author.pop("text_reviews_count", None)
        author.pop("ratings_count", None)
        writer.writerow(list(author.values()))

    authors_raw.close()
    authors_clean.close() 


if __name__ == '__main__':
    clean_authors()