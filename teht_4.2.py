while True:
    tuumia = float(input("Kerro tuumia: "))
    if tuumia < 0:
        print("Ohjelma lopettaa.")
        break
    senttimetre = tuumia * 2.54
    print(f"{tuumia} tuumia = {senttimetre:.2f} cm")
