# %% Import thư viện và đọc dữ liệu
import pandas as pd
import matplotlib.pyplot as plt

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

gender["ty_le"].plot(kind="bar")
plt.title("Tỷ lệ hài lòng theo giới tính")
plt.ylabel("Tỷ lệ (%)")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# %% Theo loại khách hàng
customer = tinh_ty_le("Customer Type")
print(customer.round(2))

customer["ty_le"].plot(kind="bar")
plt.title("Tỷ lệ hài lòng theo loại khách hàng")
plt.ylabel("Tỷ lệ (%)")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# %% Theo mục đích chuyến đi
travel = tinh_ty_le("Type of Travel")
print(travel.round(2))

travel["ty_le"].plot(kind="bar")
plt.title("Tỷ lệ hài lòng theo mục đích chuyến đi")
plt.ylabel("Tỷ lệ (%)")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# %% Theo hạng vé
class_summary = tinh_ty_le("Class")
class_summary = class_summary.reindex(["Business", "Eco Plus", "Eco"])
print(class_summary.round(2))

class_summary["ty_le"].plot(kind="bar")
plt.title("Tỷ lệ hài lòng theo hạng vé")
plt.ylabel("Tỷ lệ (%)")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
