def apversti_teksta(tekstas):
    return tekstas[::-1]

def apversti_sakini(tekstas):
    return " ".join(tekstas.split()[::-1])

print(apversti_teksta("ABC"))
print(apversti_sakini("Labas Pasauli Dabar!!!"))

def i_didziasias(tekstas, funkcija=None):
    if funkcija:
        tekstas = funkcija(tekstas)
    return tekstas.upper()

print(i_didziasias("abc", funkcija=apversti_teksta))
print(i_didziasias("Labas Pasauli Dabar!!!", funkcija=apversti_sakini))


print('==================================================================')


# Paprastas Dekoratorius
def registratorius(funkcija):
    def apvalkalas(argumentas):
        rezultatas = funkcija(argumentas)
        if rezultatas % 2 == 0:
            print(f"{rezultatas} yra lyginis")
        else:
            print(f"{rezultatas} yra nelyginis")
        return rezultatas
    return apvalkalas

@registratorius
def kvadratu(skaicius):
    return skaicius ** 2

print(kvadratu(8))


print('==================================================================')

# Pavyzdys: Vartotojo Apibrėžtas Iteratorius
class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    def __iter__(self):
        return iter([self.vardas, self.pavarde, self.pareigos])

darbuotojas = Darbuotojas("Jonas", "Jonaitis", "Programuotojas")
for savybe in darbuotojas:
    print(savybe)

print('==================================================================')
# Pavyzdys: Vartotojo Apibrėžtas Iteratorius
class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    def __iter__(self):
        return iter([self.vardas, self.pavarde, self.pareigos])

darbuotojas = Darbuotojas("Jonas", "Jonaitis", "Programuotojas")
for savybe in darbuotojas:
    print(savybe)


print('==================================================================')
# generatorine funkcija
def skaiciuok_iki(max_reiksme):
    skaicius = 0
    while skaicius < max_reiksme:
        yield skaicius
        skaicius += 1

for numeris in skaiciuok_iki(5):
    print(numeris)
