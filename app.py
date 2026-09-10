import streamlit as st
import pandas as pd
import numpy as np

st.title("🚕 Hyderabad Auto Fare Analyzer")
df = pd.read_csv('hyderabad_auto_fares.csv')

pickup = st.selectbox("Pickup", df['pickup'].unique())
drop = st.selectbox("Drop", df['drop'].unique())
hour = st.slider("Hour of day", 0, 23, 9)

distance = round(np.random.uniform(2,15), 2)
is_peak = hour in [8,9,18,19,20]
base = 26 + max(0, distance-1.6)*13.75
surge = 1.5 if is_peak else 1.0
fare = round(base * surge, 2)

st.metric("Estimated Fare", f"₹{fare}")
st.metric("Peak Hour?", "Yes 🔴" if is_peak else "No 🟢")
st.line_chart(df.groupby('hour')['final_fare'].mean())