import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m",
}

response = requests.get(url, params=params)
data = response.json()

print(data["hourly"]["time"][0])
print(data["hourly"]["temperature_2m"][0])