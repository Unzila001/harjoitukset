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

#pääohjelma
autot = []
for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100, 200))
    autot.append(auto)

print("Kilpailu alkaa! (läksy)")

kilpailu_ohi = False
tunti = 0

while not kilpailu_ohi:
    tunti += 1

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu_ohi = True

# tulostus taulukkona
print("\nKilpailu päättyi!\n")
print(f"{'Rekisteri':<10} {'Huippu':<10} {'Nopeus':<10} {'Matka':<10}")

for auto in autot:
    print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<10} {auto.nopeus:<10} {int(auto.matka):<10}")