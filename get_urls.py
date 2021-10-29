from bs4 import BeautifulSoup as bs
import requests

def get_soup(url):
    page = requests.get(url)
    return bs(page.content, 'html.parser')

def get_books(soup): 
    for a in soup.find_all('a', {'class':'bookTitle'}, href=True):
        print(a['href'])

for i in range(1, 101):
    seed_url = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page={}".format(i)
    soup = get_soup(seed_url)
    get_books(soup)
