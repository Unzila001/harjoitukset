#Kuhan alamitta senttimetreinä
alamitta = 37

#kysy pituus käytäjältä
kuhan_pituus = float(input("Anna Kuhan pituuden senttimetreinä: "))
if kuhan_pituus < alamitta:
    puuttuu = alamitta - kuhan_pituus
    print("Kuha on alamittainen.")
    print("Laskea kuhan takaisin järveen.")
    print(f"Kuhasta puuttuu {puuttuu:.2f} cm alimmasta sallitusta pyyntimitasta.")
else:
    print("Kuha on sallittua pyyntimittaa.")