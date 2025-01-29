
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
    for elem in args:
        print(n ** elem)

pakelti_laipsniu(2, 4, 5, 6)