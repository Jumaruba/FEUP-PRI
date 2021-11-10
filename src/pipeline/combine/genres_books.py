import csv
import ast
from typing import List
import utils
import pandas as pd

last_id: int = 0              # Tracks the last id. 
genres_books: dict = {}       # This dictionary will map book id's and genre id's. {book_id: genre_id}


books_clean_path = utils.get_clean_path("books")
books_processed_path = utils.get_processed_path("books")
genres_clean_path = utils.get_clean_path("genres")
genres_books_path = utils.get_processed_path("genres_books")
genres_processed_path = utils.get_processed_path("genres")


def add_genre_to_dict(writer, book_id: str, genre_names: List[str]) -> None: 
    """Adds the genres to the dictionary that maps genres and ids. 
    """
    global last_id, genres_books
    for name in genre_names:  
        if not name in genres_books:  
            last_id += 1
            genres_books[name] = last_id 

        writer.writerow([genres_books[name], book_id])

def create_genres_books_association():
    """ Creating many to many realtion between genres and books. 
    This new relation contais the columns genre_id and book_id. 
    """
    books_clean = open(books_clean_path, "r", encoding="utf-8", newline="\n")
    books_df = pd.read_csv(books_clean)
    books_clean.close()
    book_id_list = books_df['book_id']

    genres_clean = open(genres_clean_path,"r")  
    genres_books_csv = open(genres_books_path,"w", encoding="utf-8", newline="\n") 
    writer = csv.writer(genres_books_csv)
    writer.writerow(["genre_id", "book_id"]) 

    csv_reader = csv.reader(genres_clean)       # Read the csv.
    next(csv_reader, None)                      # Skip reading the header.

    for book_id, genres_str in csv_reader:   
        genres = ast.literal_eval(genres_str)
        # Keep only the books that are both in genres.csv and books.csv
        if int(book_id) in list(book_id_list):
            add_genre_to_dict(writer, book_id, genres)
            
    genres_books_csv.close()
    genres_clean.close() 

def create_genres():
    """ Tranform the genres.csv into a file with genres_id and genres_name.
    """

    genres_new = open(genres_processed_path, "w", encoding="utf-8", newline="\n") 
    writer = csv.writer(genres_new)
    writer.writerow(["genre_id", "genre_name"]) 
    for genre_name, genre_id in genres_books.items():
        writer.writerow([genre_id, genre_name])
    genres_new.close() 

def delete_books_without_genre():
    """ Drop the books in books.csv that don't have genres associated in genres_books.csv.
    """
    books_clean = open(books_clean_path, "r", encoding="utf-8", newline="\n")
    books_df = pd.read_csv(books_clean)
    books_clean.close()

    books_genres = open(utils.get_processed_path("genres_books"), "r", encoding="utf-8", newline="\n") 
    books_genres_df = pd.read_csv(books_genres)
    book_ids = set(books_genres_df['book_id'])                             
    
    # Filtering: removing books that don't have a genre associated. 
    books_processed_df = books_df[books_df['book_id'].isin(book_ids)]
    books_processed_df.to_csv(books_processed_path, index=False)

if __name__ == "__main__":
    create_genres_books_association()
    create_genres()
    delete_books_without_genre()








