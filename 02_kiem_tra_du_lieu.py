import pandas as pd

df = pd.read_csv("data/airline.csv")

# %% Kiểm tra missing value
missing = pd.DataFrame({
    "so_luong_thieu": df.isna().sum(),
    "ty_le_thieu": df.isna().mean() * 100
})
missing = missing[missing["so_luong_thieu"] > 0]
missing["ty_le_thieu"] = missing["ty_le_thieu"].round(2)
print(missing)

# %% Kiểm tra dữ liệu trùng
print("Số dòng trùng hoàn toàn:", df.duplicated().sum())
print("Số id bị trùng:", df["id"].duplicated().sum())

# %% Kiểm tra các biến phân loại
cat_cols = ["Gender", "Customer Type", "Type of Travel", "Class", "satisfaction"]

for col in cat_cols:
    print("\n", col)
    print(df[col].value_counts())

# %% Thống kê một số biến số
num_cols = [
    "Age",
    "Flight Distance",
    "Departure Delay in Minutes",
    "Arrival Delay in Minutes"
]
print(df[num_cols].describe().T)

# %% Kiểm tra miền điểm dịch vụ
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

service_range = pd.DataFrame({
    "min": df[service_cols].min(),
    "max": df[service_cols].max(),
    "so_luong_0": (df[service_cols] == 0).sum()
})
print(service_range)
