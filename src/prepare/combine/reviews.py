from utils import *
import pandas as pd
import os 

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

def delete_reviews_without_book():
    """ Drop the reviews in the reviews.csv that don't have any book associated in the books.csv.
    """
    books_csv = open(get_processed_path(CURRENT_PATH,"books"), "r", encoding="utf-8", newline="\n")  
    books_df = pd.read_csv(books_csv)
    books_csv.close()
    book_ids = books_df['book_id']

    reviews_csv = open(get_clean_path(CURRENT_PATH,"reviews"), "r", encoding="utf-8", newline="\n")  
    reviews_df = pd.read_csv(reviews_csv)
    reviews_csv.close()

    # Filtering: removing reviews that don't have any book associated. 
    reviews_processed_df = reviews_df[reviews_df['book_id'].isin(book_ids)] 
    reviews_processed_df.to_csv(get_processed_path(CURRENT_PATH,"reviews"), index=False)


if __name__ == '__main__':
    delete_reviews_without_book()