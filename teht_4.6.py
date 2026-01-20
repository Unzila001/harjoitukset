import random
pisteet = int(input("Anna satunnaisten pisteiden määrä: "))
ympyra_sisalla = 0
for _ in range(pisteet):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        ympyra_sisalla += 1
pi_laskettu = 4 * ympyra_sisalla / pisteet

print(f"Piin likiarvo: {pi_laskettu}")