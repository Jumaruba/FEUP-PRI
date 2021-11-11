import pandas as pd
from mdutils.mdutils import MdUtils
from utils import *

def explore_genres():
    genres_processed_path = "../../data/processed/genres.csv"
    authors_df = pd.read_csv(genres_processed_path)
    md = MdUtils(file_name='../../data/explore/genres', title='Genres - Data Exploration and Characterization')

    stats(authors_df, md)

    md.create_md_file()

if __name__ == '__main__':
    explore_genres()