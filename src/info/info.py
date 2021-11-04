from typing import List

from bs4 import BeautifulSoup as bs 
import mechanize as mc
import re 

class Info:
    br = mc.Browser() 

    def __init__(self, url) -> None: 
        self.br = mc.Browser()
        html = self.get_html(url)
        self.soup = bs(html, "html.parser")
        self.retrieve_info()  

    def get_html(self, url):
        page = self.br.open(url)
        return page.read()

    def get_fields_number(self) -> int:
        raise NotImplementedError()

    def get_fields_name(self) -> List[str]: 
        raise NotImplementedError()

    def retrieve_info(self)-> List[str]:
        raise NotImplementedError()

    def replace_multiple_spaces(self, str):
        return re.sub('\s+', ' ', str)



    