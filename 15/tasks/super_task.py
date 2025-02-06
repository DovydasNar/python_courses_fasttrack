from datetime import datetime, timedelta


class Book:

    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self.borrow_data = None

    def __str__(self):
        status = 'Prieinama' if self.available else f'Pasiskolinta iki: {self.due_date()}'
        return f'Knygos pavadinimas: {self.title}, autorius: {self.author}, isleista: {self.year}. {status}'


    def is_classic(self):
        current_year = datetime.now().year
        return current_year - self.year > 50

    def due_date(self):
        if self.borrow_data:
            return (self.borrow_data + timedelta(days=14)).strftime('%Y-%m-%d')
        return 'Nera pasiskolinta'



class Library:

    def __init__(self):
        self.books = []

    def add_book(self):


        title = input('Iveskite knygos pavadinima: ')
        author = input('Iveskite knygos autoriu: ')

        try:
            year = int(input('Iveskite knygos amziu: '))
        except ValueError:
            print(f'Klaida, iveskite skaicius.')
            return

        book = Book(title, author, year)
        self.books.append(book)
        print(f'Knyga {book.title} prideta i biblioteka')

    def display_books(self):
        if not self.books:
            print('Bibliotekoje nera prideta knygu.')
        else:
            for book in self.books:
                print(book)

    def borrow_book(self):
        title = input('Iveskite knyga, kuria norite pasiskolinti: ')
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    book.borrow_data = datetime.now()
                    print(f'Pasiskolinote knyga: {book.title}, grazinti iki: {book.due_date()}')
                else:
                    print(f'Knyga {book.title} neprieinama')
                return
        print(f'Tokios knygos - {title} nera bibliotekoje')

    def return_book(self):

        title = input('Iveskite grazinamos knygos pavadinima: ')

        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    book.borrow_data = None
                    print(f'Knyga: {book.title}, sekmingai grazinta.')
                else:
                    print(f'Knyga {book.title} jau bibliotekoje')
                return
        print(f'Tokios knygos - {title} nera bibliotekoje')

    def filter_books(self, **kwargs):

        print('Pasirinkite kriteriju, pagal ka filtruoti rezultatus:')
        print('1 - Pagal pavadinima')
        print('2 - Pagal autoriu')
        print('3 - Pagal metus')

        choice = input('Iveskite numeri, pagal ka norite isfiltruoti rezultatus: ')

        if choice == '1':
            title = input('Iveskite pavadinima: ')
            filtered = [book for book in self.books if title in book.title.lower()]
        elif choice == '2':
            author = input('Iveskite autoriu: ')
            filtered = [book for book in self.books if author in book.author.lower()]
        elif choice == '3':
            try:
                year = int(input('Iveskite metus: '))
                filtered = [book for book in self.books if book.year == year]
            except ValueError:
                print('Klaida, ivestis turi buti skaiciai!')
                return
        else:
            print('Neteisingas pasirinkimas!')

        if filtered:
            print('Knygos pagal jusu filtravima:')
            for book in filtered:
                print(book)
        else:
            print('Klaida, nerasta tokios knygos.')


library = Library()

while True:
    print('===== MENIU ====')
    print('1 - Prideti nauja knyga i biblioteka')
    print('2 - Perziureti visa bibliotekos knygu sarasa ')
    print('3 - Pasiskolinti knyga ')
    print('4 - Grazinti knyga ')
    print('5 - Filtruoti knygas pagal pavadinima, autoriu ar metus ')
    print('6 - Iseiti is programos')

    choice = input('Irasykite atitinkama skaiciu, atlikti veiksmams: ')

    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        library.borrow_book()
    elif choice == '4':
        library.return_book()
    elif choice == '5':
        library.filter_books()
    elif choice == '6':
        print('Programa baige savo darba. Aciu ir Iki!')
        break
    else:
        print('Klaida! Iveskite tinkama skaiciu is meniu!')
        continue































