while True:
    tuumia = float(input("Kerro tuumia: "))
    if tuumia < 0:
        print("Ohjelma lopettaa.")
        break
    senttimetre = tuumia * 2.54
    print(f"{tuumia} tuumia = {senttimetre:.2f} cm")


num = 1
x = 0
while x >= 0:
    x = int(input("Give value in inches. Negative value will terminate: "))
    if x < 0:
        break

    num = x * 2.54

    print(num)
