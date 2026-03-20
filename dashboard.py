import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# =========================
# LOAD DATA
# =========================
day_df = pd.read_csv("day_clean.csv")
hour_df = pd.read_csv("hour_clean.csv")

# convert datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("Filter Data")

min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(min_date, max_date)
)

# HANDLE ERROR
if len(date_range) != 2:
    st.warning("Silakan pilih rentang tanggal dengan benar")
    st.stop()

start_date, end_date = date_range

# 🔥 FIX PENTING (INI YANG BIKIN ERROR KEMARIN)
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# =========================
# FILTER DATA
# =========================
day_filtered = day_df[
    (day_df["dteday"] >= start_date) &
    (day_df["dteday"] <= end_date)
]

hour_filtered = hour_df[
    (hour_df["dteday"] >= start_date) &
    (hour_df["dteday"] <= end_date)
]

# =========================
# HEADER
# =========================
st.title("🚲 Bike Sharing Dashboard")

# =========================
# KPI
# =========================
total_rentals = day_filtered["cnt"].sum()
st.metric("Total Penyewaan", total_rentals)

# =========================
# PENYEWAAN PER HARI
# =========================
st.subheader("📊 Penyewaan Berdasarkan Hari")

weekday_avg = day_filtered.groupby("weekday")["cnt"].mean()

fig, ax = plt.subplots()
ax.plot(weekday_avg.index, weekday_avg.values, marker='o')
ax.set_xlabel("Hari (0=Min, 6=Sab)")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xticks(range(7))

st.pyplot(fig)

# =========================
# PENYEWAAN PER JAM
# =========================
st.subheader("⏰ Penyewaan Berdasarkan Jam")

hour_avg = hour_filtered.groupby("hr")["cnt"].mean()

fig, ax = plt.subplots()
ax.plot(hour_avg.index, hour_avg.values, marker='o')
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xticks(range(24))

st.pyplot(fig)

# =========================
# FOOTER
# =========================
st.caption("Bike Sharing Dashboard 🚀")