lentoasemat = {}
while True:
    print("\nValitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoasema")
    print("3. Lopeta")

    valinta = input("Valintasi: ")
    if valinta == "1":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Lentoasema eo löydy.")


    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break
    else:
        print("Virheellinen valinta.")