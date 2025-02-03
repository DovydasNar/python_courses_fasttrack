#                       Funkcijos, pažangi dalis

# def print_args(*args):
#     print(args)
#
#
# print_args('Dovydas', 'Adomas', 2025)

def give_hello_to_names(*args):
    res = ""
    for name in args:
        res += f"Hello {name}\n"
    return res


print(give_hello_to_names('Dovydas', 'John', 'Valdas'))


print('============================================')

def multiply_all_by_numb(numb, *args):
    for elem in args:
        print(elem * numb)

multiply_all_by_numb(7, 10, 11, 50)

print('============================================')

def take_order(customer_name, *args):
    '''

    :param customer_name:
    :param args:
    :return:
    '''

    print(f'Order for {customer_name}')
    for i in args:
        print(f'- {i}')
    print('Thank you for your order!')

take_order('Dovydas', 'Milk', 'Beer', 'Pizza')

print('============================================')


def multiply_all_by_numb(numb, *args, text='* daugyba'):
    for elem in args:
        print(f'{numb * elem} {text}')

multiply_all_by_numb(7, 10, 11, 50)

print('============================================')

def return_list_of_multiplied_numbs(numb, *args, info=False):
    multiplied_numbs = [elem * numb for elem in args]
    if info:
        print(f"daugiklis: {numb}, args: {args}, rezultatas: {multiplied_numbs}")
    return multiplied_numbs

res = return_list_of_multiplied_numbs(7, 10, 11, 50)
print(res)  # [70, 77, 350]

res = return_list_of_multiplied_numbs(3, 10, 11, 50, info=True)  # daugiklis yra: 3 *args yra: (10, 11, 50) rezultatas yra: [30, 33, 150]
print(res)  # [30, 33, 150]

