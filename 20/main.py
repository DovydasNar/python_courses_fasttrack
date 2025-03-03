# #                                                            Mokyklos duomenų valdymo sistema
#
# import sqlite3
#
# conn = sqlite3.connect('mokykla.db')
# cursor = conn.cursor()
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS mokiniai (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     vardas TEXT,
#     pavarde TEXT,
#     klase INTEGER,
#     vidurkis INTEGER)
# ''')
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS mokytojai (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     vardas TEXT,
#     pavarde TEXT,
#     dalykas TEXT)
# ''')
#
# conn.commit()
#
# class Asmuo:
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#
#     def __str__(self):
#         return f'{self.vardas} {self.pavarde}'
#
#
# class Mokinys(Asmuo):
#     def __init__(self, vardas, pavarde, klase, vidurkis):
#         super().__init__(vardas, pavarde)
#         self.klase = klase
#         self.vidurkis = vidurkis
#
# class Mokytojas(Asmuo):
#     def __init__(self, vardas, pavarde, dalykas):
#         super().__init__(vardas, pavarde)
#         self.dalykas = dalykas
#
# def funkcijos_vykdymas(f):
#     def wrapper(*args, **kwargs):
#         print(f'Vykdoma funkcija: {f.__name__}')
#         return f(*args, **kwargs)
#     return wrapper
#
# @funkcijos_vykdymas
# def prideti_mokini(vardas, pavarde, klase, vidurkis):
#     try:
#         cursor.execute('''
#         INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis)
#         VALUES (?, ?, ?, ?)
#         ''', (vardas, pavarde, klase, vidurkis))
#         conn.commit()
#         print('Mokinys pridetas!')
#     except Exception as err:
#         print(f'Klaida {err} pridedant mokini.')
#
#
# @funkcijos_vykdymas
# def prideti_mokytoja(vardas, pavarde, dalykas):
#     try:
#         cursor.execute('''
#         INSERT INTO mokytojai (vardas, pavarde, dalykas)
#         VALUES (?, ?, ?)
#         ''', (vardas, pavarde, dalykas))
#         conn.commit()
#         print('Mokytojas pridetas!')
#     except Exception as err:
#         print(f'Klaida {err} pridedant mokytoja.')
#
# @funkcijos_vykdymas
# def gauti_visus_mokinius():
#     try:
#         cursor.execute('SELECT * FROM mokiniai')
#         mokiniai = cursor.fetchall()
#         for mokinys in mokiniai:
#             print(mokinys)
#     except Exception as err:
#         print(f'Klaida {err} gaunant mokinius')
#
# @funkcijos_vykdymas
# def gauti_visus_mokytojus():
#     try:
#         cursor.execute('SELECT * FROM mokytojai')
#         mokytojai = cursor.fetchall()
#         for mokytojas in mokytojai:
#             print(mokytojas)
#     except Exception as err:
#         print(f'Klaida {err} gaunant mokytojus.')
#
# @funkcijos_vykdymas
# def ieskoti_mokinio(vardas):
#     try:
#         cursor.execute('SELECT * FROM mokiniai WHERE vardas = ?', (vardas,))
#         rezultatas = cursor.fetchall()
#         if rezultatas:
#             for mokinys in rezultatas:
#                 print(mokinys)
#         else:
#             print(f'Mokinys {rezultatas} nerastas')
#     except Exception as err:
#         print(f'Klaida {err} ieskant mokinio.')
#
# @funkcijos_vykdymas
# def atnaujinti_mokinio_informacija(mokinio_id, nauja_klase):
#     try:
#         cursor.execute('''
#         UPDATE mokiniai SET klase = ? WHERE id = ?
#         ''', (mokinio_id, nauja_klase))
#         conn.commit()
#         print(f'Mokinio informacija atnaujinta.')
#     except Exception as err:
#         print(f'Klaida {err} atnaujinant informacija apie mokini.')
#
# @funkcijos_vykdymas
# def mokinio_trynimas(mokinio_id):
#     try:
#         cursor.execute('DELETE FROM mokiniai WHERE id = ?', (mokinio_id,))
#         conn.commit()
#         print('Mokinys istrintas.')
#     except Exception as err:
#         print(f'Klaida {err} istrinant mokini.')
#
# class MokiniuIteratorius:
#     def __init__(self):
#         self.index = 0
#         self.mokiniai = self.gauti_mokiniu_sarasa()
#
#     def gauti_mokiniu_sarasa(self):
#         cursor.execute('SELECT * FROM mokiniai')
#         return cursor.fetchall()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.mokiniai):
#             rezultatas = self.mokiniai[self.index]
#             self.index += 1
#             return rezultatas
#         else:
#             raise StopIteration
#
#
#
# if __name__ == '__main__':
# #     prideti_mokini('Dovydas', 'Narvilas', 11, 8.3)
# #     prideti_mokini('Deividas', 'Deividaitis', 8, 7.8)
# #     prideti_mokini('Petras', 'Petraitis', 5, 9.3)
# #     prideti_mokini('Zivile', 'Zivilaite', 12, 9.6)
# #     prideti_mokini('Ona', 'Onaite', 7, 7.9)
# # #
# #     prideti_mokytoja('Vilius', 'Vilaitis', 'Geografija')
# #     prideti_mokytoja('Paulius', 'Paulaitis', 'Istorija')
# #     prideti_mokytoja('Rasa', 'Rasiene', 'Matematika')
#
#
#     # print('Mokiniu sarasas:')
#     # gauti_visus_mokinius()
#     # #
#     # print('Mokytoju sarasas:')
#     # gauti_visus_mokytojus()
#     #
#     # print('Ieskoti mokinio:')
#     # ieskoti_mokinio('Dovydas')
#
#     # print('Trinti mokini:')
#     # mokinio_trynimas(2)
#     #
#     # print('Atnaujinti klase')
#     # atnaujinti_mokinio_informacija(1, 10)
#     #
#     #
#     # print('Iteravimas per sarasa')
#     # iteratorius = MokiniuIteratorius()
#     # for mokinys in iteratorius:
#     #     print(mokinys)
#
#     gauti_visus_mokinius()
#     mokinio_trynimas(10)
#     gauti_visus_mokinius()
#     mokinio_trynimas(6)
#     gauti_visus_mokinius()
#
#
#
# conn.close()
#
#
#


















