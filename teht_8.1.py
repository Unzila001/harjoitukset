import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3307,
    database='flight_game',
    user='root',
    password='Unzila001',
    autocommit=True
)

def get_airport_data(icao):
    sql = f"SELECT name, iso:region FROM airport WHERE ident ='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    val = kursori.fetchall()
    if kursori.rowcount > 0:
        for n in val:
            print(f"{icao} lentokentän nimi on {n[0]} ja se sijaistee n[1]" )
    return val





