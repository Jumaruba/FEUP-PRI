import requests 
import tematic 


def query_exe(query, file, id_fieldname) -> None:
    results = requests.get(query).json()['response']['docs']
    relevant = list(map(lambda el: int(el.strip().split(",")[0]), open(file).readlines()))  
    tematic.generate_metrics(results, relevant, id_fieldname)      

# BOOKS ===========================
BOOKS_QRELS_FILEPATH = "../data/queries/books/related.txt"
# Without boost
QUERY_BOOKS_1 = "http://localhost:8983/solr/books_subset/select?q={!q.op=OR df=description}romantic%26tragedy&q=title:tragedy%26romantic&rows=10&wt=json"
# With boost
QUERY_BOOKS_2 = "http://localhost:8983/solr/books_subset/select?q=({!q.op=OR df=description}romantic%26tragedy)^=4&q=title:tragedy%26romantic&rows=10&wt=json" 

#query_exe(QUERY_BOOKS_1, BOOKS_QRELS_FILEPATH, "book_id") 
#query_exe(QUERY_BOOKS_2, BOOKS_QRELS_FILEPATH, "book_id")   

# REVIEWS ==========================  
REVIEWS_BAD_FILEPATH = "../data/queries/reviews/bad.txt" 
REVIEWS_GOOD_FILEPATH = "../data/queries/reviews/good.txt" 

# Bad without boost
QUERY_REVIEWS_1 = "http://localhost:8983/solr/reviews_subset/select?q={!q.op=OR df=review_text}hating this book&rows=10&wt=json"
# Bad with boost
QUERY_REVIEWS_2 = "http://localhost:8983/solr/reviews_subset/select?q=({!q.op=OR df=review_text}romantic%26tragedy)^=4&q=title:tragedy%26romantic&rows=10&wt=json" 

query_exe(QUERY_REVIEWS_1, REVIEWS_BAD_FILEPATH, "review_id")
