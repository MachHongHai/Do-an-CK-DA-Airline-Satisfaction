import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")

df = pd.read_csv("data/airline.csv")

# %% Kiểm tra missing value
missing = pd.DataFrame({
    "so_luong_thieu": df.isna().sum(),
    "ty_le_thieu": df.isna().mean() * 100
})
missing = missing[missing["so_luong_thieu"] > 0]
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
    "max": df[service_cols].max()
})
print(service_range)

# %% Boxplot Age
plt.figure(figsize=(5.5, 4))
plt.boxplot(df["Age"].dropna(), patch_artist=True, boxprops=dict(facecolor="#7293CB", alpha=0.7))
plt.title("Phân bố độ tuổi hành khách (Age)", fontweight="bold")
plt.ylabel("Độ tuổi (năm)")
plt.tight_layout()
plt.show()

# %% Boxplot Flight Distance
plt.figure(figsize=(5.5, 4))
plt.boxplot(df["Flight Distance"].dropna(), patch_artist=True, boxprops=dict(facecolor="#7293CB", alpha=0.7))
plt.title("Phân bố khoảng cách chuyến bay (Flight Distance)", fontweight="bold")
plt.ylabel("Khoảng cách bay")
plt.tight_layout()
plt.show()

# %% Boxplot Departure Delay
plt.figure(figsize=(5.5, 4))
plt.boxplot(df["Departure Delay in Minutes"].dropna(), patch_artist=True, boxprops=dict(facecolor="#E1974C", alpha=0.7))
plt.title("Phân bố thời gian trễ khởi hành (Departure Delay)", fontweight="bold")
plt.ylabel("Thời gian trễ (phút)")
plt.tight_layout()
plt.show()

# %% Boxplot Arrival Delay
plt.figure(figsize=(5.5, 4))
plt.boxplot(df["Arrival Delay in Minutes"].dropna(), patch_artist=True, boxprops=dict(facecolor="#E1974C", alpha=0.7))
plt.title("Phân bố thời gian trễ khi đến (Arrival Delay)", fontweight="bold")
plt.ylabel("Thời gian trễ (phút)")
plt.tight_layout()
plt.show()
