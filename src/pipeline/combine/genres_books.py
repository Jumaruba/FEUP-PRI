import json
import csv
from typing import List 

last_id: int = 0              # Tracks the last id. 
genres: dict = {}             # This dictionary will map the genres and id's. {genre_name: id}
genres_books: dict = {}       # This dictionary will map the books id's and the genres id's. {book_id: genre_id}


def get_names(group_names: str) -> List[str]:
    """In the json some genres names may be separated by ",". 
    Thus to extract the real names, it's important to treat these cases.

    Args:
        group_names (str): String with genres separated by space.

    Returns:
        List[str]: List of genres. 
    """
    arr = group_names.split(",")
    arr = list(map(str.strip, arr))

    return arr 


def add_genre_to_dict(genre_names: List[str]) -> None: 
    """Adds the genres to the dictionary that maps genres and ids. 

    Args:
        genre_names (List[str]): [description]
    """
    global last_id 
    for name in genre_names:  
        if not name in genres.keys():  
            last_id += 1
            genres[name] = last_id



genres_clean = open("../../data/clean/genres.csv" ,"r") 
books_clean = open("../../data/clean/books.json" ,"r")  
genres_books_csv = open("../../data/clean/genres_books.csv" ,"w", encoding="utf-8", newline="\n") 
writer = csv.writer(genres_books_csv)
writer.writerow(["genre_id", "book_id"]) 

csv_reader = csv.reader(genres_clean)       # Read the csv.
next(csv_reader, None)                      # Skip reading the header.

for book_id, genres_dict in csv_reader:   
    genres_dict = genres_dict.replace("\'", "\"") 
    names = json.loads(genres_dict) 

    for group_names,_ in names.items(): 
        names = get_names(group_names) 
        add_genre_to_dict(names) 
        for name in names:
            writer.writerow([genres[name], book_id])


genres_books_csv.close()
genres_clean.close() 