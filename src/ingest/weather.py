import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
       "latitude": 52.52,
       "longitude": 13.41,
       "start_date": "2024-01-01",
       "end_date": "2024-01-07",
       "hourly": "temperature_2m,wind_speed_100m,shortwave_radiation",
       "wind_speed_unit": "ms",
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data["hourly"])
print(df.head())
print(df.shape)