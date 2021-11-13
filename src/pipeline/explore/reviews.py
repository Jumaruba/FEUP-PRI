#%%
import pandas as pd
import os
from mdutils import MdUtils
import wordcloud
from utils.helpers import stats
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def write_image(text:str, image_name: str) -> str:
    return f"![{text}](reviews/{image_name})"



# PREDEFINED VARS =======================
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PROCESSED_PATH = CURRENT_PATH + "/../../data/combine/"
OUTPUT_PATH = CURRENT_PATH + "/../../data/explore/reviews/"
os.mkdir(OUTPUT_PATH)

# MARKDOWN ==============================
df_reviews = pd.read_csv(PROCESSED_PATH + "reviews.csv", encoding="utf-8")
mdFile = MdUtils(file_name='reviews', title='Reviews Data Characterization')
#%%
# Visualize the header
mdFile.write("To get a feeling of the data, let's visualize the reviews head data.")
header = str(df_reviews.head())
mdFile.insert_code(header)

# Stats 
stats(df_reviews, mdFile)

# WordCloud 
image_name = "wordcloud.png"
mdFile.new_header(level=2, title="Word cloud")
mdFile.write("Visualizing the most frequent words in the texts.")
mdFile.new_line()
mdFile.write(write_image("Wordcloud", image_name))
wordcloud = WordCloud(background_color="white", width=3000,
                      height=2000).generate_from_text(str(df_reviews['review_text']))
plt.figure(figsize=[15, 10])
plt.imshow(wordcloud, interpolation="bilinear")
plt.savefig(OUTPUT_PATH + image_name)
plt.close()

# Rating 
image_name = "rating_barplot.png"

mdFile.new_header(level=2, title="Rating analysis")
mdFile.write("Getting the frequence of rating.")
mdFile.new_line()
mdFile.write(write_image("Rating barplot", image_name))

count = df_reviews['rating'].value_counts()
plt.figure()
plt.bar(count.index, count.values)
plt.title("Rating frequence")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig(OUTPUT_PATH + image_name)

# Top 20 most talked books
mdFile.new_header(level=2,  title="Most talked books")
df_books = pd.read_csv(PROCESSED_PATH + "books.csv") 
count = df_reviews['book_id'].value_counts()[:20]
books_ids = count.index
frequency = count.values

book_title = df_books[df_books['book_id'].isin(books_ids)]['title']
most_talked_books = pd.DataFrame({'id': books_ids, 'title': book_title, 'num_reviews': frequency}).to_markdown(index=False)
mdFile.write(most_talked_books, wrap_width=0)


# Save
mdFile.create_md_file()
