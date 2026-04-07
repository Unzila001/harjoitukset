from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3307,
        database='flight_game',
        user='root',
        password='Unzila001',
        autocommit=True
    )

@app.route('/kenttä/<icao>')
def get_airport(icao,):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "Select name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        name, municipality = result
        return jsonify({
            "ICAO": icao,
            "Name": name,
            "Municipality": municipality
        })
    else:
        return jsonify({
            "error": "Airport not found"
        })

if __name__ == '__main__':
    app.run(port=3000)