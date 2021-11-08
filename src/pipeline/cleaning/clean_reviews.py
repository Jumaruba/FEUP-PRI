import json

reviews_raw = open("../../data/raw/reviews.json" ,"r")
reviews_clean = open("../../data/clean/reviews.json" ,"w")

reviews_list = []
for reviews_obj in reviews_raw: 
    review = json.loads(reviews_obj) 
    review.pop('user_id', None) 
    review.pop('date_updated', None)
    review.pop('started_at', None)
    review.pop('n_comments', None)
    review.pop('n_votes', None)
    review.pop('read_at', None)
    reviews_list.append(review)


json.dump(reviews_list, reviews_clean, indent=2)
reviews_raw.close()
reviews_clean.close()