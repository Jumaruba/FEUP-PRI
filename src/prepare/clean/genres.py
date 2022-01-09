import json
import csv
from typing import List
import os 

MAX_GENRES = 11000
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
RAW_PATH = CURRENT_PATH + "/../../data/raw/genres.json"
CLEAN_PATH = CURRENT_PATH + "/../../data/clean/genres.csv"

def get_genres(genres_groups: List[str]) -> List[str]:
    genres = []
    for genres_group in genres_groups: 
        genres += get_names(genres_group)
    return genres 

def get_names(group_names: str) -> List[str]:
    """In the json some genres names may be separated by ",". Thus to extract the real names, it's important to treat these cases.

    Args:
        group_names (str): String with genres separated by space.

    Returns:
        List[str]: List of genres. 
    """
    arr = group_names.split(",")
    arr = list(map(str.strip, arr))

    return arr 


def clean_genres():
    genres_raw = open(RAW_PATH ,"r")
    genres_clean = open(CLEAN_PATH ,"w", newline="\n", encoding="utf-8")
    writer = csv.writer(genres_clean)

    header = ["book_id", "genres"]
    writer.writerow(header)

    n_genres = 0
    for genres_obj in genres_raw: 
        if n_genres == MAX_GENRES:
            break
        genres = json.loads(genres_obj) 
        if bool(genres['genres']):  
            genres_arr = get_genres(list(genres["genres"].keys()))
            writer.writerow([genres["book_id"], genres_arr])
            n_genres += 1

    genres_raw.close()
    genres_clean.close() 

if __name__ == '__main__':
    clean_genres()