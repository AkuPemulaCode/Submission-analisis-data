import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv("day_clean.csv")
hour_df = pd.read_csv("hour_clean.csv")

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

urutan_hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_df["weekday_name"] = pd.Categorical(
    day_df["weekday"].map({
        0: "Sunday", 1: "Monday", 2: "Tuesday",
        3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"
    }),
    categories=urutan_hari,
    ordered=True
)

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

day_plot_data = day_filtered.groupby("weekday_name", observed=False)["cnt"].sum().reset_index()

max_cnt = day_plot_data["cnt"].max()
colors = ["#1f77b4" if val == max_cnt else "#d3d3d3" for val in day_plot_data["cnt"]]

fig_day, ax_day = plt.subplots(figsize=(10, 6))

sns.barplot(
    x="weekday_name", 
    y="cnt", 
    data=day_plot_data, 
    palette=colors,
    hue="weekday_name", 
    legend=False,
    ax=ax_day
)

ax_day.set_title(f"Total Penyewaan Sepeda per Hari\n(Periode: {start_date.strftime('%Y-%m-%d')} s/d {end_date.strftime('%Y-%m-%d')})", fontsize=16, fontweight='bold', pad=20)
ax_day.set_xlabel(None) 
ax_day.set_ylabel("Total Penyewaan", fontsize=12)

for p in ax_day.patches:
    ax_day.annotate(f"{int(p.get_height()):,}", 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 8), 
                textcoords='offset points',
                fontsize=11, fontweight='bold', color='#333333')

sns.despine()
ax_day.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()

st.pyplot(fig_day)

st.subheader("⏰ Penyewaan Berdasarkan Jam")

hour_plot_data = hour_filtered.groupby("hr")["cnt"].sum().reset_index()

fig_hour, ax_hour = plt.subplots(figsize=(12, 6))

sns.lineplot(
    x="hr", 
    y="cnt", 
    data=hour_plot_data, 
    color="#ff7f0e",
    linewidth=3, 
    marker="o",
    markersize=8,
    markerfacecolor="white",
    markeredgewidth=2,
    ax=ax_hour
)

ax_hour.axvspan(7, 9, color='gray', alpha=0.15, label='Jam Sibuk Pagi')
ax_hour.axvspan(16, 19, color='gray', alpha=0.15, label='Jam Sibuk Sore')

top_3_hours = hour_plot_data.nlargest(3, 'cnt')
for index, row in top_3_hours.iterrows():
    ax_hour.text(
        row['hr'], 
        row['cnt'] + (hour_plot_data['cnt'].max() * 0.03), 
        f"{int(row['cnt']):,}", 
        ha='center', 
        fontsize=11, 
        fontweight='bold',
        color='#333333'
    )

ax_hour.set_title(f"Tren Total Penyewaan Sepeda per Jam\n(Periode: {start_date.strftime('%Y-%m-%d')} s/d {end_date.strftime('%Y-%m-%d')})", fontsize=16, fontweight='bold', pad=20)
ax_hour.set_xlabel("Jam (0 - 23)", fontsize=12)
ax_hour.set_ylabel("Total Penyewaan", fontsize=12)
ax_hour.set_xticks(range(0, 24))

sns.despine()
ax_hour.grid(axis='y', linestyle='--', alpha=0.3)
ax_hour.grid(axis='x', visible=False) 
ax_hour.legend(loc='upper left')
plt.tight_layout()

st.pyplot(fig_hour)

st.caption("Bike Sharing Dashboard 🚀")