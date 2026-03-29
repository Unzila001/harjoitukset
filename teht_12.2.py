import requests

kaupunki = input("Anna kaupunki nimi: ")
API_key = "API_KEY"

url = f"https://api.openweathermap.org/data/3.0/weather?q={kaupunki}&appid={API_key}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} C")
else:
    print("Error:", data["message"])