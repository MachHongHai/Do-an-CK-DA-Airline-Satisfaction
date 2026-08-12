# %% Import thư viện và đọc dữ liệu
import pandas as pd
import matplotlib.pyplot as plt

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

plt.figure(figsize=(9, 6.5))
service_mean.plot(kind="barh", color="#4C92C3", edgecolor="black", alpha=0.85)
plt.title("Điểm trung bình của các tiêu chí dịch vụ", fontsize=12, fontweight="bold")
plt.xlabel("Điểm trung bình (Thang điểm 0 - 5)")
plt.xlim(0, 5.5)
plt.grid(axis="x", linestyle="--", alpha=0.5)

# Thêm giá trị điểm số ở cuối mỗi thanh ngang
for i, v in enumerate(service_mean):
    plt.text(v + 0.05, i, f"{v:.2f}", va="center", fontsize=9, fontweight="bold")

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
plt.figure(figsize=(9, 6.5))
sorted_diff.plot(kind="barh", color="#2ecc71", edgecolor="black", alpha=0.85)
plt.title("Chênh lệch điểm dịch vụ giữa nhóm Hài lòng vs Không hài lòng", fontsize=12, fontweight="bold")
plt.xlabel("Chênh lệch điểm trung bình (satisfied - neutral/dissatisfied)")
plt.xlim(0, max(sorted_diff) + 0.3)
plt.grid(axis="x", linestyle="--", alpha=0.5)

# Thêm giá trị chênh lệch ở cuối mỗi thanh
for i, v in enumerate(sorted_diff):
    plt.text(v + 0.03, i, f"+{v:.2f}", va="center", fontsize=9, fontweight="bold")

plt.tight_layout()
plt.show()
