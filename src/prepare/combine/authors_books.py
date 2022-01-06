import csv
import pandas as pd 
import ast
from utils import *
import os 

# Argument positions in books.csv
BOOK_ID_POS = -3
AUTHORS_POS = 7
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def create_books_authors_association() -> None:
    """
    Create many to many relation between books and authors.
    This new relation contais the columns author_id and book_id. 
    """
    # Reading files. 
    books_csv = open(get_processed_path(CURRENT_PATH,"books"), "r", encoding="utf-8", newline="\n")  
    authors_books_csv = open(get_processed_path(CURRENT_PATH,"authors_books"), "w", encoding="utf-8", newline="\n") 
    books_csv_temp = open(get_processed_path(CURRENT_PATH,"books_temp"),  "w", encoding="utf-8", newline="\n") 

    # Get writers
    writer = csv.writer(authors_books_csv)                  # Authors books relation.
    writer_temp = csv.writer(books_csv_temp)                # Remove Authors row.
    writer.writerow(["author_id", "book_id"]) 

    csv_reader = csv.reader(books_csv)                      # Get books as csv. 
    header_books = next(csv_reader, None)                   # Skip the header. 
    header_books.pop(AUTHORS_POS)                           # Remove AUTHORS column. 

    writer_temp.writerow(header_books)                      # Write reader. 

    for row in csv_reader:
        book_id = row[BOOK_ID_POS]
        authors = row[AUTHORS_POS] 
        authors_list = ast.literal_eval(authors)  

        # Removing authors column
        row.pop(AUTHORS_POS)
        writer_temp.writerow(row)

        # Build relation authors books. 
        for author in authors_list:
            writer.writerow([author, book_id])


    books_csv.close() 
    books_csv_temp.close() 
    authors_books_csv.close() 

    os.remove(get_processed_path(CURRENT_PATH,"books"))
    os.rename(get_processed_path(CURRENT_PATH,"books_temp"), get_processed_path(CURRENT_PATH,"books"))   
                       
def delete_authors_without_books():
    """ Drop the authors in the authors.csv that don't have any book associated in the authors_books.csv.
    """
    books_authors_csv = open(get_processed_path(CURRENT_PATH,"authors_books"), "r", encoding="utf-8", newline="\n")  
    books_authors_df = pd.read_csv(books_authors_csv)
    books_authors_csv.close()
    author_ids = set(books_authors_df['author_id'])                       
    
    authors_csv = open(get_clean_path(CURRENT_PATH,"authors"), "r", encoding="utf-8", newline="\n")
    authors_df = pd.read_csv(authors_csv)
    authors_csv.close()
    
    # Filtering: removing authors that don't have any book associated. 
    authors_processed_df = authors_df[authors_df['author_id'].isin(author_ids)] 
    authors_processed_df.to_csv(get_processed_path(CURRENT_PATH,"authors"), index=False)

    
if __name__ == '__main__':
    create_books_authors_association()
    delete_authors_without_books()