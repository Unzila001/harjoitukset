luvut = []
while True:
    num = input("Kerro luvut: ")
    if num == "":
        break
    luvut.append(int(num))
luvut.sort(reverse=True)
viisi_suuri = luvut[:5]
print("Viisi suuri luvut: ", viisi_suuri)

#Ope method
"""luvut = []
syöte = input("Anna kokonaislulu (tyhjä lopettaa): ")
while syöte != "":
    luku = int(syöte)
    luvut.append(luku)
    syöte = input("Anna kokonaislulu (tyhjä lopettaa): ")

luvut.sort(reverse=True)
for i in range (5):
    print(luvut[i])"""