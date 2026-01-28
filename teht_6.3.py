def neste_gallonaa(gallon):
    return gallon * 3.785

#pääohjelma
gallon = float(input("Anna määrä gallonoina: "))
while gallon >= 0:
    litra = neste_gallonaa(gallon)
    print(f"{gallon} gallon on {litra:.2f} litraa.")
    gallon = float(input("Anna määrä gallonoina: "))
