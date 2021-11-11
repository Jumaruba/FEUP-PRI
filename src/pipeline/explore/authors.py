import pandas as pd
from mdutils.mdutils import MdUtils
from utils import *

def explore_authors():
    authors_processed_path = "../../data/processed/authors.csv"
    authors_df = pd.read_csv(authors_processed_path)
    md = MdUtils(file_name='../../data/explore/authors', title='Authors - Data Exploration and Characterization')

    stats(authors_df, md)

    md.create_md_file()

if __name__ == '__main__':
    explore_authors()