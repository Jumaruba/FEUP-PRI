import csv
import os
import pandas as pd

def get_combine_path(name): 
    current_path =  os.path.dirname(os.path.abspath(__file__))
    return current_path + "/../data/combine/"+ name + ".csv"

def get_search_path(name):
    current_path =  os.path.dirname(os.path.abspath(__file__)) 
    return current_path + "/../data/search/"+ name + ".csv"

def reviews_doc():

    books_df = pd.read_csv(get_combine_path("books"), usecols=['book_id', 'title'])
    reviews_df = pd.read_csv(get_combine_path("reviews"))

    # TODO - check if it really makes sense to join the genres here

    reviews_doc_df = pd.merge(reviews_df, books_df, on="book_id", how="left")

    reviews_doc_df.drop(columns="review_id", inplace=True)
    
    reviews_doc_df.to_csv(get_search_path("reviews"))

if __name__ == '__main__':
    reviews_doc()

