

class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self._atlyginimas = None
        self.__asmens_kodas = None

    def get_atlyginimas(self):
        if self._atlyginimas:
            return self._atlyginimas
        return 'Neaisku'

    def _set_atlyginimas(self, suma):
        if int(suma) > 0:
            self._atlyginimas = suma
        else:
            print('Atlyginimas negali būti <=0')

    def get_asmens_kodas(self):
        if self.__asmens_kodas:
            return self.__asmens_kodas
        return 'Neaisku'

    def _set_asmens_kodas(self, asmens_kodas):
        if int(asmens_kodas) > 0:
            self.__asmens_kodas = asmens_kodas
        else:
            print('Atlyginimas negali būti <=0')

    def __str__(self):
        return f'Vardas: {self.vardas} Pavarde: {self.pavarde} Pareigos: {self.pareigos} {self.get_atlyginimas()} {self.get_asmens_kodas()}'

    def __reset_asmens_kodas(self):
        self.__asmens_kodas = '123123123'

class Vadovas(Darbuotojas):
    def __init__(self, vardas, pavarde, pareigos, departamentas):
        super().__init__(vardas, pavarde, pareigos)
        self.departamentas = departamentas

    def super_change_of_atlyginmas(self):
        self._atlyginimas = '123412341234'

class Sarasas:
    def __init__(self):
        self.super_sarasas = []

    def change_elemntu_atlyginimas(self):
        for i in self.super_sarasas:
        #     i._atlyginimas
        #     i.__asmens_kodas
            print(i)

vadovas1 = Vadovas('Jonas',' Jonaitis', 'Programuotojas', 'IT')
vadovas1.super_change_of_atlyginmas()

# AttributeError BECAUSE METHOD IS PRIVATE. COMMENT vadovas1.__reset_asmens_kodas() OR MAKE __reset_asmens_kodas NOT PRIVATE METHOD
# vadovas1.__reset_asmens_kodas()


print(vadovas1)

elem = Sarasas()
elem.super_sarasas.append(vadovas1)

print(elem.change_elemntu_atlyginimas())

