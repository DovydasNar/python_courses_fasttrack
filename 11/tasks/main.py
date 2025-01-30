
#                           1 task

def sudeti_skaicius(*args):
    res = sum(args)
    print(res)

sudeti_skaicius(5, 10, 15)
sudeti_skaicius(100, 200, 300, 400)

print('============================================')

def sveikinti_vardus(*args):
    res = ''
    for name in args:
        res += f'Hello {name}\n'
    return res

print(sveikinti_vardus('Dovydas', 'John', 'Jack'))


print('============================================')


def pakelti_laipsniu(n, *args):
    return [i ** n for i in args]     #   <- sutrumpintas budas
    # for elem in args:
    #     print(n ** elem)

print(pakelti_laipsniu(2, 4, 5, 6))

print('============================================')
print('============================================')

#                           2 task

def spausdinti_zinutes(kartai, *args, pabaiga='!'):
    for i in args:
        print((i + ' ') * kartai + pabaiga)

spausdinti_zinutes(5, 'Labas, Dovydai', 'kaip sekasi', 'gerai', pabaiga='!')


print('============================================')


def dauginti_skaicius(n, *args):
    res = []
    for numb in args:
        res.append(n * numb)
    return res

print(dauginti_skaicius(5, 2, 3, 4, 5))


print('============================================')
print('============================================')


#                           3 task

def rodyti_duomenis(**kwargs):
    print(kwargs)

rodyti_duomenis(vardas='Dovydas', pavarde='Narvilas', gim_metai=1996, lytis='vyras')


print('============================================')
print('============================================')

#                          4 task

# 11 task

pakelti_kvadratu = lambda x: x ** 2
print(pakelti_kvadratu(5))

print('============================================')

# 12 task

darbuotojai = [
    ('Jonas', 2500),
    ('Asta', 3200),
    ('Mantas', 2100)
]

print(type(darbuotojai))

surusiuoti_darbuotojai = sorted(darbuotojai, key=lambda x: x[1])
print(surusiuoti_darbuotojai)

print('============================================')


# 13 task

sarasas = [5, 10, 15, 20, 25, 30]

dalijasi_is_10 = list(filter(lambda x: x % 10 == 0, sarasas))

print(dalijasi_is_10)

print('============================================')
print('============================================')
