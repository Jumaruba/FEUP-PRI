import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import seaborn as sns
from mdutils.mdutils import MdUtils
from utils import *

def head(df, md):
    md.new_line("To get a feeling of the data, let's visualize the reviews head data.")
    md.insert_code(str(df.head()))

def wordcloud(df, md, category):
    # Generate a word cloud image
    wordcloud = WordCloud().generate(' '.join(df[category]))
    md.new_line("Wordcloud with the words that are more used on Book Titles")

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='nearest')
    plt.axis('off')
    plt.savefig(get_plots_filepath('wordcloud' + category + '.jpg'), bbox_inches='tight')
    plt.clf()
    
    md.new_paragraph(md.new_inline_image(text='', path=get_plots_filepath('wordcloud' + category + '.jpg')))

def explore_books(df, md):
    md.new_line("")
    md.new_header(level=2, title='Physical or Ebook? Which one the readers prefer?', add_table_of_contents='n')
    sns.countplot(x=df['is_ebook']).set_title('Distribution of the ebooks')
    plt.savefig(get_plots_filepath('is_ebook.jpg'))
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path=get_plots_filepath('is_ebook.jpg')))
    md.new_line("")

def heatmap_books(df, md):
    md.new_line("")
    plt.figure(figsize=[10, 10])
    df_ = df[['average_rating', 'num_pages', 'book_id']]
    df_ = df_.dropna(axis = 0, subset=['num_pages'])
    md.new_header(level=2, title='Heatmap', add_table_of_contents='n')
    sns.heatmap(df_.corr(), annot=True, cbar=False)
    plt.savefig(get_plots_filepath('heatmap.jpg'))
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path=get_plots_filepath('heatmap.jpg')))
    md.new_line("")

def null_values(df,md):
    md.new_header(level=2, title='Null Count', add_table_of_contents='n')
    md.new_paragraph("Like in every database, there are some null values.")
    md.insert_code(str(df.isna().sum()))

def number_pages(df,md):
    md.new_header(level=2, title='Number Books with N Pages', add_table_of_contents='n')
    md.new_line(f"Book with the most number of pages: {df['num_pages'].max()}")

    ranges = [0,100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 10000]
    result = []
    for i in df.groupby(pd.cut(df.num_pages, ranges)).count()['title']:
        result.append(i)

    ranges = ['0', '100', '200', '300', '400', '500', '600', '700', '800', '900', '1000+']
    ax = sns.lineplot(x=ranges, y=result).set_title('Number Books with N Pages')
    plt.ylabel("Number of Books")
    plt.xlabel("Number of Pages")
    plt.savefig(get_plots_filepath('number_pages.jpg'))
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path=get_plots_filepath('number_pages.jpg')))
    md.new_line("")


def date_published(df,md):
    md.new_header(level=2, title='Date published', add_table_of_contents='n')
    md.new_line("")
    df['publication_year'] = df['date'].apply(lambda x: x.split("-")[0])
    ax = sns.countplot(x=df['publication_year']).set_title('Publication')
    plt.savefig(get_plots_filepath('date_published.jpg'))
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path=get_plots_filepath('date_published.jpg')))
    md.new_line("")


if __name__ == "__main__":
    books_path = get_processed_filepath('books.csv')
    df = pd.read_csv(books_path)
    
    md = MdUtils(file_name=get_explore_filepath("books"), title='Books - Data Exploration and Characterization')
    md.new_header(level=2, title='Books Descriptive Analysis', add_table_of_contents='n')
    md.new_paragraph()
    head(df, md)
    stats(df, md)
    wordcloud(df, md, 'title')
    explore_books(df, md)
    heatmap_books(df, md)
    #null_values(df,md)
    number_pages(df,md)
    #date_published(df,md)
    md.create_md_file()