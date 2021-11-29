import csv
import pandas as pd 

def get_df(path_name):
    path = "./src/data/processed/" + path_name
    csv = open(path, "r", encoding="utf-8", newline="\n")  
    df = pd.read_csv(csv)
    csv.close()
    return df

books_df = get_df("books.csv")
genres_df = get_df("genres.csv")
genres_books_df = get_df("genres_books.csv")

df = (genres_books_df.merge(genres_df, left_on='genre_id', right_on='genre_id')
            .merge(books_df, left_on='book_id', right_on="book_id")
            .drop(['genre_id'], axis=1))

df.to_csv("./src/data/documents/books_docs.csv", index=False)
   