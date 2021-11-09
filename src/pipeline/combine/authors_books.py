import csv
from io import TextIOWrapper
import pandas as pd 
import ast
from utils import *
import os 

# Argument positions in books.csv
BOOK_ID_POS = 16
AUTHORS_POS = 7


def create_books_authors_association() -> None:
    """
    Create Processed authors.
    """
    # Reading files. 
    books_csv = open(get_processed_path("books"), "r", encoding="utf-8", newline="\n")  
    authors_books_csv = open(get_processed_path("authors_books"), "w", encoding="utf-8", newline="\n") 
    books_csv_temp = open(get_processed_path("books_temp"),  "w", encoding="utf-8", newline="\n") 

    # Get writers
    writer = csv.writer(authors_books_csv)                  # Authors books relation.
    writer_temp = csv.writer(books_csv_temp)                # Remove books without authors and remove authors row.
    writer.writerow(["author_id", "book_id"]) 

    csv_reader = csv.reader(books_csv)                      # Get books as csv. 
    header_books = next(csv_reader, None)                   # Skip the header. 
    header_books.pop(AUTHORS_POS)                           # Remove AUTHORS column. 

    writer_temp.writerow(header_books)                      # Write reader. 

    for row in csv_reader:
        book_id = row[BOOK_ID_POS]
        authors = row[AUTHORS_POS] 
        authors_list = ast.literal_eval(authors)  

        # Removing books without authors.
        if bool(authors): 
            row.pop(AUTHORS_POS)
            writer_temp.writerow(row)

        # Build relation authors books. 
        for author in authors_list:
            writer.writerow([author, book_id])


    books_csv.close() 
    books_csv_temp.close() 
    authors_books_csv.close() 

    os.remove(get_processed_path("books"))
    os.rename(get_processed_path("books_temp"), get_processed_path("books"))   
                       

def delete_authors_without_books():
    """ Drop the authors in the authors.csv that don't have any book associated in the authors_books.csv.
    """
    books_csv = open(get_processed_path("books"), "r", encoding="utf-8", newline="\n")  
    books_df = pd.read_csv(books_csv)
    
    books_authors = open(get_processed_path("authors_books"), "r", encoding="utf-8", newline="\n") 
    books_authors_df = pd.read_csv(books_authors)
    book_ids = set(books_authors_df['book_id'])                            # Get's set of books_id
    
    books_processed_df = books_df[books_df['book_id'].isin(book_ids)]      # Filtering: removing authors that don't have any book associated. 
    
    books_processed_df.to_csv(get_processed_path, index=False)

    
if __name__ == '__main__':
    create_books_authors_association()
    delete_authors_without_books()