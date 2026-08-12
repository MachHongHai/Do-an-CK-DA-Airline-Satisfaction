# %% Import thư viện và đọc dữ liệu
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/airline_clean.csv")

# %% Thống kê tuổi theo satisfaction
age_summary = df.groupby("satisfaction")["Age"].agg(["count", "mean", "median", "std"])
print(age_summary.round(2))

sat_age = df[df["satisfaction"] == "satisfied"]["Age"]
not_sat_age = df[df["satisfaction"] == "neutral or dissatisfied"]["Age"]

plt.boxplot([not_sat_age, sat_age])
plt.xticks([1, 2], ["neutral/dissatisfied", "satisfied"])
plt.title("Tuổi theo mức độ hài lòng")
plt.ylabel("Tuổi")
plt.show()

# %% Tỷ lệ hài lòng theo nhóm tuổi
df["age_group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 30, 45, 60, 100],
    labels=["<=18", "19-30", "31-45", "46-60", ">60"],
    include_lowest=True
)

age_rate = df.groupby("age_group", observed=True)["satisfaction_binary"].mean() * 100
print(age_rate.round(2))

age_rate.plot(kind="bar")
plt.title("Tỷ lệ hài lòng theo nhóm tuổi")
plt.ylabel("Tỷ lệ (%)")
plt.xlabel("Nhóm tuổi")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# %% Khoảng cách chuyến bay theo satisfaction
distance_summary = df.groupby("satisfaction")["Flight Distance"].agg(["count", "mean", "median", "std"])
print(distance_summary.round(2))

sat_distance = df[df["satisfaction"] == "satisfied"]["Flight Distance"]
not_sat_distance = df[df["satisfaction"] == "neutral or dissatisfied"]["Flight Distance"]

plt.boxplot([not_sat_distance, sat_distance], showfliers=False)
plt.xticks([1, 2], ["neutral/dissatisfied", "satisfied"])
plt.title("Flight Distance theo mức độ hài lòng")
plt.ylabel("Flight Distance")
plt.show()

# %% Tỷ lệ hài lòng theo nhóm khoảng cách
df["distance_group"] = pd.cut(
    df["Flight Distance"],
    bins=[0, 500, 1000, 2000, 5000],
    labels=["<=500", "501-1000", "1001-2000", ">2000"],
    include_lowest=True
)

distance_rate = df.groupby("distance_group", observed=True)["satisfaction_binary"].mean() * 100
print(distance_rate.round(2))

distance_rate.plot(kind="bar")
plt.title("Tỷ lệ hài lòng theo nhóm khoảng cách")
plt.ylabel("Tỷ lệ (%)")
plt.xlabel("Nhóm Flight Distance")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
