import json
import csv

def clean_reviews():
    reviews_raw = open("../../data/raw/reviews.json" ,"r")
    reviews_clean = open("../../data/clean/reviews.csv" ,"w", newline="\n", encoding="utf-8")
    writer = csv.writer(reviews_clean)

    header = ["book_id", "review_id", "rating", "review_text", "date_added"]
    writer.writerow(header)

    for reviews_obj in reviews_raw: 
        review = json.loads(reviews_obj) 
        review.pop('user_id', None) 
        review.pop('date_updated', None)
        review.pop('started_at', None)
        review.pop('n_comments', None)
        review.pop('n_votes', None)
        review.pop('read_at', None)
        writer.writerow(list(review.values()))

    reviews_raw.close()
    reviews_clean.close()

if __name__ == '__main__':
    clean_reviews()