import pandas as pd

# Creating Customer Data
data = {
    "CustomerID": ["C01", "C02", "C03", "C04", "C05",
                   "C06", "C07", "C08", "C09", "C10"],

    "Name": ["Asha", "Rahul", "Aman", "Priya", "Rohit",
             "Neha", "Karan", "Sneha", "Vikas", "Anjali"],

    "City": ["Raipur", "Bhilai", "Raipur", "Durg", "Bhilai",
             "Raipur", "Durg", "Bhilai", "Raipur", "Durg"],

    "Purchases": [5, 3, 8, 2, 6, 4, 7, 3, 5, 9],

    "TotalSpent": [12000, 6000, 25000, 3000, 15000,
                   9000, 18000, 4000, 11000, 30000]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display Customer Data
print("===== RETAIL CUSTOMER DATA =====")
print(df)

# Total Customers
print("\nTotal Customers:", len(df))

# Total Purchases
print("Total Purchases:", df["Purchases"].sum())

# Total Revenue
print("Total Revenue: Rs.", df["TotalSpent"].sum())

# Average Spending
print("Average Spending: Rs.", df["TotalSpent"].mean())

# Highest Spending Customer
highest = df.loc[df["TotalSpent"].idxmax()]

print("\n===== HIGHEST SPENDING CUSTOMER =====")
print(highest)

# City Wise Analysis
print("\n===== CITY WISE CUSTOMER ANALYSIS =====")
print(df.groupby("City")["TotalSpent"].sum())

# Sorting Customers by Spending
print("\n===== CUSTOMER SPENDING RANKING =====")
print(df.sort_values(by="TotalSpent", ascending=False))
