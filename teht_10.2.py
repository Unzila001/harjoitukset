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

class Talo:
    def __init__(self, yllä, alaa, hissi_lkm):
        self.yllä = yllä
        self.alaa = alaa
        self.hissit = []

        for i in range(hissi_lkm):
            hissi = Hissi(alaa, yllä)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissi_num, kohde_kerros):
        hissi = self.hissit[hissi_num - 1]
        hissi.siirry_kerrokseen(kohde_kerros)
#pääohjelma

talo = Talo(1,10,3)
talo.aja_hissiä(1,5)
talo.aja_hissiä(2,8)
talo.aja_hissiä(1,1)


