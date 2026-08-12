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

service_mean.plot(kind="barh", figsize=(9, 7))
plt.title("Điểm trung bình của các tiêu chí dịch vụ")
plt.xlabel("Điểm trung bình")
plt.xlim(0, 5)
plt.tight_layout()
plt.show()

# %% So sánh hai nhóm satisfaction
service_by_sat = df.groupby("satisfaction")[service_cols].mean().T
service_by_sat["chenh_lech"] = (
    service_by_sat["satisfied"]
    - service_by_sat["neutral or dissatisfied"]
)

print(service_by_sat.sort_values("chenh_lech", ascending=False).round(2))

# %% Biểu đồ chênh lệch điểm dịch vụ
service_by_sat["chenh_lech"].sort_values().plot(kind="barh", figsize=(9, 7))
plt.title("Chênh lệch điểm dịch vụ giữa hai nhóm")
plt.xlabel("satisfied - neutral/dissatisfied")
plt.tight_layout()
plt.show()
