import csv
import os


def get_combine_path(name): 
    current_path =  os.path.dirname(os.path.abspath(__file__))
    return current_path + "/../data/combine/"+ name + ".csv"

    

authors_books = open(get_combine_path("authors_books"))
authors = open(get_combine_path("authors"))
books = open(get_combine_path("books")) 



