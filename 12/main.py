#                                           Pamoka 12 try except sakinys


ivestis = '4'
try:
    skaicius = int(ivestis)
    res = skaicius / 0  # šis veiksmas sukels klaidą
except Exception as e:
    print("Mes crashinom, tačiau suvaldėm crashą")
    print(e.__class__)  # išspausdina klaidos klasę
    print(e)  # išspausdina klaidos pranešimą

print("Programa tęsia darbą")


print('=======================')

ivestis1 = input("Įveskite sveiką skaičių: ")
ivestis2 = input("Įveskite daliklį: ")

try:
    skaicius = int(ivestis1)
    daliklis = int(ivestis2)
    res = skaicius / daliklis
    print(f'Rezultatas: {res}')
except ValueError:
    print("Mes crashinom su ValueError")
    print("Paleiskite programą išnaujo ir ivestis padarykit kad tai būtų sveikas skaičius")
except ZeroDivisionError:
    print("Mes crashinom su ZeroDivisionError")
    print("Pakeiskite daliklį iš 0 į kitą")

print("Programa tęsia darbą")

print('=======================')

