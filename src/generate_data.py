
import numpy as np
import pandas as pd
import mysql.connector
from getpass import getpass

np.random.seed(42)

# Lists to store customer details
customer_data = []
purchase_data = []

# Generate 1000 customers
for i in range(1, 1001):

    age = np.random.randint(18, 71)
    gender = np.random.choice(["Male", "Female"])

    # Randomly select customer type
    customer_type = np.random.choice(
        ["Premium", "Budget", "Frequent", "Occasional", "At Risk"],
        p=[0.18, 0.22, 0.25, 0.20, 0.15]
    )

    # Generate data according to customer type
    if customer_type == "Premium":
        income = np.random.normal(1250000, 250000)
        score = np.random.normal(85, 8)
        visits = np.random.normal(8, 2)
        basket = np.random.normal(5500, 1000)
        days = np.random.normal(5, 4)

    elif customer_type == "Budget":
        income = np.random.normal(350000, 100000)
        score = np.random.normal(35, 12)
        visits = np.random.normal(5, 2)
        basket = np.random.normal(1200, 350)
        days = np.random.normal(15, 10)

    elif customer_type == "Frequent":
        income = np.random.normal(650000, 150000)
        score = np.random.normal(70, 10)
        visits = np.random.normal(15, 3)
        basket = np.random.normal(1800, 400)
        days = np.random.normal(3, 3)

    elif customer_type == "Occasional":
        income = np.random.normal(750000, 200000)
        score = np.random.normal(40, 12)
        visits = np.random.normal(2, 1)
        basket = np.random.normal(2500, 700)
        days = np.random.normal(55, 20)

    else:
        income = np.random.normal(550000, 150000)
        score = np.random.normal(20, 10)
        visits = np.random.normal(2, 1)
        basket = np.random.normal(1300, 350)
        days = np.random.normal(110, 25)

    # Restrict values to valid ranges
    income = round(max(150000, min(income, 2000000)), 2)
    score = round(max(1, min(score, 100)), 2)
    visits = int(max(1, min(round(visits), 25)))
    basket = round(max(300, min(basket, 10000)), 2)
    days = int(max(0, min(round(days), 180)))

    # Calculate estimated annual spending
    annual_spending = round(
        visits * 12 * basket * np.random.normal(1, 0.08), 2
    )

    # Store customer details
    customer_data.append(
        [i, age, gender, income]
    )

    # Store purchase details
    purchase_data.append(
        [i, score, visits, basket, annual_spending, days]
    )

# Convert lists into DataFrames
customers = pd.DataFrame(
    customer_data,
    columns=["customer_id", "age", "gender", "annual_income"]
)

purchase_history = pd.DataFrame(
    purchase_data,
    columns=[
        "customer_id",
        "spending_score",
        "visit_frequency",
        "average_basket_value",
        "annual_spending",
        "days_since_last_visit"
    ]
)

# Connect to MySQL
password = getpass("Enter MySQL password: ")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="bigbazaar_db"
)

cursor = connection.cursor()

# Insert customer details
query1 = """
INSERT INTO customers
(customer_id, age, gender, annual_income)
VALUES (%s, %s, %s, %s)
"""

cursor.executemany(query1, customer_data)

# Insert purchase details
query2 = """
INSERT INTO purchase_history
(customer_id, spending_score, visit_frequency,
average_basket_value, annual_spending,
days_since_last_visit)
VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(query2, purchase_data)

# Save changes
connection.commit()

print("Customer data inserted successfully!")

# Check total records
cursor.execute("SELECT COUNT(*) FROM customers")
print("Total customers:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM purchase_history")
print("Total purchase records:", cursor.fetchone()[0])

cursor.close()
connection.close()
