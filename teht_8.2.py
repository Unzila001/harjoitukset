import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3307,
    database='flight_game',
    user='root',
    password='Unzila001',
    autocommit=True
)
def lentokenttien_tyypeit():
    maakoodi = input("Anna maakoodin(esimerkiksi FI): ").upper()

    kursori = yhteys.cursor()
    sql = """
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    """

    kursori.execute(sql, (maakoodi,))
    result = kursori.fetchall()

    if result:
        for row in result:
            lentokenttien_tyypeit = row[0]
            määrä = row[1]
            print(f"{lentokenttien_tyypeit}: {määrä}")
    else:
        print("Lentokenttä ei löydyy")
    kursori.close()
lentokenttien_tyypeit()
yhteys.close()