class Hissi:
    def __init__(self, yllä, alaa):
        self.yllä = yllä
        self.alaa = alaa
        self.nyt = alaa #aloita alimmasta kerroksesta

    def kerros_ylös(self):
        if self.nyt < self.yllä:
            self.nyt += 1
            print(f"Hissi on nyt {self.nyt} kerroksessa.")

    def kerros_alas(self):
        if self.nyt > self.alaa:
            self.nyt -= 1
            print(f"Hissi on nyt {self.nyt} kerroksessa.")

    def siirry_kerrokseen(self, kerros):
        while self.nyt < kerros:
            self.kerros_ylös()
        while self.nyt > kerros:
            self.kerros_alas()

#pääohjelma

h = Hissi(10,1)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)


