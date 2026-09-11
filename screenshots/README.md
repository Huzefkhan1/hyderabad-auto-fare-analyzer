# 🚕 Hyderabad Auto Fare Analyzer

A data analysis and prediction tool that estimates auto-rickshaw fares across Hyderabad localities based on official RTA tariff rules, peak-hour surge patterns, and time-of-day effects.

## 📌 Problem Statement
Real fare data from ride-hailing companies (Ola/Uber) is not publicly available. To still build a realistic, explainable fare analysis project, this dataset was **simulated using Telangana RTA's official auto-rickshaw tariff structure** — not random numbers.

## ⚙️ Approach
- Base fare calculated using actual RTA rules: ₹26 for first 1.6 km, ₹13.75/km after that
- Peak-hour surge (8–10 AM, 6–9 PM) applied with a 1.2x–1.8x multiplier
- Night charge (11 PM–5 AM) adds a flat 50% surcharge
- 2,000 trip records generated across 8 major Hyderabad localities (Gachibowli, Kukatpally, Mehdipatnam, Ameerpet, Kondapur, Secunderabad, Dilsukhnagar, Banjara Hills)

## 🛠️ Tech Stack
- **Python** — Pandas, NumPy (data generation)
- **Matplotlib, Seaborn** — exploratory data analysis
- **Streamlit** — interactive web app for live fare estimation

## 📊 Key Insights
- Fares spike **~40–50%** during peak hours (8–9 AM, 6–8 PM) due to surge multiplier
- Night rides (11 PM–5 AM) consistently cost more despite lower traffic
- [Yahan apna ek aur observation likho jo charts se dikha — jaise konsa route sabse busy tha]

## 🚀 Run Locally
```bash
pip install streamlit pandas numpy
streamlit run app.py
```

## 📷 Screenshots

### Streamlit App
![App Screenshot](screenshots/app.png)

### Peak Hour Surge Analysis
![Peak Surge](screenshots/peak_surge.png)

### Hourly Fare Trend
![Hourly Trend](screenshots/hourly_trend.png)

## 📁 Files
- `app.py` — Streamlit application
- `hyderabad_auto_fares.csv` — generated dataset (2000 trips)

## 🔗 Author
Huzef Khan — [GitHub](https://github.com/Huzefkhan1) | [LinkedIn](https://linkedin.com/in/huzef-khan)