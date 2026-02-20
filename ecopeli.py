import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3307,
         database='flight_game',
         user='root',
         password='Unzila001',
         autocommit=True
         )

def hae_pelaajat():
    sql = f"SELECT * FROM game"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[4]}. Id {rivi[0]}")
    return

def luo_pelaaja():
    pelaajamäärä = f"select count(*) from game" #haetaan nykyisten pelaajien määrä
    kursori = yhteys.cursor()
    kursori.execute(pelaajamäärä)
    määrä = kursori.fetchall()[0][0]
    #print(määrä)
    nimi = input("Anna uuden pelaajan nimi: ")
    uusipelaaja = f"insert into game (id, screen_name) values ({määrä + 1}, 'dc')"

    kursori.execute(uusipelaaja)
    #tulos = kursori.fetchall()
    #print(tulos)

pelaaja = {
    "nimi": "",
    "akku": 0,
    "sijainti": "",
    "ekopisteet": 0
}

valinta = 10

while valinta != "0":
    print("Päävalikko:")
    print("1. Jatka peliä")
    print("2. Luo uusi pelaaja")
    print("0. Poistu pelistä")
    valinta = input()

    if valinta == "1":
        hae_pelaajat()

    elif valinta == "2":
        luo_pelaaja()
    elif valinta == "0":
        print("Heippa")
    else:
        print("Tuntematon valinta!")