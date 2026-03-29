import random

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_tiedot(self):
        print(f"rekisteritunnus: {self.rekisteritunnus}")
        print(f"huippunopeus   : {self.huippunopeus}")
        print(f"nopeus         : {self.nopeus}")
        print(f"matka          : {self.matka}")

    def kiihdytä(self, nopeus):
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = nopeus


    def kulje(self, aika):
        self.matka += (self.nopeus * aika)

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankki = tankki

#pääohjelma

Sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ABC-15", 165, 32.3)

Sähköauto.kiihdytä(100)
polttomoottoriauto.kiihdytä(120)

Sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauto {Sähköauto.rekisteritunnus} ajoi {Sähköauto.matka} km")
print(f"Polttomoottoriauto {polttomoottoriauto.rekisteritunnus} ajoi {polttomoottoriauto.matka} km")