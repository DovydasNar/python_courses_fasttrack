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




