

import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load the dataset
df = pd.read_csv("retail_sales_dataset.csv")

# 2. Create a folder for results
os.makedirs("results", exist_ok=True)

print("RETAIL SALES DATA ANALYSIS")
print("=" * 40)

# 3. Explore the dataset
print("\nFirst five rows:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# 4. Prepare the date column
df["Date"] = pd.to_datetime(df["Date"])

# 5. Sales by product category
category_sales = df.groupby("Product Category")["Total Amount"].sum()
category_sales = category_sales.sort_values(ascending=False)

plt.figure(figsize=(9, 5))
category_sales.plot(kind="bar")
plt.title("Total Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("results/revenue_by_category.png")
plt.close()

# 6. Sales by gender
gender_sales = df.groupby("Gender")["Total Amount"].sum()

plt.figure(figsize=(7, 5))
gender_sales.plot(kind="bar")
plt.title("Total Revenue by Gender")
plt.xlabel("Gender")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("results/revenue_by_gender.png")
plt.close()

# 7. Monthly revenue
monthly_sales = (
    df.set_index("Date")
    .resample("MS")["Total Amount"]
    .sum()
)

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Revenue in 2023")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("results/monthly_revenue.png")
plt.close()

# 8. Display key findings
print("\nKEY FINDINGS")
print("=" * 40)

print("\nRevenue by product category:")
print(category_sales)

print("\nRevenue by gender:")
print(gender_sales)

print("\nTotal revenue:", df["Total Amount"].sum())
print("Average transaction amount:", round(df["Total Amount"].mean(), 2))

print("\nAll graphs saved in the results folder.")
