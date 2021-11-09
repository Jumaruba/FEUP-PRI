import csv
from io import TextIOWrapper
import pandas as pd 
import ast
import utils
import os 

# Argument positions in books.csv
BOOK_ID_POS = 16
AUTHORS_POS = 7
books_path = utils.get_processed_path("books")
authors_books_path = utils.get_processed_path("authors_books")

def create_books_authors_association() -> None:
    """
    Create Processed authors
    """
    # Reading files. 
    books_csv = open(books_path, "r", encoding="utf-8", newline="\n")  
    authors_books_csv = open(authors_books_path, "w", encoding="utf-8", newline="\n") 
    books_csv_temp = open(utils.get_processed_path("books_temp"),  "w", encoding="utf-8", newline="\n")
    writer = csv.writer(authors_books_csv)   
    writer.writerow(["author_id", "book_id"]) 

    writer_temp = csv.writer(books_csv_temp)

    csv_reader = csv.reader(books_csv)                      # Read the books csv
    header_books = next(csv_reader, None)                   # Skip the header.  
    header_books.pop(AUTHORS_POS) 

    writer_temp.writerow(header_books)

    for row in csv_reader:
        book_id = row[BOOK_ID_POS]
        authors = row[AUTHORS_POS] 
        authors_list = ast.literal_eval(authors) 

        if bool(authors): 
            row.pop(AUTHORS_POS)
            writer_temp.writerow(row)

        for author in authors_list:
            writer.writerow([author, book_id])


    books_csv.close() 
    books_csv_temp.close()
    os.remove(utils.get_processed_path("books"))
    os.rename(utils.get_processed_path("books_temp"), utils.get_processed_path("books"))   
    authors_books_csv.close()
                       

def delete_authors_without_books():
    """ Drop the authors in the authors.csv that don't have any book associated in the authors_books.csv.
    """
    books_csv = open(books_path, "r", encoding="utf-8", newline="\n")  
    books_df = pd.read_csv(books_csv)
    
    books_authors = open(utils.get_processed_path("authors_books"), "r", encoding="utf-8", newline="\n") 
    books_authors_df = pd.read_csv(books_authors)
    book_ids = set(books_authors_df['book_id'])                            # Get's set of books_id
    
    books_processed_df = books_df[books_df['book_id'].isin(book_ids)]      # Filtering: removing authors that don't have any book associated. 
    
    books_processed_df.to_csv(books_path, index=False)

    
if __name__ == '__main__':
    create_books_authors_association()
    delete_authors_without_books()