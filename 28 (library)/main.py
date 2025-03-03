from random import choice

from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()

def sanitize_input(user_input):
    return user_input.strip()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

    borrowed_books = relationship('BorrowedBook', back_populates='book')


class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    borrowed_books = relationship('BorrowedBook', back_populates='reader')


class BorrowedBook(Base):
    __tablename__ = 'borrowedBooks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    reader_id = Column(Integer, ForeignKey('readers.id'), nullable=False)
    borrowed_at = Column(DateTime, default=datetime.now())
    return_due_date = Column(DateTime, default=datetime.now() + timedelta(days=30))

    book = relationship('Book', back_populates='borrowed_books')
    reader = relationship('Reader', back_populates='borrowed_books')


engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)


# Lenteliu sukurimas ========================


Session = sessionmaker(bind=engine)
session = Session()

def add_book():
    title = sanitize_input(input('Iveskite knygos pavadinima: '))
    author = sanitize_input(input('Iveskite knygos autoriu: '))
    year_published = input('Iveskite knygos isleidimo metus: ')
    if not year_published.isdigit():
        print('Klaida, knygos metai turi buti skaiciai!')
        return
    book = Book(title=title, author=author, year_published=year_published)
    session.add(book)
    session.commit()
    print('Knyga prideta sekmingai.')

def add_reader():
    name = sanitize_input(input('Iveskite vartotojo varda: '))
    email = sanitize_input(input('Iveskite vartotojo el. pasta: '))
    existing_reader = session.query(Reader).filter_by(email=email).first()
    if existing_reader:
        print('Klaida, skaitytojas su tokiu el. pastu jau egzistuoja.')
        return
    reader = Reader(name=name, email=email)
    session.add(reader)
    session.commit()
    print('Vartotojas sekmingai pridetas.')


def borrow_book():
    book_id = input('Iveskite knygos ID: ')
    reader_id = input('Iveskite vartotojo ID: ')
    if not book_id.isdigit() or not reader_id.isdigit():
        print('Klaida, skaitytojo ir knygos ID turi buti skaiciai!')
        return
    book = session.query(Book).filter_by(id=book_id, available=True).first()
    if book:
        borrowed_book = BorrowedBook(book_id=book_id, reader_id=reader_id)
        book.available = False
        session.add(borrowed_book)
        session.commit()
        print('Sekmingai pasiskolinote knyga.')
    else:
        print('Klaida, knyga jau pasiskolinta arba tokia knyga neegzistuoja.')

def update_book():
    book_id = input('Iveskite knygos ID: ')
    if not book_id.isdigit():
        print('Klaida, knygos ID turi buti skaiciai!')
        return
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book.title = sanitize_input(input('Iveskite nauja knygos pavadinima: '))
        book.author = sanitize_input(input('Iveskite nauja knygos autoriu: '))
        session.commit()
        print('Knyga atnaujinta sekmingai.')
    else:
        print('Klaida! Knyga atnaujinta nesekmingai')

def delete_book():
    book_id = input('Iveskite knygos ID: ')
    if not book_id.isdigit():
        print('Klaida, knygos ID turi buti skaiciai!')
        return
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print('Knyga pasalinta sekmingai!')
    else:
        print('Klaida salinant knyga.')

def delete_reader():
    reader_id = input('Iveskite vartotojo ID: ')
    if not reader_id.isdigit():
        print('Klaida, skaitytojo ID turi buti skaiciai.')
    reader = session.query(Reader).filter_by(id=reader_id).first()
    if reader:
        session.delete(reader)
        session.commit()
        print('Skaitytojas pasalintas sekmingai.')
    else:
        print('Klaida salinant skaitytoja.')

def show_books():
    books = session.query(Book).all()
    if books:
       for book in books:
           print(f' ID: {book.id}, Knygos pavadinimas: {book.title}, autorius: {book.author} - {"Prieinama" if book.available else "Neprieinama"}')
    else:
        print('Knygu lentyna yra tuscia')

def show_readers():
    readers = session.query(Reader).all()
    if readers:
        for reader in readers:
            print(f'ID: {reader.id}, vardas: {reader.name}, el. pastas: {reader.email}')
        else:
            print('Skaitytoju nera.')


def show_borrowed_books():
    borrowed_books = session.query(BorrowedBook).all()
    for borrowed in borrowed_books:
        print(f'Knyga: {borrowed.book.title}, pas skaitytoja {borrowed.reader.name}, paskolinta iki {borrowed.return_due_date}')

def time_borrowed_book():
    book_id = sanitize_input(input('Iveskite knygos ID: '))
    if not book_id.isdigit():
        print('Klaida, knygos ID turi buti skaiciai!')
        return
    record = session.query(BorrowedBook).filter(BorrowedBook.book_id == int(book_id)).first()
    if record:
        days_borrowed = (datetime.now() - record.borrowed_at).days
        print(f'Knyga jau paskolinta {days_borrowed} dienu.')
    else:
        print('Knyga nera paskolinta.')


def reader_books_history():
    reader_id = sanitize_input(input('Iveskite skaitytojo ID: '))
    if not reader_id.isdigit():
        print('Klaida, skaitytojo ID turi buti skaiciai.')
        return
    records = session.query(BorrowedBook).filter(BorrowedBook.reader_id == int(reader_id)).all()
    for record in records:
        print(f'Knyga: {record.book.title}, paskolinta: {record.borrowed_at} iki {record.return_due_date}')




while True:
    print(f'-- KNYGU BIBLIOTEKA --')
    print('========================')
    print('---------MENIU----------')
    print('1 - Prideti nauja knyga')
    print('2 - Prideti nauja skaitytoja')
    print('3 - Paskolinti knyga skaitytojui')
    print('4 - Atnaujinti knygos informacija')
    print('5 - Pasalinti knyga')
    print('6 - Pasalinti skaitytoja')
    print('7 - Rodyti visas knygas')
    print('8 - Rodyti visus skaitytojus')
    print('9 - Rodyti paskolintas knygas')
    print('10 - Rodyti kiek laiko paskolinta knyga')
    print('11 - Rodyti skaitytojo skolinimosi istorija')
    print('0 - Iseiti is programos')

    print('========================')

    choice = input('Pasirinkite veiksma: ')
    if choice == '1':
        add_book()
    elif choice == '2':
        add_reader()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        update_book()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        delete_reader()
    elif choice == '7':
        show_books()
    elif choice == '8':
        show_readers()
    elif choice == '9':
        show_borrowed_books()
    elif choice == '10':
        time_borrowed_book()
    elif choice == '11':
        reader_books_history()
    elif choice == '0':
        print('Programa baigia savo darba')
        break
    else:
        print('Neteisingas pasirinkimas.')

















