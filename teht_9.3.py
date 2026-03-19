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
x = Auto("ABC-123", 142)
x.kiihdytä(60)
x.kulje(1.5)
x.tulosta_tiedot()