class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

#pääohjelma
x = Auto("ABC-123", 142)

print(x.rekisteritunnus)
print(x.huippunopeus)
print(x.nopeus)
print(x.matka)
