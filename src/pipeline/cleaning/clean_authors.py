import json
import csv

def clean_authors():
    authors_raw = open("../../data/raw/authors.json" ,"r")
    authors_clean = open("../../data/clean/authors.csv" ,"w",  newline="\n", encoding="utf-8")
    writer = csv.writer(authors_clean)

    header = ["average_rating", "author_id", "name"]
    writer.writerow(header)

    for author_obj in authors_raw: 
        author = json.loads(author_obj)
        author.pop("text_reviews_count", None)
        author.pop("ratings_count", None)
        writer.writerow(author.values())

    authors_raw.close()
    authors_clean.close() 


if __name__ == '__main__':
    clean_authors()