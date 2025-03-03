

# task 1

class Zmogus:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def prisistatyti(self):
        return f'{self.vardas} {self.pavarde}'



zmogus1 = Zmogus('Dovydas', 'Narvilas')

# print(zmogus1.prisistatyti())

class Studentas(Zmogus):
    def __init__(self, vardas, pavarde, studiju_programa):
        self.vardas = vardas
        self.pavarde = pavarde
        self.studiju_programa = studiju_programa

    def prisistatyti(self):
        return f'As esu {self.vardas} {self.pavarde}, studijuoju - {self.studiju_programa}'


studentas1 = Studentas('Dovydas', 'Narvilas', 'FullStack programavimas')

# print(studentas1.prisistatyti())

class Universitetas:
    def __init__(self):
        self.studentai = []

    def prideti_studenta(self, studentas):
        self.studentai.append(studentas)

    def rodyti_visus_studentus(self):
        for studentas in self.studentai:
            print(studentas.prisistatyti())



studentas1 = Studentas('Dovydas', 'Narvilas', 'Programavimas')
studentas2 = Studentas('Tomas', 'Tomaitis', ' Dizainas')
studentas3 = Studentas('Petras', 'Petraitis', 'Vadyba')
studentas4 = Studentas('Juozas', 'Juozaitis', 'Inzinerija')


universitetas = Universitetas()

universitetas.prideti_studenta(studentas1)
universitetas.prideti_studenta(studentas2)
universitetas.prideti_studenta(studentas3)

universitetas.rodyti_visus_studentus()


print('===============================================================')

# task 2

import pickle

class Knyga:
    def __init__(self, pavadinimas, autorius, metai):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.metai = metai

    def __str__(self):
        return f'"{self.pavadinimas}" - {self.autorius} ({self.metai})'

class Biblioteka:
    def __init__(self):
        self.knygos = []
        self.failas = "biblioteka.pkl"
        self.ikelti_duomenis()

    def prideti_knyga(self, knyga):
        self.knygos.append(knyga)
        self.issaugoti_duomenis()

    def istrinti_knyga(self, pavadinimas):
        self.knygos = [knyga for knyga in self.knygos if knyga.pavadinimas != pavadinimas]
        self.issaugoti_duomenis()

    def rodyti_knygas(self):
        if not self.knygos:
            print("Bibliotekoje nėra knygų.")
        else:
            for knyga in self.knygos:
                print(knyga)

    def ieskoti_knygos(self, uzklausa):
        rezultatai = [knyga for knyga in self.knygos if uzklausa.lower() in knyga.pavadinimas.lower() or uzklausa.lower() in knyga.autorius.lower()]
        if rezultatai:
            for knyga in rezultatai:
                print(knyga)
        else:
            print("Knyga nerasta.")

    def issaugoti_duomenis(self):
        with open(self.failas, "wb") as f:
            pickle.dump(self.knygos, f)

    def ikelti_duomenis(self):
        try:
            with open(self.failas, "rb") as f:
                self.knygos = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.knygos = []

# Testavimas
biblioteka = Biblioteka()

biblioteka.prideti_knyga(Knyga("Haris Poteris", "J.K. Rowling", 1997))
biblioteka.prideti_knyga(Knyga("Žiedų Valdovas", "J.R.R. Tolkien", 1954))

print("\nVisos knygos bibliotekoje:")
biblioteka.rodyti_knygas()

biblioteka.ieskoti_knygos("Tolkien")

biblioteka.istrinti_knyga("Haris Poteris")
biblioteka.rodyti_knygas()








