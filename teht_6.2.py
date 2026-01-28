import random
def heittää_nopa(tahko):
    return random.randint(1, tahko)

#pääohjelma
max_luku = int(input("Anna nopan tahkojen lukumäärä:  "))
heittää = 0
while heittää != max_luku:
    heittää = heittää_nopa(max_luku)
    print(heittää)

