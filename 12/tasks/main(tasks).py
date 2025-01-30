

# task 2

def dalinti(a, b):
    try:
        return a / b
    except Exception as e:
        return f'Dalyba is nulio negalima: {e}'

print(dalinti(10, 2))
print(dalinti(5, 0))
print(dalinti(8, 4))

print('===============================')
print('===============================')

# task 3

while True:

    skaicius_ivestis =  input('Iveskite skaiciu: ')
    daliklis_ivestis =  input('Iveskite dalikli: ')

    try:
        skaicius = int(skaicius_ivestis)
        daliklis = int(daliklis_ivestis)

        res = skaicius / daliklis

        print(f'Rezultatas yra: {res}')
    except ValueError:
        print(f'Crash su ValueError, nes ivedete {skaicius_ivestis} ir {daliklis_ivestis}')
    except ZeroDivisionError:
        print(f'Crash su ZeroDivisionError, skaicius {skaicius_ivestis} nesidalina is {daliklis_ivestis} ')

    # break








