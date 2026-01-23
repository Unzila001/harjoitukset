import random
x = int(input("Kerro noppa määrä: "))
summa = 0
for i in range (x):
    noppa = random.randint(1,6)
    summa += noppa
print("Noppien summa:" , summa)
