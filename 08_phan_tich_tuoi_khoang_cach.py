# %% Import thư viện và đọc dữ liệu
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/airline_clean.csv")

# %% Thống kê tuổi theo satisfaction
age_summary = df.groupby("satisfaction")["Age"].agg(["count", "mean", "median", "std"])
print(age_summary.round(2))

sat_age = df[df["satisfaction"] == "satisfied"]["Age"]
not_sat_age = df[df["satisfaction"] == "neutral or dissatisfied"]["Age"]

plt.figure(figsize=(6.5, 4.5))
bp_age = plt.boxplot([not_sat_age, sat_age], patch_artist=True)
colors = ["#e74c3c", "#2ecc71"]
for patch, color in zip(bp_age['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
plt.xticks([1, 2], ["Trung lập / Không hài lòng", "Hài lòng"])
plt.title("Phân bố Tuổi theo mức độ hài lòng", fontweight="bold")
plt.ylabel("Tuổi")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
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

plt.figure(figsize=(6.5, 4.5))
age_rate.plot(kind="bar", color="#4C92C3", edgecolor="black", alpha=0.85)
plt.title("Tỷ lệ hài lòng theo nhóm tuổi", fontweight="bold")
plt.ylabel("Tỷ lệ (%)")
plt.xlabel("Nhóm tuổi")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, v in enumerate(age_rate):
    plt.text(i, v + 2, f"{v:.2f}%", ha="center", va="bottom", fontweight="bold")

plt.tight_layout()
plt.show()

# %% Khoảng cách chuyến bay theo satisfaction
distance_summary = df.groupby("satisfaction")["Flight Distance"].agg(["count", "mean", "median", "std"])
print(distance_summary.round(2))

sat_distance = df[df["satisfaction"] == "satisfied"]["Flight Distance"]
not_sat_distance = df[df["satisfaction"] == "neutral or dissatisfied"]["Flight Distance"]

plt.figure(figsize=(6.5, 4.5))
bp_dist = plt.boxplot([not_sat_distance, sat_distance], showfliers=False, patch_artist=True)
for patch, color in zip(bp_dist['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
plt.xticks([1, 2], ["Trung lập / Không hài lòng", "Hài lòng"])
plt.title("Flight Distance theo mức độ hài lòng", fontweight="bold")
plt.ylabel("Khoảng cách bay (Flight Distance)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
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

plt.figure(figsize=(6.5, 4.5))
distance_rate.plot(kind="bar", color="#4C92C3", edgecolor="black", alpha=0.85)
plt.title("Tỷ lệ hài lòng theo nhóm khoảng cách bay", fontweight="bold")
plt.ylabel("Tỷ lệ (%)")
plt.xlabel("Nhóm khoảng cách (Dặm / Flight Distance)")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, v in enumerate(distance_rate):
    plt.text(i, v + 2, f"{v:.2f}%", ha="center", va="bottom", fontweight="bold")

plt.tight_layout()
plt.show()
