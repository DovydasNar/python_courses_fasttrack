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

# def trys_sveikinimai(name1, name2, name3):
#     res = f'Labas {name1}!, Labas {name2}!, Labas {name3}!'
#     return res
#
# print(trys_sveikinimai('Dovydas', 'Tomas', 'Raidas'))
#
# print('===========')
#
# #                       4 task
#
# def sveikink_su_pavadinimu(vardas, pavadinimas='drauge'):
#     zinute = f'Labas, {vardas}! Ka veiki, {pavadinimas}?'
#     return zinute
#
# res = sveikink_su_pavadinimu('Dovydas')
# print(res)
#
# res = sveikink_su_pavadinimu('Raidas', 'kolega')
# print(res)

#                                                   ====================

#                           Loginiai jungikliai funkcijose

# def dalink_spec(sk1, sk2, iki_sveiko_sk=False):
#     if not iki_sveiko_sk:
#         return sk1 / sk2
#     return sk1 // sk2
#
# print(dalink_spec(777, 5, True))
#
# def button_modify_product(product, inform_client=False):
#     if inform_client:
#         print('Product was modified succesfully by the system!')
#         return product * 50
#
# button_modify_product(product='Tapkes',inform_client=True)
# button_modify_product('Tapkes')

#                                                   Docstringai funkcijose

# def say_hello(name):
#     """
#      Priima vardą ir atspausdina pasisveikinimą.
#      :param name: str - vardas žmogaus
#      :return: None
#      """
#     return print(name)
#
# say_hello('Dovydas')
#
#
# #                                                       Type hints ir anotacijos
#
# def add(x: int, y: int):
#     return x + y
#
# add(2,5)
#
# print(add(1,5))
#
#
# def add(x: int, y: int) -> int:
#     return x + y
#
#
# a = 2 + add(1,3)

#                       task 5

def skaiciuoti_sumos_tipa(x: int,y: int, tik_teigiama=False):
    """
    Suskaiciuoja sumos tipa, jei tik_teigiama=True - ir jeigu neigiama skaiciu gauname, grazina 0.
    :param x:
    :param y:
    :param tik_teigiama:
    :return:

    """
    res = x + y
    if tik_teigiama:
        res = max(res, 0)
    return res

print(skaiciuoti_sumos_tipa(5,5))
print(skaiciuoti_sumos_tipa(-10,5))
print(skaiciuoti_sumos_tipa(-10,5, tik_teigiama=True))
print(skaiciuoti_sumos_tipa(5,5, tik_teigiama=True))


print('============================')

#                       task 6

def apskaiciuok_vidurki(skaiciai:int):
    if not skaiciai:
        return 0
    res = sum(skaiciai) / len(skaiciai)
    return res

print(apskaiciuok_vidurki([1,2,10,20]))
print(apskaiciuok_vidurki([]))
print(apskaiciuok_vidurki([1,1,1,1, 200]))

print('============================')


#                       task 7

def prideti_zodi(tekstas: str, zodis: str) -> str:
    if tekstas == '':
        return zodis
    else:
        return tekstas + ' ' + zodis


print(prideti_zodi('Sveiki, kaip sekasi?', 'Dovydai'))





