from geopy import distance
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3307,
    database='flight_game',
    user='root',
    password='Unzila001',
    autocommit=True
)

def GetCoordinate(icao):
    sql = f"SELECT latitude_deg, longitude_deg, name FROM airport WHERE name = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    val = kursori.fetchall()
    if val == []:
        print(f"Lentokenttää {icao} ei löydetty")
        exit(1)
    elif val[0][2] != "":
        print(val[0][2])
    return(val[0][0], val[0][1])

def GetDistance(a1: tuple, a2: tuple):
    return distance.distance(a1, a2).km

def main():
    airports = []
    while len(airports) < 2:
        airports.append(GetCoordinate(input("Syötä ICAO-koodi: ")))
    print(f"Lentokenttien välinen matka on {GetDistance(airports[0], airports[1])}")
main()