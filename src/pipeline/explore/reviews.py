# %%
import pandas as pd
from mdutils import MdUtils
from utils.helpers import *
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def write_image(text: str, image_name: str) -> str:
    return f"![{text}](plots/{image_name})"


def create_header(md_file, df_reviews) -> None:
    md_file.write(
        "To get a feeling of the data, let's visualize the reviews head data.")
    header = str(df_reviews.head())
    md_file.insert_code(header)


def create_world_cloud(md_file, df_reviews) -> None:
    # WordCloud
    image_name = "wordcloud.png"
    md_file.new_header(level=2, title="Word cloud")
    md_file.write("Visualizing the most frequent words in the texts.")
    md_file.new_line()
    md_file.write(write_image("Wordcloud", image_name))
    wordcloud = WordCloud(background_color="white", width=3000,
                          height=2000).generate_from_text(str(df_reviews['review_text']))
    plt.figure(figsize=[15, 10])
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.savefig(get_plots_filepath(image_name))
    plt.close()


def get_reviews_rating(md_file, df_reviews) -> None:
    image_name = "rating_barplot.png"

    md_file.new_header(level=2, title="Rating analysis")
    md_file.write("Getting the frequence of rating.")
    md_file.new_line()
    md_file.write(write_image("Rating barplot", image_name))

    count = df_reviews['rating'].value_counts()
    plt.figure()
    plt.bar(count.index, count.values)
    plt.title("Rating frequence")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.savefig(get_plots_filepath(image_name))


def get_most_talked_books(md_file, df_reviews) -> None:
    md_file.new_header(level=2,  title="Most talked books")
    df_books = pd.read_csv(get_processed_filepath("books.csv"))
    count = df_reviews['book_id'].value_counts()[:20]
    books_ids = count.index
    frequency = count.values

    book_title = df_books[df_books['book_id'].isin(books_ids)]['title']
    most_talked_books = pd.DataFrame(
        {'id': books_ids, 'title': book_title, 'num_reviews': frequency}).to_markdown(index=False)
    md_file.write(most_talked_books, wrap_width=0)


if __name__ == '__main__':
    df_reviews = pd.read_csv(get_processed_filepath(
        "reviews.csv"), encoding="utf-8")
    md_file = MdUtils(file_name=get_explore_filepath(
        "reviews"), title='Reviews Data Characterization')

    create_header(md_file, df_reviews)
    stats(df_reviews, md_file)
    create_world_cloud(md_file, df_reviews)
    get_reviews_rating(md_file, df_reviews)
    get_most_talked_books(md_file, df_reviews)

    md_file.create_md_file()
