import json
import csv

def clean_genres():
    genres_raw = open("../../data/raw/genres.json" ,"r")
    genres_clean = open("../../data/clean/genres.csv" ,"w", newline="\n", encoding="utf-8")
    writer = csv.writer(genres_clean)

    header = ["book_id", "genres"]
    writer.writerow(header)

    for genres_obj in genres_raw: 
        genres = json.loads(genres_obj) 
        if bool(genres['genres']):  
            writer.writerow([genres["book_id"], genres["genres"]])

    genres_raw.close()
    genres_clean.close() 

if __name__ == '__main__':
    clean_genres()