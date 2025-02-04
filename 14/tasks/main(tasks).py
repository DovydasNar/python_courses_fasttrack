                                        # 1 task


class Car:
    manufacturer = 'Toyota'

print(Car.manufacturer)


class Bike:
    manufacturer = 'Yamaha'

print(Bike.manufacturer)

print('===============================================')

                                        # 2, 3, 4, 5, 6 tasks
from datetime import datetime

class Book:

    publisher = 'Penguin'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_age(self):
        current_year = datetime.now().year
        return current_year - self.year


book1 = Book('Altoriu Sesely', 'Vincas Mykolaitis Putinas', 1933)
book2 = Book('Vakaru fronte nieko naujo', 'E. M. Remarkas', 1928)
book3 = Book('Tarp pilku debesu', 'Ruta Sepetys', 2023)


print(f'Book 1: {book1.title}, {book1.author}, {book1.year}, publisher: {Book.publisher}')
print(f'Book 2: {book2.title}, {book2.author}, {book2.year}')
print(f'Book 3: {book3.title}, {book3.author}, {book3.year}')

print('===============================================')

print(f'Knyga: {book1.title} yra {book1.get_book_age()} metu senumo')
print(f'Knyga: {book2.title} yra {book2.get_book_age()} metu senumo')
print(f'Knyga: {book3.title} yra {book3.get_book_age()} metu senumo')

print('===============================================')

















