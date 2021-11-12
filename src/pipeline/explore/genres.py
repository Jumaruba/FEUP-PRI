import pandas as pd
from mdutils.mdutils import MdUtils
from utils import *
import seaborn as sns
from matplotlib import pyplot as plt

def explore_genres(md):
    genres_processed_path = "../../data/processed/genres.csv"
    genres_df = pd.read_csv(genres_processed_path)

    stats(genres_df, md)

def explore_genres_books(md):
    genres_books_path = "../../data/processed/genres_books.csv"
    genres_books_df = pd.read_csv(genres_books_path)
    genres_processed_path = "../../data/processed/genres.csv"
    genres_df = pd.read_csv(genres_processed_path)

    merged_df = pd.merge(genres_books_df, genres_df, on="genre_id")

    md.new_header(level=2, title='Genres Descriptive Analysis', add_table_of_contents='n')
    
    sns.countplot(merged_df['genre_name'], dodge=False).set_title('No. of books per genre')
    plt.savefig(get_plots_path() + 'books_per_genre_count.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/books_per_genre_count.jpg'))

if __name__ == '__main__':
    md = MdUtils(file_name='../../data/explore/genres', title='Genres - Data Exploration and Characterization')
    explore_genres(md)
    explore_genres_books(md)
    md.create_md_file()