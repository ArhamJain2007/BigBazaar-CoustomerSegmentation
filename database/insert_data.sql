USE bigbazaar_db;

SELECT COUNT(*) AS total_customers
FROM customers;

SELECT COUNT(*) AS total_purchase_records
FROM purchase_history;

SELECT *
FROM customers
LIMIT 10;

SELECT *
FROM purchase_history
LIMIT 10;