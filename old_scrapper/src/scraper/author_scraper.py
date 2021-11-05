from scraper.scraper import Scraper 

""" This file processes the author biography for the generated books
"""


class AuthorScraper(Scraper):
    def __init__(self, url) -> None:
        Scraper.__init__(self, url)
        self.url = url

    def get_description(self):
        try:
            div = self.soup.find('div', attrs={"class": "aboutAuthorInfo"})
            span = div.find_all('span')[1].text
            return span
        except:
            print("Error on getting author description on", self.url)
            return ""
