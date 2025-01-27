# print('Hello world!')
#                                       Funkcijos ir jų naudojimas

#                                                   uzduotis 2

# def sudaugink(x,y):
#     if not x or not y:
#         return
#     return x * y
#
#
# suma = sudaugink(5, 10)
#
# if suma:
#     print(f'Suma yra: {suma}')
# else:
#     print('Numbers are wrong or not provided')
#                                                   ====================
# def say_hello_to_two(name1, name2):
#     if not name1 or not name2:
#         return
#     hello_string = f'Hello to {name1} and hello to {name2}'
#     return hello_string
#
# res = say_hello_to_two('Dovydas', 'Zivile')
# print(res)


#                   Numatytosios reikšmės ir keyword argumentai


# def greet(name='User'):
#     print(f'Hello, {name}!')
#
# greet('Dovydas')
# greet()


# def priimk_pacienta(pacientas, gydytojas='gyd. Pagalnutylenis'):
#     irasas_gyd_zurnale = f'Pacientas {pacientas}, prieme {gydytojas}'
#     return irasas_gyd_zurnale
#
# res = priimk_pacienta('Adomas')
# print(res)
#
# res = priimk_pacienta('Rolandas')
# print(res)
#
# res = priimk_pacienta('Izidorius', 'Pakaitenis')
# print(res)
#
# res = priimk_pacienta(
#     gydytojas='gyd. Zivile',
#     pacientas='Dovydas'
# )
# print(res)

#                       3 task

def trys_sveikinimai(name1, name2, name3):
    res = f'Labas {name1}!, Labas {name2}!, Labas {name3}!'
    return res

print(trys_sveikinimai('Dovydas', 'Tomas', 'Raidas'))

print('===========')

#                       4 task

def sveikink_su_pavadinimu(vardas, pavadinimas='drauge'):
    zinute = f'Labas, {vardas}! Ka veiki, {pavadinimas}?'
    return zinute

res = sveikink_su_pavadinimu('Dovydas')
print(res)

res = sveikink_su_pavadinimu('Raidas', 'kolega')
print(res)