import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m",
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data["hourly"])
print(df.head())
print(df.shape)