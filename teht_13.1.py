from flask import Flask, jsonify

app = Flask(__name__)
def alkuluku(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
@app.route('/alkuluku/<int:number>')
def check_alkuluku(number):
    result = alkuluku(number)
    return jsonify({
        "Number": number,
        "isPrime": result
    })

if __name__ == '__main__':
    app.run(port=3000)