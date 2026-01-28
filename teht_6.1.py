import random
def heittää_nopa():
    return random.randint(1,6)

#Pääohjelma
heittää = 0
while heittää != 6:
    heittää = heittää_nopa()
    print((heittää))