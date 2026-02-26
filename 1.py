class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self._author = author
        self._year = year

    def get_info(self):
        return f'"{self.title}" ({self._author}, {self._year})'
    

class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def get_info(self):
        return f'"{self.title}" ({self._author}, {self._year}), ISBN: {self.isbn}'
    

class Magazine(Publication):
    def __init__(self, title, editor, year, issue_number):
        super().__init__(title, editor, year)
        self.issue_number = issue_number

    def get_info(self):
        return f'"{self.title}" (Ред. {self._author}, {self._year}), Выпуск №{self.issue_number}'
    