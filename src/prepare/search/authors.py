import csv
import os
import pandas as pd
from utils import *

# Get files. 
authors_books = pd.read_csv(get_combine_path("authors_books"))
authors = pd.read_csv(get_combine_path("authors"))
books = pd.read_csv(get_combine_path("books"))


def get_books_name(book_id):
    return books[books['book_id'] == book_id]['title'].values[0]

def get_authors_name(author_id):
    return authors[authors['author_id'] == author_id]['name'].values[0]

def get_authors_books(author_id):
    # Gets all the books for one author. 
    book_ids = authors_books[authors_books['author_id'] == author_id]['book_id'].tolist()
    return ";".join(list(map(get_books_name, book_ids)))

authors_id = authors_books['author_id'].unique()    # Get the authors id.
df_output  = pd.DataFrame()

for author_id in authors_id:
    books_name = get_authors_books(author_id)
    author_name = get_authors_name(author_id)
    df_output = df_output.append({'author_name': author_name, 'books_name': books_name}, ignore_index=True)

df_output.to_csv(get_search_path("authors"), index=False)




