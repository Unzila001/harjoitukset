import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3307,
    database='flight_game',
    user='root',
    password='Unzila001',
    autocommit=True
)

kursori = yhteys.cursor()
kursori.execute("SELECT DATABASE()")
print("DATABASE yhteys:", kursori.fetchone()[0])

icao = input("Anna airport ICAO-koodi: ").upper()
sql = "SELECT name, municipality FROM airport WHERE ident = %s"
kursori.execute(sql, (icao,))
result = kursori.fetchone()

if result:
    print(f"Lentokenettän nimi: {result[0]}")
    print(f"Municipality: {result[1]}")

else:
    print("Lentokenttää ei löydy")

kursori.close()
yhteys.close()




