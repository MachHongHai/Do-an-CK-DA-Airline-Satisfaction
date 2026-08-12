import pandas as pd

train = pd.read_csv("data/raw/train.csv")
test = pd.read_csv("data/raw/test.csv")

#Kích thước dữ liệu train và test
print("Kích thước file train:", train.shape)
print("Kích thước file test:", test.shape)

#Xem danh sách cột trong file train và test
print("Cột trong file train:", train.columns.tolist())
print("Cột trong file test:", test.columns.tolist())

#Kiểm tra xem hai file có cùng cột hay không
print("Hai file có cùng cột:",
      train.columns.tolist() == test.columns.tolist())

#Gộp dữ liệu train và test
df = pd.concat([train, test], ignore_index=True)

#Kích thước dữ liệu sau khi gộp
print("Dữ liệu sau khi gộp:", df.shape)

#Lưu dữ liệu gộp vào file airline.csv
df.to_csv("data/airline.csv", index=False)

print("Đã lưu file data/airline.csv")