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

    def retrieve_info(self)-> List[str]:
        """This method retrieves the information of a file as List.

        Raises:
            NotImplementedError: Must be implemented by the child class.

        Returns:
            List[str]: Information of a file.
        """
        raise NotImplementedError()

    def replace_multiple_spaces(self, str):
        return re.sub('\s+', ' ', str)



    