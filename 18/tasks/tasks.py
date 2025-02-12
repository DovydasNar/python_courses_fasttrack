# 4 uzduotis


class Matematika:
    @staticmethod
    def sudeti(a, b):
        return a + b

    @staticmethod
    def atimti(a, b):
        return a - b

    @staticmethod
    def dauginti(a, b):
        return a * b

    @staticmethod
    def dalinti(a, b):
        if b == 0:
            return 'Klaida, dalyba is 0 negalima'
        return a / b

    @staticmethod
    def ar_lyginis(skaicius):
        return skaicius % 2 == 0


print(Matematika.atimti(5, 3))
print(Matematika.sudeti(5, 3))
print(Matematika.dalinti(5, 3))
print(Matematika.dauginti(5, 3))

print(Matematika.ar_lyginis(5))
print(Matematika.ar_lyginis(4))


# 5 uzduotis

class Automobilis:
    def __init__(self, marke, modelis, metai):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai

    @classmethod
    def sukurti_is_string(cls, eilute):
        marke, modelis, metai = eilute.split()
        return cls(marke, modelis, metai)

    @classmethod
    def naujausias_modelis(cls, auto_sarasas):
        auto_objektai = [cls.sukurti_is_string(eilute) for eilute in auto_sarasas]
        naujausias = max(auto_objektai, key=lambda auto: auto.metai)
        return naujausias

    def __str__(self):
        return f'Automobilio marke: {self.marke}, modelis: {self.modelis}, metai: {self.metai}'

autos = [
'Ford Mondeo 2005',
'Volkswagen Tiguan 2012',
'Porsche 911 2018'
]

automobilis = 'Ford Mondeo 2005'

auto = Automobilis.sukurti_is_string(automobilis)
print(auto)

print('-' * 30)

naujausias = Automobilis.naujausias_modelis(autos)
print(naujausias)



print('==================================')

# 1. Funkcijos kaip Pirmos Klasės Objektai

def prideti_zenkliuka(tekstas):
    return tekstas + '*'


def apversti_teksta(tekstas):
    return tekstas[::-1]



def apdoroti_teksta(tekstas, funkcija=None):
    if funkcija:
        return funkcija(tekstas)
    return tekstas.lower()



def keli_apdorojimai(tekstas, *funkcijos):
    for funkcija in funkcijos:
        tekstas = funkcija(tekstas)
        return tekstas

tekstas = 'Hello World!'

print(apdoroti_teksta(tekstas))
print(apdoroti_teksta(tekstas, prideti_zenkliuka))
print(apdoroti_teksta(tekstas, apversti_teksta))
print(keli_apdorojimai(tekstas, apdoroti_teksta, prideti_zenkliuka, apversti_teksta, ))


print('==================================')

# 3 task

def sekimo_dekoratorius(funkcija):
    def vidine_funkcija(*args, **kwargs):
        print(f'Vykdoma funkcija {funkcija.__name__}')

        rezultatas = funkcija(*args, **kwargs)

        print('Funkcija baigta.')

        return rezultatas

    return vidine_funkcija



@sekimo_dekoratorius
def dauginti(a,b):
    return a * b


@sekimo_dekoratorius
def dalinti(a,b):
    if b == 0:
        return 'Klaida, dalyba is 0 negalima'
    return a / b


print(dalinti(5,5))
print(dauginti(5,5))

print('==================================')

class SkaiciuSekosIteratorius:
    def __init__(self, pradinis, galinis):
        self.pradinis = pradinis
        self.galinis = galinis
        self.current = pradinis

    def __iter__(self):
        self.current = self.pradinis
        return self

    def __next__(self):
        if self.current > self.galinis:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

    def atgaline_seka(self):
        return list(range(self.galinis, self.pradinis -1, -2))


iteratorius = SkaiciuSekosIteratorius(1, 10)

for skaicius in iteratorius:
    print(skaicius)

print('============================================================')

print(iteratorius.atgaline_seka())




