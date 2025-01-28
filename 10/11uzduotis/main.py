from moduliai import aritmetika

print(aritmetika.dalyba(10, 2))
print(aritmetika.atimtis(10, 2))

print('==========================================')


import moduliai.aritmetika

print(moduliai.aritmetika.atimtis(20, 5))
print(moduliai.aritmetika.dalyba(10, 2))

print('==========================================')

from moduliai.aritmetika import atimtis, dalyba

res = atimtis(50, 25)
print(f'Atimtis: {res}')
res = dalyba(100, 4)
print(f'Dalyba: {res}')

print('==========================================')

import moduliai.aritmetika as ar

print(f'Atimtis: {ar.atimtis(30, 10)}')
print(f'Dalyba: {ar.dalyba(50, 5)}')

print('==========================================')

import moduliai


print(f'Atimtis: {moduliai.aritmetika.atimtis(15, 5)}')


