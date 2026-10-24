import holidays
import pandas as pd
import duckdb

YEARS = range(2019, 2027)
STATES = ["BB", "BE", "BW", "BY", "HB", "HE", "HH", "MV",
          "NI", "NW", "RP", "SH", "SL", "SN", "ST", "TH"]

DB_PATH = "data/power.duckdb"

rows = []
for state in STATES:
    state_holidays = holidays.Germany(subdiv=state, years=YEARS)
    for date, name in state_holidays.items():
        rows.append({"date": date, "state": state, "name": name})

df = pd.DataFrame(rows)

daily = df.groupby("date").agg(
    n_states=("state", "nunique"),
    name=("name", "first"),
).reset_index()

con = duckdb.connect(DB_PATH)
con.execute("CREATE OR REPLACE TABLE holidays AS SELECT * FROM daily")
con.sql("SELECT n_states, COUNT(*) AS days FROM holidays GROUP BY n_states ORDER BY n_states DESC").show()
con.close()