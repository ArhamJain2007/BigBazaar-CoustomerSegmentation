
import mysql.connector
from getpass import getpass

def create_connection():

    password = getpass("Enter MySQL password: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="bigbazaar_db"
    )

    return connection
