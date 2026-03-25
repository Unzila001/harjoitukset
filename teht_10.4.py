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

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, aika):
        self.matka += (self.nopeus * aika)

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilannne(self):
        print(f"{'Rekisteri':<10} {'Huippu':<10} {'Nopeus':<10} {'Matka':<10}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<10} {auto.nopeus:<10} {int(auto.matka):<10}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

#pääohjelma

autot = []
for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100, 200))
    autot.append(auto)

print("Kilpailu alkaa! (läksy)")

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0

while not kilpailu.kilpailu_ohi():
    tunti += 1
    kilpailu.tunti_kuluu()

    # optional: print every 10 hours
    if tunti % 10 == 0:
        print(f"\nTilanne {tunti} tunnin jälkeen:")
        kilpailu.tulosta_tilannne()

# final result
print("\nKilpailu päättyi!\n")
kilpailu.tulosta_tilannne()