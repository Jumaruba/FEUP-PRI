from clean_authors import clean_authors
from clean_books import clean_books
from clean_genres import clean_genres
from clean_reviews import clean_reviews
from clean_series import clean_series

if __name__ == '__main__':
    clean_reviews()
    clean_books()
    clean_genres()
    clean_authors()
    clean_series()