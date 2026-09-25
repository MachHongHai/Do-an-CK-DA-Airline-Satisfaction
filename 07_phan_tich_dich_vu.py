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

# Điểm 0 là trường hợp không áp dụng nên không tính vào trung bình
service_data = df[service_cols].mask(df[service_cols] == 0)

# %% Điểm dịch vụ trung bình
service_mean = service_data.mean().sort_values()
print(service_mean.round(2))

service_mean.plot(kind="barh")
plt.title("Điểm trung bình các tiêu chí dịch vụ")
plt.xlabel("Điểm trung bình")
plt.show()

# %% So sánh hai nhóm satisfaction
service_compare = df[["satisfaction"]].join(service_data)

service_by_sat = service_compare.groupby("satisfaction")[service_cols].mean().T
service_by_sat["chenh_lech"] = (
    service_by_sat["satisfied"]
    - service_by_sat["neutral or dissatisfied"]
)

sorted_diff = service_by_sat["chenh_lech"].sort_values()
print(service_by_sat.sort_values("chenh_lech", ascending=False).round(2))

# %% Biểu đồ chênh lệch điểm dịch vụ
sorted_diff.plot(kind="barh")
plt.title("Chênh lệch điểm dịch vụ giữa hai nhóm")
plt.xlabel("Chênh lệch điểm trung bình")
plt.show()
