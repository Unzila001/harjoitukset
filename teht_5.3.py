luvut = int(input("Kerro kokonaisluvut: "))
if luvut < 2:
    print("Luvut eivät ole alkulukuja")
else:
    alkuluka = True
    for i in range(2,luvut):
        if luvut % i == 0:
            alkuluka = False
            break
    if alkuluka:
        print("Luvut on alkulukuja")
    else:
        print("Luvut eivät ole alkulukuja")
