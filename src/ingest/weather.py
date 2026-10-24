import requests
import pandas as pd
import duckdb

LOCATIONS = {
    "husum": (54.48, 9.05),
    "rostock": (54.09, 12.10),
    "berlin": (52.52, 13.41),
    "essen": (51.46, 7.01),
    "frankfurt": (50.11, 8.68),
    "munich": (48.14, 11.58),
}

URL = "https://archive-api.open-meteo.com/v1/archive"
DB_PATH = "data/power.duckdb"


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
    df["time"] = pd.to_datetime(df["time"], utc=True)
    df["location"] = name
    return df


def save_weather(df):
    con = duckdb.connect(DB_PATH)
    con.execute("CREATE OR REPLACE TABLE weather AS SELECT * FROM df")
    con.close()


frames = []
for name, (lat, lon) in LOCATIONS.items():
    print(f"Downloading {name}...")
    frames.append(fetch_weather(name, lat, lon, "2019-01-01", "2026-10-17"))

df = pd.concat(frames, ignore_index=True)
save_weather(df)

con = duckdb.connect(DB_PATH)
con.execute("SET TimeZone = 'UTC'")
con.sql("""
    SELECT location,
           MIN(time) AS first_hour,
           MAX(time) AS last_hour,
           COUNT(*) - COUNT(wind_speed_100m) AS missing_wind,
           ROUND(AVG(wind_speed_100m), 2) AS avg_wind,
           ROUND(AVG(shortwave_radiation), 1) AS avg_sun
    FROM weather
    GROUP BY location
    ORDER BY avg_wind DESC
""").show()
con.close()