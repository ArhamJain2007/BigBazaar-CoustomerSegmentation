
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load original customer data
data = pd.read_csv("Data/customers.csv")

# Create output folder graphs

# 1. Income distribution
plt.figure(figsize=(8, 5))
plt.hist(data["annual_income"], bins=20)
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income")
plt.ylabel("Number of Customers")
plt.savefig("Output/Graphs/income_distribution.png")
plt.show()

# 2. Spending score distribution
plt.figure(figsize=(8, 5))
plt.hist(data["spending_score"], bins=20)
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Number of Customers")
plt.savefig("Output/Graphs/spending_distribution.png")
plt.show()

# 3. Income vs Spending Score
plt.figure(figsize=(8, 5))
plt.scatter(data["annual_income"], data["spending_score"])
plt.title("Annual Income vs Spending Score")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.savefig("Output/Graphs/income_vs_spending.png")
plt.show()

# 4. Correlation heatmap
numeric_data = data.select_dtypes(include=["number"])
numeric_data = numeric_data.drop(columns=["customer_id"])

plt.figure(figsize=(10, 7))
sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Customer Data Correlation Heatmap")
plt.savefig("Output/Graphs/correlation_heatmap.png")
plt.show()

# 5. Box plot
plt.figure(figsize=(10, 5))
sns.boxplot(data=numeric_data)
plt.title("Customer Features Box Plot")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Output/Graphs/box_plot.png")
plt.show()

print("All graphs generated successfully!")
