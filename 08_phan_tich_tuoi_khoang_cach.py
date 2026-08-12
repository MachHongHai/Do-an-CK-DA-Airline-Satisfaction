# %% Import thư viện và đọc dữ liệu
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")

df = pd.read_csv("data/airline_clean.csv")

# %% Thống kê tuổi theo satisfaction
age_summary = df.groupby("satisfaction")["Age"].agg(["count", "mean", "median", "std"])
print(age_summary.round(2))

sat_age = df[df["satisfaction"] == "satisfied"]["Age"]
not_sat_age = df[df["satisfaction"] == "neutral or dissatisfied"]["Age"]

plt.figure(figsize=(6, 4))
plt.boxplot([not_sat_age, sat_age], tick_labels=["Không hài lòng / Trung lập", "Hài lòng"], patch_artist=True, boxprops=dict(facecolor="#7293CB", alpha=0.7))
plt.title("Phân bố Tuổi theo mức độ hài lòng", fontweight="bold")
plt.ylabel("Tuổi")
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

plt.figure(figsize=(6, 4))
ax1 = age_rate.plot(kind="bar", color="steelblue", width=0.5)
ax1.bar_label(ax1.containers[0], fmt="%.2f%%", padding=3, fontweight="bold")
plt.title("Tỷ lệ hài lòng theo nhóm tuổi", fontweight="bold")
plt.ylabel("Tỷ lệ hài lòng (%)")
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

plt.figure(figsize=(6, 4))
plt.boxplot([not_sat_distance, sat_distance], tick_labels=["Không hài lòng / Trung lập", "Hài lòng"], showfliers=False, patch_artist=True, boxprops=dict(facecolor="#7293CB", alpha=0.7))
plt.title("Flight Distance theo mức độ hài lòng", fontweight="bold")
plt.ylabel("Khoảng cách bay (Flight Distance)")
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

plt.figure(figsize=(6, 4))
ax2 = distance_rate.plot(kind="bar", color="steelblue", width=0.5)
ax2.bar_label(ax2.containers[0], fmt="%.2f%%", padding=3, fontweight="bold")
plt.title("Tỷ lệ hài lòng theo nhóm khoảng cách bay", fontweight="bold")
plt.ylabel("Tỷ lệ hài lòng (%)")
plt.xlabel("Nhóm khoảng cách bay (Dặm)")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
