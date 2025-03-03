import datetime


class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return f'Knygos pavadinimas: {self.title}, autorius: {self.author}, metai: {self.year}'

    def is_classic(self):
        year_now = datetime.datetime.now().year
        return year_now - self.year > 50


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print('Bibliotekoje nera knygu')
        else:
            for book in self.books:
                print(book)







