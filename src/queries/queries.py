import requests 
from metrics import generate_metrics

def query_exe(query, file, id_fieldname, path) -> None:
    results = requests.get(query).json()['response']['docs']
    relevant = list(map(lambda el: int(el.strip().split(",")[0]), open(file).readlines()))  
    generate_metrics(results, relevant, id_fieldname, path)      


def query_romantic_tragedy(): 
    """
    Query that searches books about romatic tragedies. 
    The queries shows how the distance between and boost can improve the query. 
    - The first query is a simple query without boost. 
    - The second one contains words distance and boost.  
    """

    BOOKS_QRELS_FILEPATH_1 = "../data/queries/romantic_tragedy/related.txt"
    # Without boost
    QUERY_BOOKS_1 = "http://localhost:8983/solr/books_subset_1/select?q=description:romantic%26tragedy&rows=8&wt=json"
    # With boost
    QUERY_BOOKS_2 = "http://localhost:8983/solr/books_subset_1/query?q=description:%20romantic%20tragedy&q.op=OR&defType=edismax&indent=true&qf=description%5E2&ps=4&rows=8"

    query_exe(QUERY_BOOKS_1, BOOKS_QRELS_FILEPATH_1, "book_id","romantic_tragedy/no_boost/") 
    query_exe(QUERY_BOOKS_2, BOOKS_QRELS_FILEPATH_1, "book_id","romantic_tragedy/boost/")   


def query_world_war():
    """
    Query taht searches about the world wars.
    - In the first query we are forcing that the words "world" and "war" appear in the phrase but not necessarily in sequence. Of course, a priority is given if they 
    are togheter. 
    - In the second query we're forcing an exact match in world war phrase. 
    """  
    BOOKS_QRELS_FILEPATH_2 = "../data/queries/world_war/related.txt"

    # Without boost.
    QUERY_BOOKS_3 = "http://localhost:8983/solr/books_subset_2/query?q=description:\"world war\"&rows=10"
    # With boost. 
    QUERY_BOOKS_4 = "http://localhost:8983/solr/books_subset_2/select?defType=edismax&q=+world +war&qf=description^1&rows=10&ps=2"

    query_exe(QUERY_BOOKS_3, BOOKS_QRELS_FILEPATH_2, "book_id", "world_war/no_boost/") 
    query_exe(QUERY_BOOKS_4, BOOKS_QRELS_FILEPATH_2, "book_id", "world_war/boost/")

def query_world_war_nofilter():
    """
    Query taht searches about the world wars.
    - In the first query we are forcing that the words "world" and "war" appear in the phrase but not necessarily in sequence. Of course, a priority is given if they 
    are togheter. 
    - In the second query we're forcing an exact match in world war phrase. 
    """  
    BOOKS_QRELS_FILEPATH_3 = "../data/queries/world_war_nofilter/related.txt"

    # Without boost.
    QUERY_BOOKS_5 = "http://localhost:8983/solr/books_subset_4/query?q=description:\"world war\"&rows=10"
    # With boost. 
    QUERY_BOOKS_6 = "http://localhost:8983/solr/books_subset_4/select?defType=edismax&q=+world +war&qf=description^1&rows=10&ps=2"

    query_exe(QUERY_BOOKS_5, BOOKS_QRELS_FILEPATH_3, "book_id", "world_war_nofilter/no_boost/") 
    query_exe(QUERY_BOOKS_6, BOOKS_QRELS_FILEPATH_3, "book_id", "world_war_nofilter/boost/")


def query_reviews():
    REVIEWS_BAD_FILEPATH = "../data/queries/reviews/bad.txt" 
    REVIEWS_GOOD_FILEPATH = "../data/queries/reviews/good.txt" 

    bad_search_review = "hated this books"
    # Bad.
    QUERY_REVIEWS_1 = "http://localhost:8983/solr/reviews_subset/select?q={!q.op=OR df=review_text}hated this books&rows=10&wt=json"
    # With rating and sorted by ascending. 
    QUERY_REVIEWS_2 = "http://localhost:8983/solr/reviews_subset/select?q={!q.op=OR df=review_text}hated this books AND rating:[0 TO 3.5]&sort=field(rating, min) asc&rows=20&wt=json"

    query_exe(QUERY_REVIEWS_1, REVIEWS_BAD_FILEPATH, "review_id", "pos_neg_reviews/synonyms/bad/")
    query_exe(QUERY_REVIEWS_2, REVIEWS_BAD_FILEPATH, "review_id", "pos_neg_reviews/rating/bad/") 

    """
    good_search_review = "in love with this book"
    # Good without boost.
    QUERY_REVIEWS_3 = "http://localhost:8983/solr/reviews_subset/select?q={!q.op=OR df=review_text}in love with this book&rows=10&wt=json"
    # With rating and sorted by descending. 
    QUERY_REVIEWS_4 = "http://localhost:8983/solr/reviews_subset/select?q={!q.op=OR df=review_text}in love with this book AND rating:[3 TO *]&sort=field(rating, min) desc&rows=20&wt=json&rows=10&wt=json"
    """

def group_authors():
    QUERY_AUTHORS = 'http://localhost:8983/solr/reviews/select?rows=0&q=genres:romance&wt=json&json.facet={top:{ type:terms, limit: 10, field:authors, facet:{mean_rating:"avg(rating)", min_rating: "min(rating)", max_rating: "max(rating)"}, sort:{mean_rating: desc, min_rating: desc, max_rating: desc}}}'

def query_science():
    """
    Query that searchs for most recent science books. 

    """ 
    QUERY_SCIENCE_PATH = "../data/queries/science/related.txt" 
    # Without boost 
    #defType=edismax&bf=recip(ms(NOW,book_date),3.16e-11,1,1)
    QUERY_SCIENCE_1 = "http://localhost:8983/solr/books_subset_3/select?q=description:science%20title:science&q.op=AND"

    # With boost 
    #  tiramos livros do gênero ficção dar boost do genero non-fiction
    # genres:-"historical fiction"
    QUERY_SCIENCE_2 = "http://localhost:8983/solr/books_subset_3/select?q.op=AND&defType=edismax&q=science -genres:fiction -genres:\"historical-fiction\"&bq=genres:\"non-fiction\"^4&qf=description title" 

    query_exe(QUERY_SCIENCE_1, QUERY_SCIENCE_PATH, "book_id", "science/no_boost/")
    query_exe(QUERY_SCIENCE_2, QUERY_SCIENCE_PATH, "book_id", "science/boost/")  


if __name__ == "__main__": 
    #query_romantic_tragedy()
    #query_world_war()
    #query_reviews()
    #query_science()
    query_world_war_nofilter()
