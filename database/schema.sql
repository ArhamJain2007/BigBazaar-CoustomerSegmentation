CREATE DATABASE IF NOT EXISTS bigbazaar_db;

USE bigbazaar_db;

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    annual_income FLOAT
);

CREATE TABLE IF NOT EXISTS purchase_history (
    purchase_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT UNIQUE,
    spending_score FLOAT,
    visit_frequency INT,
    average_basket_value FLOAT,
    annual_spending FLOAT,
    days_since_last_visit INT,
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);