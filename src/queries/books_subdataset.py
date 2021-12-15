import pandas as pd

# This program must be executed in the filepath. 
f_qrel = open("../data/queries/books/related.txt", "r")
f_norelated = open("../data/queries/books/no_related.txt", "r")
f_books = pd.read_csv("../data/search/books.csv")

get_id = lambda line: int(line.split(",")[0])
ids = list(map(get_id, f_norelated.readlines() + f_qrel.readlines()))

subdataset = f_books[f_books.book_id.isin(ids)]
subdataset.to_csv("../data/search/books_subdataset.csv", index=False)