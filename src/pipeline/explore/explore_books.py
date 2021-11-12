import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

def wordcloud(df, category):
    # Generate a word cloud image
    wordcloud = WordCloud().generate(' '.join(df[category]))

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    books_path = "../../data/processed/books.csv"
    df = pd.read_csv(books_path)

    wordcloud(df, 'title')