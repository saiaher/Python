import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_db"
)

query = "SELECT * FROM employees"

df = pd.read_sql(query, conn)

conn.close()

print(df)