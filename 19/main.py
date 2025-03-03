# prisijungimas prie duom bazes SQL


import sqlite3

# Prisijungimas prie duomenų bazės
conn = sqlite3.connect("pavyzdys.db")
c = conn.cursor()

# Lentelės sukūrimas
c.execute('''CREATE TABLE IF NOT EXISTS studentai (
                vardas TEXT,
                pavarde TEXT,
                klase INTEGER)''')

conn.commit()
conn.close()


# duomenu iterpimas (INSERT)

# import sqlite3
#
# # Įterpiamas naujas studentas
# with sqlite3.connect("pavyzdys.db") as conn:
#     c = conn.cursor()
#     c.execute("INSERT INTO studentai (vardas, pavarde, klase) VALUES (?, ?, ?)",
#               ("Jonas", "Jonaitis", 10))
#
# # duomenu skaitymas (SELECT)
#
# import sqlite3
#
# # Nuskaitomi visi studentai
# with sqlite3.connect("pavyzdys.db") as conn:
#     c = conn.cursor()
#     for row in c.execute("SELECT * FROM studentai"):
#         print(row)
#
# # duomenu atnaujinimas (UPDATE)
#
# import sqlite3
#
# # Atnaujinamas studento klasės lygis
# with sqlite3.connect("pavyzdys.db") as conn:
#     c = conn.cursor()
#     c.execute("UPDATE studentai SET klase = 11 WHERE vardas = 'Jonas'")
#
# # Patikriname atnaujinimą
# with sqlite3.connect("pavyzdys.db") as conn:
#     c = conn.cursor()
#     for row in c.execute("SELECT * FROM studentai"):
#         print(row)
#
#
# # DUOMENU ISTRYNIMAS (DELETE)
#
# import sqlite3
#
# # Ištrinamas studentas pagal vardą
# with sqlite3.connect("pavyzdys.db") as conn:
#     c = conn.cursor()
#     c.execute("DELETE FROM studentai WHERE vardas = 'Jonas'")
#
# # Patikriname trynimą
# with sqlite3.connect("pavyzdys.db") as conn:
#     c = conn.cursor()
#     for row in c.execute("SELECT * FROM studentai"):
#         print(row)
#
# # LENTELES SUKURIMAS
#
# import sqlite3
#
# # Sukuriama lentelė mokytojams
# with sqlite3.connect("pavyzdys.db") as conn:
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS mokytojai (
#             vardas TEXT,
#             pavarde TEXT,
#             dalykas TEXT
#         )
#     ''')
#
#
# # NAUDOJIMOSI PRAKTIKOS. PARAMETERIZUOTA UZKLAUSA
#
# import sqlite3
#
# # Įterpiamas mokytojas su saugia parametrizuota užklausa
# with sqlite3.connect("pavyzdys.db") as conn:
#     c = conn.cursor()
#     c.execute("INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)",
#               ("Tomas", "Tomaitis", "Matematika"))
#
#
# # UZDARYMO PRAKTIKA
#
# # Ryšio uždarymas
# conn = sqlite3.connect("pavyzdys.db")
# conn.close()
#

