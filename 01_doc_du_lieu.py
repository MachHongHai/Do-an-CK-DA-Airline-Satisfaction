import pandas as pd

#Đọc dữ liệu
df = pd.read_csv("data/airline.csv")

print("Kích thước dữ liệu:", df.shape)

#Xem 5 dòng đầu
print(df.head())

#Xem danh sách cột
print("Danh sách cột:")
for col in df.columns:
    print("-", col)

#Xem thông tin dữ liệu
print("Thông tin dữ liệu:")
print(df.info())
