import csv 
from utils import * 
import pandas as pd 

def combine_series():
    series = open(get_clean_path("series"), "r", encoding="utf-8", newline="\n")  
    df_series = pd.read_csv()
    series.close()

    books = open(get_processed_path("books"), "r", encoding="utf-8", newline="\n") 
    df_books = pd.read_csv(books)
    books_ids = set(df_books['book_id'])
    books.close()

    
    combined_series = open(get_processed_path("series"),"w", encoding="utf-8", newline="\n")

if __name__ == '__main__':
    combine_series()
