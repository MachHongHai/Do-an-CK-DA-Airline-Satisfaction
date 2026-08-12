# %% Import thư viện và đọc dữ liệu
import pandas as pd
import matplotlib.pyplot as plt

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

plt.figure(figsize=(6.5, 4.5))
bp1 = plt.boxplot([not_sat_departure, sat_departure], showfliers=False, patch_artist=True)
colors = ["#e74c3c", "#2ecc71"]
for patch, color in zip(bp1['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
plt.xticks([1, 2], ["Trung lập / Không hài lòng", "Hài lòng"])
plt.title("Departure Delay theo mức độ hài lòng", fontweight="bold")
plt.ylabel("Thời gian trễ xuất phát (Phút)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# %% Boxplot Arrival Delay
arrival = df.dropna(subset=["Arrival Delay in Minutes"])
sat_arrival = arrival[arrival["satisfaction"] == "satisfied"]["Arrival Delay in Minutes"]
not_sat_arrival = arrival[arrival["satisfaction"] == "neutral or dissatisfied"]["Arrival Delay in Minutes"]

plt.figure(figsize=(6.5, 4.5))
bp2 = plt.boxplot([not_sat_arrival, sat_arrival], showfliers=False, patch_artist=True)
for patch, color in zip(bp2['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
plt.xticks([1, 2], ["Trung lập / Không hài lòng", "Hài lòng"])
plt.title("Arrival Delay theo mức độ hài lòng", fontweight="bold")
plt.ylabel("Thời gian trễ hạ cánh (Phút)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# %% Histogram Arrival Delay (giới hạn 120 phút để dễ quan sát)
plot_data = arrival[arrival["Arrival Delay in Minutes"] <= 120]

plt.figure(figsize=(7, 4.5))
plt.hist(
    plot_data[plot_data["satisfaction"] == "neutral or dissatisfied"]["Arrival Delay in Minutes"],
    bins=30,
    alpha=0.6,
    color="#e74c3c",
    edgecolor="black",
    label="Trung lập / Không hài lòng",
    density=True
)
plt.hist(
    plot_data[plot_data["satisfaction"] == "satisfied"]["Arrival Delay in Minutes"],
    bins=30,
    alpha=0.6,
    color="#2ecc71",
    edgecolor="black",
    label="Hài lòng",
    density=True
)
plt.title("Phân phối Arrival Delay theo mức độ hài lòng (<= 120 phút)", fontweight="bold")
plt.xlabel("Thời gian trễ hạ cánh (Phút)")
plt.ylabel("Mật độ tần suất (Density)")
plt.grid(axis="both", linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()
