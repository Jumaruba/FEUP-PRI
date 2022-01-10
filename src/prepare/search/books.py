import csv
import os
import pandas as pd
from utils import * 


def get_df(path_name):
    csv = open(get_combine_path(path_name), "r", encoding="utf-8", newline="\n")  
    df = pd.read_csv(csv)
    csv.close()
    return df

books_df = get_df("books")
genres_df = get_df("genres")
genres_books_df = get_df("genres_books") 
authors_df = get_df("authors")
authors_books_df = get_df("authors_books")
output_df = pd.DataFrame()


def get_genre_name(genre_id):
    return genres_df[genres_df['genre_id'] == genre_id]['genre_name'].values[0]

def get_genres_books(genres_books_df, book_id):
    # Gets all the genres for one book. 
    genre_ids = genres_books_df[genres_books_df['book_id'] == book_id]['genre_id'].tolist()
    return  ";".join(list(map(get_genre_name, genre_ids)))


def get_author_name(author_id):
    return authors_df[authors_df['author_id'] == author_id]['name'].values[0]

def get_authors_books(authors_books_df, book_id):
    # Gets all the authors of one book. 
    author_ids = authors_books_df[authors_books_df['book_id'] == book_id]['author_id'].tolist()
    return  ";".join(list(map(get_author_name, author_ids)))


books_ids = books_df['book_id'].unique()
for book_id in books_ids:
    genres = get_genres_books(genres_books_df, book_id)
    authors = get_authors_books(authors_books_df, book_id)
    output_df = output_df.append({'book_id': int(book_id), 'genres': genres, 'authors': authors}, ignore_index=True)

books_df = books_df.merge(output_df, on ="book_id", how="left")
books_df.to_csv(get_search_path("books_ms2"), index=False)
   