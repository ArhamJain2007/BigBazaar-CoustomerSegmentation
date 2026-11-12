
import pandas as pd

# Load original customer data
original_data = pd.read_csv("Data/customers.csv")

# Load clustered data
clustered_data = pd.read_csv("Output/Graphs/clustered_customers.csv")

# Add cluster labels to original data
original_data["Cluster"] = clustered_data["Cluster"]

# Calculate average values for each cluster
cluster_summary = original_data.groupby("Cluster").agg({
    "age": "mean",
    "annual_income": "mean",
    "spending_score": "mean",
    "visit_frequency": "mean",
    "average_basket_value": "mean",
    "annual_spending": "mean",
    "days_since_last_visit": "mean"
})

print("\nCustomer Cluster Analysis:")
print(cluster_summary.round(2))

# Save the results
cluster_summary.to_csv("Output/Graphs/cluster_summary.csv")

# Save customer data with original values and cluster labels
original_data.to_csv(
    "Output/Graphs/final_customer_segments.csv",
    index=False
)

print("\nCustomer analysis completed!")


import matplotlib.pyplot as plt

# Plot customer segments
plt.figure(figsize=(9, 6))

for cluster in sorted(original_data["Cluster"].unique()):

    cluster_data = original_data[
        original_data["Cluster"] == cluster
    ]

    plt.scatter(
        cluster_data["annual_income"],
        cluster_data["spending_score"],
        label="Cluster " + str(cluster),
        alpha=0.6
    )

plt.title("Big Bazaar Customer Segmentation")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.savefig("Output/Graphs/customer_segments.png")
plt.show()

print("Customer segmentation graph generated!")
