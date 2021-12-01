import csv
import os
import pandas as pd

def get_combine_path(name): 
    current_path =  os.path.dirname(os.path.abspath(__file__))
    return current_path + "/../data/combine/"+ name + ".csv"

def get_search_path(name):
    current_path =  os.path.dirname(os.path.abspath(__file__)) 
    return current_path + "/../data/search/"+ name + ".csv"

def get_df(path_name):
    csv = open(get_combine_path(path_name), "r", encoding="utf-8", newline="\n")  
    df = pd.read_csv(csv)
    csv.close()
    return df

books_df = get_df("books.csv")
genres_df = get_df("genres.csv")
genres_books_df = get_df("genres_books.csv")

df = (genres_books_df.merge(genres_df, left_on='genre_id', right_on='genre_id')
            .merge(books_df, left_on='book_id', right_on="book_id")
            .drop(['genre_id'], axis=1))

df.to_csv(get_search_path("books.csv"), index=False)
   