# %% Import thư viện và đọc dữ liệu
import pandas as pd

df = pd.read_csv("data/airline.csv")
print("Trước xử lý:", df.shape)

# %% Bỏ hai cột không dùng trong phân tích
# Unnamed: 0 là cột chỉ mục dư khi xuất CSV.
# id là mã định danh, không dùng để phân tích mức độ hài lòng.
df = df.drop(columns=["Unnamed: 0", "id"])

# %% Tạo biến nhị phân cho satisfaction
df["satisfaction_binary"] = df["satisfaction"].map({
    "neutral or dissatisfied": 0,
    "satisfied": 1
})

# %% Kiểm tra lại dữ liệu
print("Sau xử lý:", df.shape)
print("Missing còn lại:")
print(df.isna().sum()[df.isna().sum() > 0])

# Arrival Delay còn missing. Không điền bằng 0 vì thiếu dữ liệu
# không đồng nghĩa với chuyến bay không bị trễ.

# %% Lưu dữ liệu sạch
df.to_csv("data/airline_clean.csv", index=False)
print("Đã lưu data/airline_clean.csv")
