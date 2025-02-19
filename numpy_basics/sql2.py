from mysql.connector import connect
import pandas as pd
from sqlalchemy import create_engine

db = {
    'database': 'fil',  
    'user': 'root',
    'password': 'chessChess2*2*',
    'host': 'localhost',
    'port': 3306
}

try:
    cnx = connect(**db)
    print("Database connection successful!")
except Exception as e:
    print("Error connecting to the database:", e)


query = "SELECT * FROM tips" 
df = pd.read_sql(query, cnx)

print(df)  
