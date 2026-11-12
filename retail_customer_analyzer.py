 import pandas as pd

    # Loading Customer Data
    def load_data():
        try:
            df = pd.read_csv("customers.csv")
            return df
        except FileNotFoundError:
            print("Error: customers.csv file not found.")
            return None


    # Spending Statistics
    def spending_statistics(df):
        mean_spend = df["TotalSpent"].mean()
        median_spend = df["TotalSpent"].median()

        highest = df.loc[df["TotalSpent"].idxmax()]
        lowest = df.loc[df["TotalSpent"].idxmin()]

        print(f"Mean spend: Rs. {mean_spend:.2f}")
        print(f"Median spend: Rs. {median_spend:.2f}")
        print(f"Highest: {highest['Name']} (Rs. {int(highest['TotalSpent'])})")
        print(f"Lowest: {lowest['Name']} (Rs. {int(lowest['TotalSpent'])})")


    # High Value Customers
    def high_value_customers(df):
        limit_input = input("Enter spending limit: ")

        try:
            limit = float(limit_input)

            if limit < 0:
                print("Amount must be 0 or more.")
                return

            customers = df[df["TotalSpent"] >= limit]

            display_limit = int(limit) if limit.is_integer() else limit
            print(f"\nHigh-value customers (TotalSpent >= {display_limit}):")

            if customers.empty:
                print("No customers found.")
            else:
                for _, row in customers.iterrows():
                    print(
                        row["CustomerID"], "|",
                        row["Name"], "|",
                        row["City"], "| Rs.",
                        int(row["TotalSpent"])
                    )

        except ValueError:
            print("Invalid amount. Please enter a number.")


    # City Wise Summary
    def city_wise_summary(df):
        summary = df.groupby("City")["TotalSpent"].agg(
            ["sum", "mean"]
        ).sort_values(by="sum", ascending=False)

        for city, row in summary.iterrows():
            print(
                f"{city} : Total Rs. {int(row['sum'])} | "
                f"Average Rs. {row['mean']:.2f}"
            )


    # Main Program
    def main():
        df = load_data()

        if df is None:
            return

        while True:
            print("\n===== RETAIL CUSTOMER ANALYZER =====")
            print("1. Spending statistics")
            print("2. High-value customers")
            print("3. City-wise summary")
            print("4. Exit")

            choice = input("Enter your choice: ").strip().lower()

            if choice in ["1", "spending statistics"]:
                spending_statistics(df)

            elif choice in ["2", "high-value customers"]:
                high_value_customers(df)

            elif choice in ["3", "city-wise summary"]:
                city_wise_summary(df)

            elif choice in ["4", "exit"]:
                print("Thank you for using Retail Customer Analyzer!")
                break

            else:
                print("Invalid menu choice. Please try again.")


    if __name__ == "__main__":
        main()
