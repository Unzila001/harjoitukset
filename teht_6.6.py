import math

def pizza_hinnan(halkaisija_cm, hinta_eur):
    pinta_ala = math.pi * (halkaisija_cm / 2) ** 2
    pinta_m2 = pinta_ala / 1000 # cm^2 to m^2
    hinta = hinta_eur / pinta_m2
    return hinta

#pääohjelma
halkaisija_1 = float(input("Anna pizzan 1 halkaisija (cm): "))
hinta_1 = float(input("Anna pizzan 1 hinta eur (cm): "))

halkaisija_2 = float(input("Anna pizzan 2 halkaisija (cm): "))
hinta_2 = float(input("Anna pizzan 2 hinta eur (cm): "))

hinta1 = pizza_hinnan(halkaisija_1, hinta_1)
hinta2 = pizza_hinnan(halkaisija_2, hinta_2)

print(f"Pizzan 1 hinta: {hinta1:.2f} €/m^2")
print(f"Pizzan 2 hinta: {hinta2:.2f} €/m^2")

if hinta1 < hinta2:
    print("Pizza 1 antaa paremman vastineen rahalle")
elif hinta2 < hinta1:
    print("Pizza 2 antaa paremman vastineen rahalle")
else:
    print("Molemmat pizzat antavat rahalle yhtä paljon vastinetta")
