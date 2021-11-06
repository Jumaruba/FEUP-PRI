import json

authors_raw = open("../../data/raw/authors.json" ,"r")
authors_clean = open("../../data/clean/authors.json" ,"w")

authors_list = []
for author_obj in authors_raw: 
    author = json.loads(author_obj)
    author.pop("text_reviews_count", None)
    authors_list.append(author)

json.dump(authors_list, authors_clean, indent=2)
authors_raw.close()
authors_clean.close()