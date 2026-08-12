# %% Import thư viện và đọc dữ liệu
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")

df = pd.read_csv("data/airline_clean.csv")

# %% Thống kê delay theo satisfaction
delay_summary = df.groupby("satisfaction")[[
    "Departure Delay in Minutes",
    "Arrival Delay in Minutes"
]].agg(["count", "mean", "median", "std", "max"])

print(delay_summary.round(2))

# %% Boxplot Departure Delay
sat_departure = df[df["satisfaction"] == "satisfied"]["Departure Delay in Minutes"].dropna()
not_sat_departure = df[df["satisfaction"] == "neutral or dissatisfied"]["Departure Delay in Minutes"].dropna()

plt.figure(figsize=(6, 4))
plt.boxplot([not_sat_departure, sat_departure], tick_labels=["Không hài lòng / Trung lập", "Hài lòng"], showfliers=False, patch_artist=True, boxprops=dict(facecolor="#7293CB", alpha=0.7))
plt.title("Departure Delay theo mức độ hài lòng", fontweight="bold")
plt.ylabel("Thời gian trễ xuất phát (Phút)")
plt.tight_layout()
plt.show()

# %% Boxplot Arrival Delay
arrival = df.dropna(subset=["Arrival Delay in Minutes"])
sat_arrival = arrival[arrival["satisfaction"] == "satisfied"]["Arrival Delay in Minutes"]
not_sat_arrival = arrival[arrival["satisfaction"] == "neutral or dissatisfied"]["Arrival Delay in Minutes"]

plt.figure(figsize=(6, 4))
plt.boxplot([not_sat_arrival, sat_arrival], tick_labels=["Không hài lòng / Trung lập", "Hài lòng"], showfliers=False, patch_artist=True, boxprops=dict(facecolor="#7293CB", alpha=0.7))
plt.title("Arrival Delay theo mức độ hài lòng", fontweight="bold")
plt.ylabel("Thời gian trễ hạ cánh (Phút)")
plt.tight_layout()
plt.show()

# %% Histogram Arrival Delay (giới hạn 120 phút để dễ quan sát)
plot_data = arrival[arrival["Arrival Delay in Minutes"] <= 120]

plt.figure(figsize=(6.5, 4))
plt.hist(
    plot_data[plot_data["satisfaction"] == "neutral or dissatisfied"]["Arrival Delay in Minutes"],
    bins=30,
    alpha=0.6,
    color="indianred",
    label="Không hài lòng / Trung lập",
    density=True
)
plt.hist(
    plot_data[plot_data["satisfaction"] == "satisfied"]["Arrival Delay in Minutes"],
    bins=30,
    alpha=0.6,
    color="mediumseagreen",
    label="Hài lòng",
    density=True
)
plt.title("Phân phối Arrival Delay theo mức độ hài lòng (<= 120 phút)", fontweight="bold")
plt.xlabel("Thời gian trễ hạ cánh (Phút)")
plt.ylabel("Mật độ tần suất (Density)")
plt.legend()
plt.tight_layout()
plt.show()
