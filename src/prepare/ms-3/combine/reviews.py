class ReviewsCombine:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def combine(self):
        print("Combining Reviews")
        self.cursor.execute("DROP TABLE IF EXISTS reviews_combined") 
        self.cursor.execute('''CREATE TABLE reviews_combined AS
                            SELECT review.review_id, review.book_id, review.rating, review.review_text, review.date_added, books_combined.title, books_combined.genres, books_combined.authors
                            FROM books_combined
                            INNER JOIN review ON books_combined.book_id = review.book_id;''')
        
        self.cursor.execute('''UPDATE books_combined
                                SET rating = (SELECT rating_values.rating as rating
                                    FROM (SELECT reviews_combined.book_id as book_id, round(AVG(reviews_combined.rating), 2) as rating
                                    FROM reviews_combined
                                    GROUP BY reviews_combined.book_id) rating_values
                                    WHERE rating_values.book_id = books_combined.book_id);''')

        self.connection.commit()
        print("Finished Combining Reviews")
