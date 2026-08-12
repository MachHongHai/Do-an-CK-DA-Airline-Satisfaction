# %% Import thư viện và đọc dữ liệu sạch
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/airline_clean.csv")

# %% Số lượng và tỷ lệ satisfaction
sat_count = df["satisfaction"].value_counts()
sat_rate = df["satisfaction"].value_counts(normalize=True) * 100

print("Số lượng:")
print(sat_count)
print("\nTỷ lệ (%):")
print(sat_rate.round(2))

# %% Biểu đồ tỷ lệ satisfaction
plt.figure(figsize=(6.5, 4.5))
bars = sat_rate.plot(kind="bar", color=["#e74c3c", "#2ecc71"], edgecolor="black", alpha=0.85)
plt.title("Tỷ lệ hài lòng của hành khách", fontsize=12, fontweight="bold")
plt.xlabel("Mức độ hài lòng")
plt.ylabel("Tỷ lệ (%)")
plt.xticks([0, 1], ["Trung lập / Không hài lòng", "Hài lòng"], rotation=0)
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Thêm con số phần trăm lên đầu từng cột
for i, v in enumerate(sat_rate):
    plt.text(i, v + 2, f"{v:.2f}%", ha="center", va="bottom", fontsize=10, fontweight="bold")

plt.tight_layout()
plt.show()

# %% Thống kê các biến số chính
num_cols = [
    "Age",
    "Flight Distance",
    "Departure Delay in Minutes",
    "Arrival Delay in Minutes"
]
print(df[num_cols].describe().T.round(2))

# %% Cơ cấu các biến phân loại
for col in ["Gender", "Customer Type", "Type of Travel", "Class"]:
    print("\n", col)
    print(df[col].value_counts())
