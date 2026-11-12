
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

# Load customer data
data = pd.read_csv("Data/customers.csv")

print("Original dataset shape:", data.shape)

# Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# Remove duplicate records
data = data.drop_duplicates()

# Fill missing numerical values with median
for column in data.select_dtypes(include=["number"]).columns:
    data[column] = data[column].fillna(data[column].median())

# Fill missing gender with most common value
data["gender"] = data["gender"].fillna(data["gender"].mode()[0])

# Convert gender into numerical values
data["gender"] = data["gender"].map({
    "Male": 0,
    "Female": 1
})

# Select numerical features for clustering
features = [
    "age",
    "gender",
    "annual_income",
    "spending_score",
    "visit_frequency",
    "average_basket_value",
    "annual_spending",
    "days_since_last_visit"
]

# Handle outliers using IQR method
for column in features:

    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    data[column] = data[column].clip(
        lower_limit, upper_limit)

# Select features for clustering
X = data[features]

# Apply feature scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(X)

# Convert scaled data into dataframe
scaled_df = pd.DataFrame(
    scaled_data,
    columns=features
)

# Save preprocessed data
scaled_df.to_csv(
    "Data/cleaned_data.csv",
    index=False
)

# Save scaler for future use
with open("Models/scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)

print("\nPreprocessing completed successfully!")

print("\nFinal dataset shape:", scaled_df.shape)

print("\nFirst five processed records:")
print(scaled_df.head())
