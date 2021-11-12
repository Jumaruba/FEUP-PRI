import pandas as pd
from mdutils.mdutils import MdUtils
from utils import *
import seaborn as sns
from matplotlib import pyplot as plt

def explore_authors(md : MdUtils):
    authors_processed_path = "../../data/processed/authors.csv"
    authors_df = pd.read_csv(authors_processed_path)

    stats(authors_df, md)

    md.new_header(level=2, title='Authors Descriptive Analysis', add_table_of_contents='n')

    # Rating Distribution
    sns.histplot(data=authors_df, x="average_rating", binwidth=0.1).set_title('Distribution of the average rating')
    plt.savefig(get_plots_path() + 'average_rating_histogram.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/average_rating_histogram.jpg'))

def explore_authors_books(md):
    authors_books_path = "../../data/processed/authors_books.csv"
    authors_books_df = pd.read_csv(authors_books_path)

    md.new_header(level=2, title='Author-Book Descriptive Analysis', add_table_of_contents='n')

    # Books per author
    explore_books_per_author(authors_books_df, md)

    # Authors per book
    explore_authors_per_book(authors_books_df, md)


def explore_books_per_author(authors_books_df, md):
    md.new_header(level=3, title='No. of Authors per Book', add_table_of_contents='n')
    
    books_per_author = authors_books_df.groupby(['author_id']).size()
    
    books_per_author_df = pd.DataFrame({'author_id':books_per_author.index, 'num_books':books_per_author.values})
    md.write(books_per_author_df["num_books"].describe().to_markdown(), wrap_width=0)
    sns.countplot(data=books_per_author_df, x="num_books").set_title('No. of books per author')
    plt.savefig(get_plots_path() + 'books_per_author_count.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/books_per_author_count.jpg'))

    sns.boxplot(data=books_per_author_df, x="num_books").set_title('No. of books per author')
    plt.savefig(get_plots_path() + 'books_per_author_boxplot.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/books_per_author_boxplot.jpg'))

    more_than_five_df = books_per_author_df.loc[books_per_author_df["num_books"] > 5]
    sns.countplot(data=more_than_five_df, x="num_books").set_title('No. of books per author (authors with more than five books)')
    plt.savefig(get_plots_path() + 'books_per_author_count2.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/books_per_author_count2.jpg'))

def explore_authors_per_book(authors_books_df, md):
    md.new_header(level=3, title='No. of Books per Author', add_table_of_contents='n')

    authors_per_book = authors_books_df.groupby(['book_id']).size()

    authors_per_book_df = pd.DataFrame({'book_id':authors_per_book.index, 'num_authors':authors_per_book.values})
    md.write(authors_per_book_df["num_authors"].describe().to_markdown(), wrap_width=0)
    sns.countplot(data=authors_per_book_df, x="num_authors").set_title('No. of authors per book')
    plt.savefig(get_plots_path() + 'authors_per_book_count.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/authors_per_book_count.jpg'))

    sns.boxplot(data=authors_per_book_df, x="num_authors").set_title('No. of authors per book')
    plt.savefig(get_plots_path() + 'authors_per_book_boxplot.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/authors_per_book_boxplot.jpg'))

    more_than_five_df = authors_per_book_df.loc[authors_per_book_df["num_authors"] > 3]
    sns.countplot(data=more_than_five_df, x="num_authors").set_title('No. of authors per book (books with more than three authors)')
    plt.savefig(get_plots_path() + 'authors_per_book_count2.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/authors_per_book_count2.jpg'))

if __name__ == '__main__':
    md = MdUtils(file_name='../../data/explore/authors', title='Authors - Data Exploration and Characterization')
    explore_authors(md)
    explore_authors_books(md)
    md.create_md_file()