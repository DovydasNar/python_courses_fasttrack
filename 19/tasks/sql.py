

# 1 TASK
import sqlite3

conn = sqlite3.connect('mokykla.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS mokykla (
    pavadinimas TEXT,
    adresas TEXT,
    mokiniu_skaicius INTEGER
)
''')

def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    cursor.execute(''' 
     INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius)
     VALUES (?, ?, ?)
     ''', (pavadinimas, adresas, mokiniu_skaicius))
    conn.commit()

prideti_mokykla('Vilniaus gimnazija', 'Vilniaus g. 10', 500)
prideti_mokykla('Kauno gimnazija', 'Kauno g. 5', 800)

def rodyti_mokyklas(min_mokiniu_skaicius=0):
    cursor.execute('''
    SELECT * FROM mokykla WHERE mokiniu_skaicius > ?
    ''', (min_mokiniu_skaicius,))

    mokyklos = cursor.fetchall()

    for mokykla in mokyklos:
        print(f'Mokykla: {mokykla[0]}, Adresas: {mokykla[1]}, mokiniu skaicius: {mokykla[2]}')

def atnaujinti_mokiniu_skaiciu(pavadinimas, naujas_mokiniu_skaicius):
    cursor.execute('''
    UPDATE mokykla
    SET mokiniu_skaicius = ?
    WHERE pavadinimas = ?
    ''', (naujas_mokiniu_skaicius, pavadinimas))

    if cursor.rowcount > 0:
        print(f'Mokiniu skaicius mokykloje:{pavadinimas} sekmingai atnaujintas i {naujas_mokiniu_skaicius}')
    else:
        print(f'Mokykla su pavadinimu {pavadinimas} nerasta.')




print('Visos mokyklos:')
rodyti_mokyklas()

print('Mokyklos su daugiau nei 600 zmoniu:')
rodyti_mokyklas(600)


atnaujinti_mokiniu_skaiciu('Kauno gimnazija', 1200)

rodyti_mokyklas()



conn.close()






