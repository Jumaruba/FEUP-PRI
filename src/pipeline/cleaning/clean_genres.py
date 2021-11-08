import json

genres_raw = open("../../data/raw/genres.json" ,"r")
genres_clean = open("../../data/clean/genres.json" ,"w")

genres_list = []
for genres_obj in genres_raw: 
    genres = json.loads(genres_obj) 
    if bool(genres['genres']):  
        genres_list.append(genres)

json.dump(genres_list, genres_clean, indent=2)
genres_raw.close()
genres_clean.close()