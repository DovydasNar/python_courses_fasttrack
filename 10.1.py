# import random
#
# atsitiktinis_skaicius = random.randint(1, 10)
# print(f"Atsitiktinis int skaičius nuo 1 iki 10: {atsitiktinis_skaicius}")

#                                               1,2 uzduotis

import random

atsitiktinis_skaicius = random.randint(1, 100)
atsitiktinis_realus = random.uniform(1, 50)

print(f'Atsitiktinis skaicius: {atsitiktinis_skaicius}')
print(f'Atsitiktinis float skaicius: {atsitiktinis_realus}')

print('======================================================================')

#                                               3 uzduotis

from random import randint, choice
generate_random_number = randint(1, 10)
print(generate_random_number)

select_random_fruit = choice(['obuolys', 'bananas', 'kriause', 'vysnia'])
print(select_random_fruit)

print('======================================================================')

#                                               4 uzduotis

import datetime as dt

print(f'Data ir laikas: {dt.datetime.now()}')

print('======================================================================')

#                                               5 uzduotis

from math import sqrt as sq

kvadratine_saknis = sq(625)
print(kvadratine_saknis)


print('======================================================================')

#                                               6 uzduotis

from math import *

sinusas = sin(90)
print(sinusas)

print('======================================================================')



