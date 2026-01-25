luvut = []
while True:
    num = input("Kerro luvut: ")
    if num == "":
        break
    luvut.append(int(num))
luvut.sort(reverse=True)
viisi_suuri = luvut[:5]
print("Viisi suuri luvut: ", viisi_suuri)