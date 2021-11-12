import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import seaborn as sns
from mdutils.mdutils import MdUtils

def wordcloud(df, md, category):
    # Generate a word cloud image
    wordcloud = WordCloud().generate(' '.join(df[category]))

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='nearest')
    plt.axis('off')
    plt.savefig('../../data/explore/plots/wordcloud' + category + '.jpg', bbox_inches='tight')
    plt.clf()
    
    md.new_paragraph(md.new_inline_image(text='Wordcloud with the words used on Book titles', path='plots/wordcloud' + category + '.jpg'))

def explore_books(df, md):
    # Rating Distribution
    #df['is_ebook'].plot(kind='bar')

    sns.histplot(data=df, x="is_ebook", binwidth=0.1).set_title('Distribution of the ebooks')
    plt.savefig('../../data/explore/plots/is_ebook.jpg')
    plt.clf()
    md.new_paragraph(md.new_inline_image(text='', path='plots/is_ebook.jpg'))

def explore_cvstats():
    pass

if __name__ == "__main__":
    books_path = "../../data/processed/books.csv"
    df = pd.read_csv(books_path)
    print(df.isna().sum())
    md = MdUtils(file_name='../../data/explore/books', title='Books - Data Exploration and Characterization')
    md.new_header(level=2, title='Books Descriptive Analysis', add_table_of_contents='n')

    wordcloud(df, md, 'title')
    explore_books(df, md)
    md.create_md_file()