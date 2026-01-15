#kysy kolme kokonaisluku
x = int(input("Anna eka kokonaisluku: "))
y = int(input("Anna toka kokonaisluku: "))
z = int(input("Anna kolmas kokonaisluku: "))

#summa, tulo, keskiarvo
summa = (x+y+z)
tulo = (x*y*z)
keskiarvo = (summa / 3)

#Tulos
print(f"Kolmen kokonaisluvun summa on {summa}")
print(f"Kolmen kokonaisluvun tulo on {tulo}")
print(f"Kolmen kokonaisluvun keskiarvo on {keskiarvo:.3f}")