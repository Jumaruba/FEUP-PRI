import json
import csv
import os 
from time import strptime

MAX_REVIEWS = 100000
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
RAW_PATH = CURRENT_PATH + "/../../data/raw/reviews.json"
CLEAN_PATH = CURRENT_PATH + "/../../data/clean/reviews.csv"

def clean_reviews():
    reviews_raw = open(RAW_PATH, "r")
    reviews_clean = open(CLEAN_PATH, "w", newline="\n", encoding="utf-8")
    writer = csv.writer(reviews_clean)

    header = ["book_id", "review_id", "rating", "review_text", "date_added"]
    writer.writerow(header)

    for i, reviews_obj in enumerate(reviews_raw):
        if i == MAX_REVIEWS:
            break 
            
        review = json.loads(reviews_obj) 
        review.pop('user_id', None)
        review.pop('date_updated', None)
        review.pop('started_at', None)
        review.pop('n_comments', None)
        review.pop('n_votes', None)
        review.pop('read_at', None) 

        _, month, day, time, _, year = review['date_added'].split(' ')
        review['date_added'] = "%04d-%02d-%02d %s" % (int(year),int(strptime(month,'%b').tm_mon),int(day),time)
        
        review['review_text'] = review['review_text'].replace("(view spoiler)[", "")
        review['review_text'] = review['review_text'].replace("(hide spoiler)]", "") 

        # Check if the text starts with "
        if review['review_text'][0] != '\"':
            review['review_text'] = "\"" + review['review_text']

        if review['review_text'][-1] != '\"':
            review['review_text'] += "\""

        writer.writerow(list(review.values()))

    reviews_raw.close()
    reviews_clean.close()


if __name__ == '__main__':
    clean_reviews()
