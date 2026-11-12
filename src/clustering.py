import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load preprocessed data
data = pd.read_csv("Data/cleaned_data.csv")

# Find the best number of clusters
inertia_values = []
silhouette_values = []

for k in range(2, 11):

    model = KMeans(n_clusters=k, random_state=42, n_init=10)

    model.fit(data)

    inertia_values.append(model.inertia_)

    score = silhouette_score(data, model.labels_)
    silhouette_values.append(score)

    print("Clusters:", k, "Silhouette Score:", round(score, 3))


# Elbow Method Graph
plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), inertia_values, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.savefig("Output/Graphs/elbow_method.png")
plt.show()


# Silhouette Score Graph
plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), silhouette_values, marker="o")
plt.title("Silhouette Score")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.savefig("Output/Graphs/silhouette_score.png")
plt.show()

print("\nCluster evaluation completed!")


# Train final K-Means model

final_model = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

# Assign clusters to customers
data["Cluster"] = final_model.fit_predict(data)

# Save clustered customer data
data.to_csv("Output/Graphs/clustered_customers.csv", index=False)

# Save the model
import pickle

with open("Models/kmeans_model.pkl", "wb") as file:
    pickle.dump(final_model, file)

print("\nFinal K-Means model trained successfully!")

print("\nNumber of customers in each cluster:")
print(data["Cluster"].value_counts())

print("\nCluster averages:")
print(data.groupby("Cluster").mean())