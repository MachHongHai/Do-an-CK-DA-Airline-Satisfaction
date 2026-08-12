# %% Import thư viện và đọc dữ liệu sạch
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")

df = pd.read_csv("data/airline_clean.csv")

# %% Số lượng và tỷ lệ satisfaction
sat_count = df["satisfaction"].value_counts()
sat_rate = df["satisfaction"].value_counts(normalize=True) * 100

print("Số lượng:")
print(sat_count)
print("\nTỷ lệ (%):")
print(sat_rate.round(2))

# %% Biểu đồ tỷ lệ satisfaction
plt.figure(figsize=(6, 4))
ax = sat_rate.plot(kind="bar", color=["#e74c3c", "#2ecc71"], width=0.45)
ax.bar_label(ax.containers[0], fmt="%.2f%%", padding=3, fontweight="bold")
plt.title("Tỷ lệ hài lòng chung của hành khách", fontsize=12, fontweight="bold")
plt.xlabel("Trạng thái hài lòng")
plt.ylabel("Tỷ lệ phần trăm (%)")
plt.xticks([0, 1], ["Không hài lòng / Trung lập", "Hài lòng"], rotation=0)
plt.ylim(0, 100)
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
