import os

def get_combine_path(name): 
    current_path =  os.path.dirname(os.path.abspath(__file__))
    return current_path + "/../../data/combine/"+ name + ".csv"

def get_search_path(name):
    current_path =  os.path.dirname(os.path.abspath(__file__)) 
    return current_path + "/../../data/search/"+ name + ".csv"