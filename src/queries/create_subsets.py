import pandas as pd

def query_romantic_tragedy():
    # This program must be executed in the filepath. 
    f_qrel = open("../data/queries/romantic_tragedy/related.txt", "r")
    f_norelated = open("../data/queries/romantic_tragedy/no_related.txt", "r")
    f_books = pd.read_csv("../data/search/books_ms2.csv")

    get_id = lambda line: int(line.split(",")[0])
    ids = list(map(get_id, f_norelated.readlines() + f_qrel.readlines()))

    subdataset = f_books[f_books.book_id.isin(ids)]
    subdataset.to_csv("../data/search/books_subdataset_1.csv", index=False) 


def query_world_war():
    f_qrel = open("../data/queries/world_war/related.txt", "r")  
    f_norelated = open("../data/queries/world_war/no_related.txt", "r")
    f_books = pd.read_csv("../data/search/books_ms2.csv")

    get_id = lambda line: int(line.split(",")[0])
    ids = list(map(get_id, f_norelated.readlines() + f_qrel.readlines()))

    subdataset = f_books[f_books.book_id.isin(ids)]
    subdataset.to_csv("../data/search/books_subdataset_2.csv", index=False) 

def query_world_war_nofilter():
    f_qrel = open("../data/queries/world_war_nofilter/related.txt", "r")  
    f_norelated = open("../data/queries/world_war_nofilter/no_related.txt", "r")
    f_books = pd.read_csv("../data/search/books_ms2.csv")

    get_id = lambda line: int(line.split(",")[0])
    ids = list(map(get_id, f_norelated.readlines() + f_qrel.readlines()))

    subdataset = f_books[f_books.book_id.isin(ids)]
    subdataset.to_csv("../data/search/books_subdataset_4.csv", index=False) 

def query_reviews():
    f_bad = open("../data/queries/reviews/bad.txt", "r")
    f_good = open("../data/queries/reviews/good.txt", "r")
    df_reviews = pd.read_csv("../data/search/reviews_ms2.csv")

    get_id = lambda line: int(line)
    ids = list(map(get_id, f_bad.readlines() + f_good.readlines()))

    subdataset = df_reviews[df_reviews.review_id.isin(ids)]
    subdataset.to_csv("../data/search/reviews_subdataset.csv", index=False)


def query_science(): 
    f_qrel = open("../data/queries/science/related.txt", "r")  
    f_norelated = open("../data/queries/science/no_related.txt", "r")
    f_books = pd.read_csv("../data/search/books_ms2.csv")

    get_id = lambda line: int(line.split(",")[0])
    ids = list(map(get_id, f_norelated.readlines() + f_qrel.readlines()))

    subdataset = f_books[f_books.book_id.isin(ids)]
    subdataset.to_csv("../data/search/books_subdataset_3.csv", index=False)  


if __name__ == '__main__': 
    # query_romantic_tragedy() 
    # query_world_war() 
    # query_world_war_nofilter() 
    query_reviews()
    # query_science()