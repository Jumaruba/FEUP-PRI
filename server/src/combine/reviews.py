class ReviewsCombine:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def combine(self):
        self.cursor.execute("DROP TABLE IF EXISTS reviews_combined") 
        self.cursor.execute('''CREATE TABLE reviews_combined AS
                            SELECT review.review_id, review.book_id, review.rating, review.review_text, review.date_added, books_combined.title, books_combined.genres, books_combined.authors
                            FROM books_combined
                            INNER JOIN review ON books_combined.book_id = review.book_id;''')
        self.connection.commit()
