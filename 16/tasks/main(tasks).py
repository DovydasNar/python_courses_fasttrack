class Gyvunas:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def judeti(self):
        print(f'Gyvunas {self.vardas} juda!')

class Kate(Gyvunas):
    def miaukseti(self):
        print(f'Kate vardu {self.vardas} sako Miau! ')

class Suo(Gyvunas):
    def lot(self):
        print(f'Suo {self.vardas} sako Au au!')

cat = Kate('Dumas', 10)
dog = Suo('Kingas', 8)

cat.miaukseti()
cat.judeti()

dog.lot()
dog.judeti()


