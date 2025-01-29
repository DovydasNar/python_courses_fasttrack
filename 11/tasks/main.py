
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

#                           2 task

def spausdinti_zinutes(kartai, *args, pabaiga='!'):
    for i in args:
        print((i + ' ') * kartai + pabaiga)

spausdinti_zinutes(5, 'Labas, Dovydai', 'kaip sekasi', pabaiga='!')


print('============================================')


def dauginti_skaicius(n, *args):
    res = []
    for numb in args:
        res.append(n * numb)
    return res

print(dauginti_skaicius(5, 2, 3, 4, 5))


print('============================================')


