import requests
import pandas as pd

LOCATIONS = {
    "husum": (54.48, 9.05),
    "rostock": (54.09, 12.10),
    "berlin": (52.52, 13.41),
    "essen": (51.46, 7.01),
    "frankfurt": (50.11, 8.68),
    "munich": (48.14, 11.58),
}

URL = "https://archive-api.open-meteo.com/v1/archive"


def fetch_weather(name, lat, lon, start_date, end_date):
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "temperature_2m,wind_speed_100m,shortwave_radiation",
        "wind_speed_unit": "ms",
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()
    df = pd.DataFrame(response.json()["hourly"])
    df["location"] = name
    return df


frames = []
for name, (lat, lon) in LOCATIONS.items():
    print(f"Downloading {name}...")
    frames.append(fetch_weather(name, lat, lon, "2024-01-01", "2024-01-07"))

df = pd.concat(frames, ignore_index=True)
print(df.head())
print(df.shape)
print(df["location"].value_counts())