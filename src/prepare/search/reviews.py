import csv
import os
import pandas as pd
from utils import *

def reviews_doc():
    books_df = pd.read_csv(get_search_path("books"), usecols=['book_id', 'title', 'genres', 'authors'])
    reviews_df = pd.read_csv(get_combine_path("reviews"))

    reviews_doc_df = pd.merge(reviews_df, books_df, on="book_id", how="left")

    reviews_doc_df.drop(columns="review_id", inplace=True)

    reviews_doc_df.index.names = ['review_id']
    
    reviews_doc_df.to_csv(get_search_path("reviews_ms2"))

if __name__ == '__main__':
    reviews_doc()

