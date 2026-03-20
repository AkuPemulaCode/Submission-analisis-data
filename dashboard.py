import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

day_df = pd.read_csv("day_clean.csv")
hour_df = pd.read_csv("hour_clean.csv")


day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

st.sidebar.header("Filter Data")

min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(min_date, max_date)
)


if len(date_range) != 2:
    st.warning("Silakan pilih rentang tanggal dengan benar")
    st.stop()

start_date, end_date = date_range


start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)


day_filtered = day_df[
    (day_df["dteday"] >= start_date) &
    (day_df["dteday"] <= end_date)
]

hour_filtered = hour_df[
    (hour_df["dteday"] >= start_date) &
    (hour_df["dteday"] <= end_date)
]


st.title("🚲 Bike Sharing Dashboard")


total_rentals = day_filtered["cnt"].sum()
st.metric("Total Penyewaan", total_rentals)


st.subheader("📊 Penyewaan Berdasarkan Hari")

weekday_avg = day_filtered.groupby("weekday")["cnt"].mean()

fig, ax = plt.subplots()
ax.plot(weekday_avg.index, weekday_avg.values, marker='o')
ax.set_xlabel("Hari (0=Min, 6=Sab)")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xticks(range(7))

st.pyplot(fig)


st.subheader("⏰ Penyewaan Berdasarkan Jam")

hour_avg = hour_filtered.groupby("hr")["cnt"].mean()

fig, ax = plt.subplots()
ax.plot(hour_avg.index, hour_avg.values, marker='o')
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xticks(range(24))

st.pyplot(fig)


st.caption("Bike Sharing Dashboard 🚀")