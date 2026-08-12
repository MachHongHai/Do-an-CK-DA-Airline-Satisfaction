# %% Import thư viện và đọc dữ liệu
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")

df = pd.read_csv("data/airline_clean.csv")

# %% Hàm tạo bảng tỷ lệ hài lòng theo nhóm
def tinh_ty_le(col):
    bang = df.groupby(col)["satisfaction_binary"].agg(["count", "sum", "mean"])
    bang.columns = ["tong", "hai_long", "ty_le"]
    bang["ty_le"] = bang["ty_le"] * 100
    return bang

# %% Theo giới tính
gender = tinh_ty_le("Gender")
print(gender.round(2))

plt.figure(figsize=(6, 4))
ax = gender["ty_le"].plot(kind="bar", color="steelblue", width=0.45)
ax.bar_label(ax.containers[0], fmt="%.2f%%", padding=3, fontweight="bold")
plt.title("Tỷ lệ hài lòng theo giới tính", fontweight="bold")
plt.ylabel("Tỷ lệ hài lòng (%)")
plt.xlabel("Giới tính")
plt.xticks([0, 1], ["Nữ", "Nam"], rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# %% Theo loại khách hàng
customer = tinh_ty_le("Customer Type")
print(customer.round(2))

plt.figure(figsize=(6, 4))
ax = customer["ty_le"].plot(kind="bar", color="steelblue", width=0.45)
ax.bar_label(ax.containers[0], fmt="%.2f%%", padding=3, fontweight="bold")
plt.title("Tỷ lệ hài lòng theo phân loại khách hàng", fontweight="bold")
plt.ylabel("Tỷ lệ hài lòng (%)")
plt.xlabel("Loại khách hàng")
plt.xticks([0, 1], ["Khách hàng thân thiết", "Khách hàng mới/vãng lai"], rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# %% Theo mục đích chuyến đi
travel = tinh_ty_le("Type of Travel")
print(travel.round(2))

plt.figure(figsize=(6, 4))
ax = travel["ty_le"].plot(kind="bar", color="steelblue", width=0.45)
ax.bar_label(ax.containers[0], fmt="%.2f%%", padding=3, fontweight="bold")
plt.title("Tỷ lệ hài lòng theo mục đích chuyến bay", fontweight="bold")
plt.ylabel("Tỷ lệ hài lòng (%)")
plt.xlabel("Mục đích chuyến bay")
plt.xticks([0, 1], ["Bay công tác", "Bay cá nhân"], rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# %% Theo hạng vé
class_summary = tinh_ty_le("Class")
class_summary = class_summary.reindex(["Business", "Eco Plus", "Eco"])
print(class_summary.round(2))

plt.figure(figsize=(6, 4))
ax = class_summary["ty_le"].plot(kind="bar", color="steelblue", width=0.5)
ax.bar_label(ax.containers[0], fmt="%.2f%%", padding=3, fontweight="bold")
plt.title("Tỷ lệ hài lòng theo hạng ghế", fontweight="bold")
plt.ylabel("Tỷ lệ hài lòng (%)")
plt.xlabel("Hạng ghế (Class)")
plt.xticks([0, 1, 2], ["Thương gia (Business)", "Phổ thông cao cấp (Eco Plus)", "Phổ thông (Eco)"], rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
