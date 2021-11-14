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
    books_path = "../../data/processed/books.csv"
    books_rating_df = pd.read_csv(books_path, usecols=['book_id', 'average_rating'])

    merged_df = pd.merge(genres_books_df, genres_df, on="genre_id")

    md.new_header(level=2, title='Genres Descriptive Analysis', add_table_of_contents='n')
    
    # No of books per genre
    sns.catplot(data=merged_df, x="genre_name", aspect=3.3, kind="count")
    plt.savefig(get_plots_path() + 'books_per_genre_count.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/books_per_genre_count.jpg'))

    # Rating distribution by genre
    merged_df = pd.merge(merged_df, books_rating_df, on="book_id")
    
    g = sns.FacetGrid(merged_df, col="genre_name", col_wrap=4, height=3, aspect=2)
    g.map(sns.histplot, "average_rating")
    plt.savefig(get_plots_path() + 'rating_per_genre.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/rating_per_genre.jpg'))

if __name__ == '__main__':
    md = MdUtils(file_name='../../data/explore/genres', title='Genres - Data Exploration and Characterization')
    explore_genres(md)
    explore_genres_books(md)
    md.create_md_file()