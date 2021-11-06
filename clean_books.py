import json

books_raw = open("data/raw/books.json" ,"r")
books_clean = open("data/clean/books.json" ,"w")

books_list = []
for books_obj in books_raw: 
    book = json.loads(books_obj)
    book.pop("text_reviews_count", None)
    book.pop("country_code", None)
    book.pop("popular_shelves", None)
    book.pop("asin", None)
    book.pop("kindle_asin", None)
    book.pop("link", None)
    book.pop("url", None)
    book.pop("word_id", None)
    if book['description']: books_list.append(book)
    
json.dump(books_list, books_clean, indent=2)
books_raw.close()
books_clean.close()