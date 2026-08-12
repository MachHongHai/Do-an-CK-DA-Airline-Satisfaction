# %% Import thư viện và đọc dữ liệu
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")

df = pd.read_csv("data/airline_clean.csv")

# %% Danh sách các tiêu chí dịch vụ
service_cols = [
    "Inflight wifi service",
    "Departure/Arrival time convenient",
    "Ease of Online booking",
    "Gate location",
    "Food and drink",
    "Online boarding",
    "Seat comfort",
    "Inflight entertainment",
    "On-board service",
    "Leg room service",
    "Baggage handling",
    "Checkin service",
    "Inflight service",
    "Cleanliness"
]

# %% Điểm dịch vụ trung bình
service_mean = df[service_cols].mean().sort_values()
print(service_mean.round(2))

plt.figure(figsize=(8, 5))
ax1 = service_mean.plot(kind="barh", color="steelblue")
ax1.bar_label(ax1.containers[0], fmt="%.2f", padding=3, fontweight="bold")
plt.title("Điểm trung bình các tiêu chí dịch vụ", fontsize=12, fontweight="bold")
plt.xlabel("Điểm trung bình (Thang điểm 0 - 5)")
plt.xlim(0, 5.5)
plt.tight_layout()
plt.show()

# %% So sánh hai nhóm satisfaction
service_by_sat = df.groupby("satisfaction")[service_cols].mean().T
service_by_sat["chenh_lech"] = (
    service_by_sat["satisfied"]
    - service_by_sat["neutral or dissatisfied"]
)

sorted_diff = service_by_sat["chenh_lech"].sort_values()
print(service_by_sat.sort_values("chenh_lech", ascending=False).round(2))

# %% Biểu đồ chênh lệch điểm dịch vụ
plt.figure(figsize=(8, 5))
ax2 = sorted_diff.plot(kind="barh", color="mediumseagreen")
ax2.bar_label(ax2.containers[0], fmt="+%.2f", padding=3, fontweight="bold")
plt.title("Chênh lệch điểm dịch vụ giữa nhóm Hài lòng vs Không hài lòng", fontsize=12, fontweight="bold")
plt.xlabel("Chênh lệch điểm trung bình (satisfied - neutral/dissatisfied)")
plt.xlim(0, max(sorted_diff) + 0.3)
plt.tight_layout()
plt.show()
