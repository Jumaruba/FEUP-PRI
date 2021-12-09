import pandas as pd

f_qrel = open("./romantic_tragedy.txt", "r")
f_norelated = open("./subdataset.txt", "r")
f_books = pd.read_csv("../../search/books.csv")

get_id = lambda line: int(line.split(",")[0])
ids = list(map(get_id, f_norelated.readlines() + f_qrel.readlines()))
print(ids)

subdataset = f_books[f_books.book_id.isin(ids)]
subdataset.to_csv("../../search/subdataset.csv", index=False)