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

plt.boxplot([not_sat_departure, sat_departure], showfliers=False)
plt.xticks([1, 2], ["neutral/dissatisfied", "satisfied"])
plt.title("Departure Delay theo mức độ hài lòng")
plt.ylabel("Phút")
plt.show()

# %% Boxplot Arrival Delay
arrival = df.dropna(subset=["Arrival Delay in Minutes"])
sat_arrival = arrival[arrival["satisfaction"] == "satisfied"]["Arrival Delay in Minutes"]
not_sat_arrival = arrival[arrival["satisfaction"] == "neutral or dissatisfied"]["Arrival Delay in Minutes"]

plt.boxplot([not_sat_arrival, sat_arrival], showfliers=False)
plt.xticks([1, 2], ["neutral/dissatisfied", "satisfied"])
plt.title("Arrival Delay theo mức độ hài lòng")
plt.ylabel("Phút")
plt.show()

# %% Histogram Arrival Delay (giới hạn 120 phút để dễ quan sát)
plot_data = arrival[arrival["Arrival Delay in Minutes"] <= 120]

plt.hist(
    plot_data[plot_data["satisfaction"] == "neutral or dissatisfied"]["Arrival Delay in Minutes"],
    bins=30,
    alpha=0.6,
    label="neutral/dissatisfied",
    density=True
)
plt.hist(
    plot_data[plot_data["satisfaction"] == "satisfied"]["Arrival Delay in Minutes"],
    bins=30,
    alpha=0.6,
    label="satisfied",
    density=True
)
plt.title("Phân phối Arrival Delay")
plt.xlabel("Phút")
plt.ylabel("Mật độ")
plt.legend()
plt.show()
