import random
Arvaa_num = random.randint(1, 10)
while True:
    luvut = int(input("Arvaa numero väliltä 1-10: "))
    if luvut < Arvaa_num:
        print("Liian pieni arvaus")
    elif luvut > Arvaa_num:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break