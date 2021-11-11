class MdBuilder: 
    text: str 

    def add_h1(self, h1: str) -> None:
        self.text += f"# {h1}"

    def add_h2(self, h2: str) -> None:  
        self.text += f"## {h2}"
    
    def add_code(self, code: str) -> None: 
        self.text += f"```{code}```"
    
    def add_link(self, text: str, link: str) -> None:
        self.text += f"[{text}]({link})" 

    def add_text(self, text: str) -> None:  
        # The two final spaces are necessary.
        self.text += f"{text}  "

    def print(self):
        print(str)