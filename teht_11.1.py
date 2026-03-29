class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan kirjoittaja {self.kirjoittaja}")
        print(f"Kirjan sivumäärä {self.sivumäärä}")

class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Lehden päätoimittaja {self.päätoimittaja}")

#pääohjelma

aku = Lehti("Aku Ankka", "Aki Hyyppä")
hytti6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku.tulosta_tiedot()
print()
hytti6.tulosta_tiedot()



