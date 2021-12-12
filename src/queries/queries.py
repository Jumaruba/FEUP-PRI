import requests 
from metrics import generate_metrics

def query_exe(query, file, id_fieldname, path) -> None:
    results = requests.get(query).json()['response']['docs']
    relevant = list(map(lambda el: int(el.strip().split(",")[0]), open(file).readlines()))  
    generate_metrics(results, relevant, id_fieldname, path)      

# BOOKS ===========================
BOOKS_QRELS_FILEPATH = "../data/queries/books/related.txt"
# Without boost
QUERY_BOOKS_1 = "http://localhost:8983/solr/books_subset/select?q={!q.op=OR df=description}romantic%26tragedy&q=title:tragedy%26romantic&rows=10&wt=json"
# With boost
QUERY_BOOKS_2 = "http://localhost:8983/solr/books_subset/select?q=({!q.op=OR df=description}romantic%26tragedy)^=4&q=title:tragedy%26romantic&rows=10&wt=json" 
# With genre 
QUERY_BOOKS_3 = "http://localhost:8983/solr/books_subset/select?q=({!q.op=OR df=description}romantic%26tragedy)^=4&q=title:tragedy%26romantic&rows=10&wt=json" 

#query_exe(QUERY_BOOKS_1, BOOKS_QRELS_FILEPATH, "book_id","tematic/no_boost/") 
#query_exe(QUERY_BOOKS_2, BOOKS_QRELS_FILEPATH, "book_id","tematic/boost/")   
#query_exe(QUERY_BOOKS_3, BOOKS_QRELS_FILEPATH, "book_id","tematic/genres/")   

# REVIEWS ==========================  
REVIEWS_BAD_FILEPATH = "../data/queries/reviews/bad.txt" 
REVIEWS_GOOD_FILEPATH = "../data/queries/reviews/good.txt" 

bad_search_review = "hated this books"
# Bad.
QUERY_REVIEWS_1 = "http://localhost:8983/solr/reviews_subset/select?q={!q.op=OR df=review_text}hated this books&rows=20&wt=json"
# With rating and sorted by ascending. 
QUERY_REVIEWS_2 = "http://localhost:8983/solr/reviews_subset/select?q={!q.op=OR df=review_text}hated this books AND rating:[0 TO 3]&sort=field(rating, min) asc&rows=20&wt=json"

query_exe(QUERY_REVIEWS_1, REVIEWS_BAD_FILEPATH, "review_id", "pos_neg_reviews/synonyms/bad/")
# query_exe(QUERY_REVIEWS_2, REVIEWS_BAD_FILEPATH, "review_id", "pos_neg_reviews/rating/bad/")

good_search_review = "in love with this book"
# Good without boost.
QUERY_REVIEWS_3 = "http://localhost:8983/solr/reviews_subset/select?q={!q.op=OR df=review_text}in love with this book&rows=20&wt=json"
# With rating and sorted by descending. 
QUERY_REVIEWS_4 = "http://localhost:8983/solr/reviews_subset/select?q={!q.op=OR df=review_text}in love with this book AND rating:[3 TO *]&sort=field(rating, min) desc&rows=20&wt=json&rows=10&wt=json"


# GROUP AUTHORS ======================
QUERY_AUTHORS = 'http://localhost:8983/solr/reviews/select?rows=0&q=genres:romance&wt=json&json.facet={top:{ type:terms, limit: 10, field:authors, facet:{mean_rating:"avg(rating)", min_rating: "min(rating)", max_rating: "max(rating)"}, sort:{mean_rating: desc, min_rating: desc, max_rating: desc}}}'


