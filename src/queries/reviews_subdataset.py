import pandas as pd

# This program must be executed in the filepath. 
f_bad = open("../data/queries/reviews/bad.txt", "r")
f_good = open("../data/queries/reviews/good.txt", "r")
df_reviews = pd.read_csv("../data/search/reviews.csv")

get_id = lambda line: int(line)
ids = list(map(get_id, f_bad.readlines() + f_good.readlines()))

subdataset = df_reviews[df_reviews.review_id.isin(ids)]
subdataset.to_csv("../data/search/reviews_subdataset.csv", index=False)