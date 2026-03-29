import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()

vitsi = data["value"]
print(vitsi)

