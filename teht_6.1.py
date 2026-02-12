import random
def heittää_nopa():
    return random.randint(1,6)

#Pääohjelma
heittää = 0
while heittää != 6:
    heittää = heittää_nopa()
    print((heittää))



#Ope method
while True:
    luku = heittää_nopa()
    print(luku)
    if luku == 6:
        break