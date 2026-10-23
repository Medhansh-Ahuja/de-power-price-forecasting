# Forecasting German Day-Ahead Electricity Prices

> Work in progress. This README grows with the project.

## Goal

Forecast tomorrow's 24 hourly day-ahead electricity prices (€/MWh) for the German–Luxembourg bidding zone (DE-LU), with prediction intervals, using only information available at noon on the day before, exactly as a market participant would.

## Data

| Source | What | Access |
|---|---|---|
| ENTSO-E Transparency Platform | Day-ahead prices; day-ahead forecasts of load, wind and solar | Free API token |
| Open-Meteo | Hourly weather (temperature, wind at 100 m, solar radiation) | Free API |
| `holidays` package | German public holidays | Python package |

History: hourly data from 2019 onward, stored in UTC.

## Planned approach

1. Naive baselines (same hour yesterday / last week) and linear regression
2. LightGBM as the main model, quantile LightGBM for P10–P90 intervals
3. LSTM or N-HiTS as a deep learning challenger
4. Rolling-origin backtest; final test on the most recent full year
5. Daily automated pipeline, FastAPI endpoint and Streamlit dashboard

## Status

- [x] Phase 1: project setup
- [ ] Phase 2: data pipeline
- [ ] Phase 3: exploratory analysis
- [ ] Phase 4: baselines and backtest framework
- [ ] Phase 5: main model
- [ ] Phase 6: uncertainty and deep learning
- [ ] Phase 7: final evaluation
- [ ] Phase 8: production pipeline
- [ ] Phase 9: dashboard

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows (Git Bash): source .venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env             # then add your ENTSO-E token to .env
```
