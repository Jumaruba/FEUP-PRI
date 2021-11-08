import csv
import ast
from typing import List
import pandas as pd

last_id: int = 0              # Tracks the last id. 
genres_books: dict = {}       # This dictionary will map the books id's and the genres id's. {book_id: genre_id}

# Get Book Id List
books_clean = open("../../data/clean/books.csv", "r", encoding="utf-8", newline="\n")
books_df = pd.read_csv(books_clean)
BOOK_ID_LIST = books_df['book_id']


def add_genre_to_dict(writer, book_id: str, genre_names: List[str]) -> None: 
    """Adds the genres to the dictionary that maps genres and ids. 

    Args:
        genre_names (List[str]): [description]
    """
    global last_id 
    for name in genre_names:  
        if not name in genres_books:  
            last_id += 1
            genres_books[name] = last_id 

        writer.writerow([genres_books[name], book_id])

def create_genres_books_association():
    """ This function is responsible for creating the association table between genres and books. 
    The genres and books contains a many-to-many association. Thus it's necessary to create an association table.
    This table contais the columns genre_id and book_id. 
    """

    genres_clean = open("../../data/clean/genres.csv" ,"r") 
    genres_books_csv = open("../../data/processed/genres_books.csv" ,"w", encoding="utf-8", newline="\n") 
    writer = csv.writer(genres_books_csv)
    writer.writerow(["genre_id", "book_id"]) 

    csv_reader = csv.reader(genres_clean)       # Read the csv.
    next(csv_reader, None)                      # Skip reading the header.

    for book_id, genres_str in csv_reader:   
        genres = ast.literal_eval(genres_str)
        if int(book_id) in list(BOOK_ID_LIST):
            add_genre_to_dict(writer, book_id, genres)
            

    genres_books_csv.close()
    genres_clean.close() 

def overwrite_genres():
    """ This function is responsible for tranforming the genres.csv into a file with genres_id and genres_name.
    """

    genres_new = open("../../data/processed/genres.csv", "w", encoding="utf-8", newline="\n") 
    writer = csv.writer(genres_new)
    writer.writerow(["genre_id", "genre_name"]) 
    for genre_name, genre_id in genres_books.items():
        writer.writerow([genre_id, genre_name])
    genres_new.close() 


def delete_books_without_genre():
    """ This function is responsible for filtering the books in the books.csv.
    Books that don't have genres associated should not be contained at books.csv. 
    Thus they are filtered based on this criteria.
    """

    books_genres = open("../../data/processed/genres_books.csv", "r", encoding="utf-8", newline="\n") 
    books_genres_df = pd.read_csv(books_genres)
    book_ids = set(books_genres_df['book_id'])                              # Get's set of books_id
    
    books_processed_df = books_df[books_df['book_id'].isin(book_ids)]       # Filtering: removing books that doesn't have a genre associated. 
    
    books_processed_df.to_csv("../../data/processed/books.csv", index=False)


if __name__ == "__main__":
    create_genres_books_association()
    overwrite_genres()
    delete_books_without_genre()
    books_clean.close()








