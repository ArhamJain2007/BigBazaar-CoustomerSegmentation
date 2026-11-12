
import pandas as pd
from db_connection import create_connection

# Connect to MySQL
connection = create_connection()

# Fetch data from both tables
query = """
SELECT
    c.customer_id,
    c.age,
    c.gender,
    c.annual_income,
    p.spending_score,
    p.visit_frequency,
    p.average_basket_value,
    p.annual_spending,
    p.days_since_last_visit
FROM customers c
JOIN purchase_history p
ON c.customer_id = p.customer_id
"""

# Load data into dataframe
data = pd.read_sql(query, connection)

print("\nData loaded successfully!")

print("\nFirst five records:")
print(data.head())

print("\nDataset information:")
data.info()

print("\nDataset shape:")
print(data.shape)

# Save data into CSV
data.to_csv("Data/customers.csv", index=False)

print("\nData saved successfully!")
connection.close()
