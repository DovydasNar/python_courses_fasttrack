                                    # 1. Klasės kūrimas ir statiniai laukai

# class House:
#     country = "LT"
#
# print(House.country)  # LT


                                # 2. Konstruktorius init ir instancijos laukų inicializavimas

class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

                                    # 3. Statinio lauko ir instancijų naudojimas


# print(House.country)  # LT

house_instance_1 = House(10_000, 1990)
print(house_instance_1.price)  # 10000
print(house_instance_1.year)  # 1990

house_instance_2 = House(12_000, 1920)
print(house_instance_2.price)  # 12000
print(house_instance_2.year)  # 1920


                                        # 4. Klasės instancijų atvaizdavimas


print(house_instance_1)  # <__main__.House object at 0x000001FDB47DB850>
print(house_instance_2)  # <__main__.House object at 0x000001FDB47DB790>

                                    # 5. Savų metodų kūrimas klasėje

import datetime

class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year


                                    # 6. Metodų iškvietimas ir rezultatų naudojimas


house_instance_1 = House(10_000, 1990)
age = house_instance_1.get_age()
print(age)  # 34

house_instance_2 = House(12_000, 1920)
print(house_instance_2.get_age())  # 104



                                    # str metodas – Objektų atvaizdavimo valdymas


class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year

    def __str__(self):
        return f"Namas {self.year} pastatymo, kaina - {self.price}, amžius - {self.get_age()}"


                                # Objektų grupių valdymas naudojant sąrašus

house1 = House(22_000, 1980)
house2 = House(12_000, 1970)
house3 = House(33_000, 2000)

houses = [house1, house2, house3]
print(houses)

for house in houses:
    print(house)


                                    # Objektų laukų keitimas iteruojant per sąrašą


for house in houses:
    print(f"sena kaina: {house.price}")
    house.price = round(house.price * 1.21)
    print(f"nauja kaina: {house.price}")

print(house1)



                        # Objektų pridėjimas į sąrašą naudojant vartotojo įvestį


houses_kaupiklis = []
while True:
    quit_choice = input("įveskite bet kokį simbolį kad išeiti Enter, tęsti įvedimą")
    if quit_choice:
        break

    year = int(input("Įveskite metus "))
    price = int(input("Įveskite kainą "))

    house_instance = House(price, year)
    houses_kaupiklis.append(house_instance)

    print("Spausdinam ką sukaupėm")
    for house in houses_kaupiklis:
        print(house)

