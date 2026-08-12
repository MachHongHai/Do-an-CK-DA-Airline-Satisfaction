# %% Import thư viện và đọc dữ liệu
import math
import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu

df = pd.read_csv("data/airline_clean.csv")

# %% Hàm tính Cramer's V
def cramers_v(table):
    chi2 = chi2_contingency(table, correction=False)[0]
    n = table.to_numpy().sum()
    rows, cols = table.shape
    return math.sqrt(chi2 / (n * min(rows - 1, cols - 1)))


def hien_thi_p(p):
    if p < 0.001:
        return "< 0.001"
    return round(p, 4)

# %% Kiểm định 1: Class và satisfaction
class_table = pd.crosstab(df["Class"], df["satisfaction"])
chi2, p, dof, expected = chi2_contingency(class_table, correction=False)

print("KIỂM ĐỊNH 1: CLASS VÀ SATISFACTION")
print(class_table)
print("Chi-square =", round(chi2, 3))
print("df =", dof)
print("p-value =", hien_thi_p(p))
print("Cramer's V =", round(cramers_v(class_table), 3))
print("Expected frequency nhỏ nhất =", round(expected.min(), 2))

# %% Kiểm định 2: Type of Travel và satisfaction
travel_table = pd.crosstab(df["Type of Travel"], df["satisfaction"])
chi2, p, dof, expected = chi2_contingency(travel_table, correction=False)

print("\nKIỂM ĐỊNH 2: TYPE OF TRAVEL VÀ SATISFACTION")
print(travel_table)
print("Chi-square =", round(chi2, 3))
print("df =", dof)
print("p-value =", hien_thi_p(p))
print("Cramer's V =", round(cramers_v(travel_table), 3))
print("Expected frequency nhỏ nhất =", round(expected.min(), 2))

# %% Kiểm định 3: Customer Type và satisfaction
customer_table = pd.crosstab(df["Customer Type"], df["satisfaction"])
chi2, p, dof, expected = chi2_contingency(customer_table, correction=False)

print("\nKIỂM ĐỊNH 3: CUSTOMER TYPE VÀ SATISFACTION")
print(customer_table)
print("Chi-square =", round(chi2, 3))
print("df =", dof)
print("p-value =", hien_thi_p(p))
print("Cramer's V =", round(cramers_v(customer_table), 3))
print("Expected frequency nhỏ nhất =", round(expected.min(), 2))

# %% Kiểm định 4: Arrival Delay giữa hai nhóm satisfaction
arrival = df.dropna(subset=["Arrival Delay in Minutes"])

sat_delay = arrival[arrival["satisfaction"] == "satisfied"]["Arrival Delay in Minutes"]
not_sat_delay = arrival[arrival["satisfaction"] == "neutral or dissatisfied"]["Arrival Delay in Minutes"]

u, p = mannwhitneyu(sat_delay, not_sat_delay, alternative="two-sided")

n1 = len(sat_delay)
n2 = len(not_sat_delay)
rank_biserial = (2 * u) / (n1 * n2) - 1

print("\nKIỂM ĐỊNH 4: ARRIVAL DELAY")
print("Số quan sát satisfied =", n1)
print("Số quan sát neutral/dissatisfied =", n2)
print("Median satisfied =", sat_delay.median())
print("Median neutral/dissatisfied =", not_sat_delay.median())
print("Mean satisfied =", round(sat_delay.mean(), 2))
print("Mean neutral/dissatisfied =", round(not_sat_delay.mean(), 2))
print("Mann-Whitney U =", round(u, 1))
print("p-value =", hien_thi_p(p))
print("Rank-biserial correlation =", round(rank_biserial, 3))
