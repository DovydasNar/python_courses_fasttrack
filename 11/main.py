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



