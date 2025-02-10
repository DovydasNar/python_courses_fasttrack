# task 1


class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []

    def prideti_pazymi(self, pazimys):
        if 1 <= pazimys <= 10:
            self._pazymiai.append(pazimys)
        else:
            print('Pazimys turi buti skaicius nuo 1 iki 10')

    def rodyti_vidurki(self):
        if not self._pazymiai:
            return 0
        return sum(self._pazymiai) / len(self._pazymiai)

studentas1 = Studentas('Dovydas', 'Narvilas')

studentas1.prideti_pazymi(10)
studentas1.prideti_pazymi(7)
studentas1.prideti_pazymi(9)
studentas1.prideti_pazymi(5)


print(f'Studentas: {studentas1.vardas} {studentas1.pavarde}, pazymiu vidurkis: {studentas1.rodyti_vidurki()}')


class StudentasLyderis(Studentas):
    def __init__(self, vardas, pavarde, bonus_taskai=0):
        super().__init__(vardas, pavarde)
        self.bonus_taskai = bonus_taskai

    def rodyti_vidurki(self):
        vidurkis = super().rodyti_vidurki()
        return vidurkis + self.bonus_taskai



studentas2 = StudentasLyderis('Romas', 'Dambrauskas', bonus_taskai=2)

studentas2.prideti_pazymi(5)
studentas2.prideti_pazymi(10)
studentas2.prideti_pazymi(7)

print(f'Studentas: {studentas2.vardas} {studentas2.pavarde}, pazymiu vidurkis su bonusu: {studentas2.rodyti_vidurki()}')


print('=================================================================================================================================')

# 1.2. task

class BankoSaskaita:
    def __init__(self, savininkas):
        self.savininkas = savininkas
        self.__balansas = 0

    def gauti_balansa(self):
        return self.__balansas

    def prideti_pinigus(self, suma):
        if suma > 0:
            self.__balansas += suma
        else:
            print('Negalima prideti neigiamos sumos.')

    def nuskaiciuoti_pinigus(self, suma):
        if 0 < suma <= self.__balansas:
            self.__balansas -= suma
        else:
            print('Nepakankamas likutis')

mano_saskaita = BankoSaskaita('Dovydas')

print(f'Saskaita: {mano_saskaita.savininkas}, balansas: {mano_saskaita.gauti_balansa()}')

mano_saskaita.prideti_pinigus(500)

print(f'Saskaita: {mano_saskaita.savininkas}, balansas: {mano_saskaita.gauti_balansa()}')

mano_saskaita.prideti_pinigus(125)

print(f'Saskaita: {mano_saskaita.savininkas}, balansas: {mano_saskaita.gauti_balansa()}')

mano_saskaita.nuskaiciuoti_pinigus(1500)

print(f'Saskaita: {mano_saskaita.savininkas}, balansas: {mano_saskaita.gauti_balansa()}')

mano_saskaita.nuskaiciuoti_pinigus(1200)

mano_saskaita.prideti_pinigus(-1000)


print('=================================================================================================================================')


# 3 task

class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = max(atlyginimas, 500)

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, naujas_atlyginimas):
        if naujas_atlyginimas >= 500:
            self.__atlyginimas = naujas_atlyginimas
        else:
            print('Atlyginimas negali buti mazesnis nei 500')

    @property
    def mokesciai(self):
        return self.__atlyginimas * 0.2

darb1 = Darbuotojas('Dovydas', 'Narvilas', 2000)

print(f'Darbuotojas {darb1.vardas} {darb1.pavarde}, atlyginimas: {darb1.atlyginimas}')


darb1.atlyginimas = 1000

print(f'Darbuotojas {darb1.vardas} {darb1.pavarde}, atlyginimas: {darb1.atlyginimas}')

darb1.atlyginimas = 2500

print(f'Darbuotojas {darb1.vardas} {darb1.pavarde}, atlyginimas: {darb1.atlyginimas}, mokesciai nuo atlyginimo: {darb1.mokesciai}')

























