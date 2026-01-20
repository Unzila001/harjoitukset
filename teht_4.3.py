num = []
while True:
    anna_num = input("Kerro numero: ")
    if anna_num == "":
        break
    num_1 = int(anna_num)
    num.append(num_1)

if num:
    print(f"Pienimmän luvut: {min(num)}")
    print(f"Suurimman luvut: {max(num)}")
else:
    print("Numeroita ei syötetty.")