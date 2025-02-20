import snowflake.connector
import pandas as pd


conn = snowflake.connector.connect(
    user='KRIS007',
    password='chessChess2*2*',
    account='lg01426.ap-southeast-1', 
    warehouse='COMPUTE_WH',
    database='FIDELITY_TEST',
    schema='MY_SCHEMA'
)


query = "SELECT * FROM MY_SCHEMA.test2;"  


df = pd.read_sql(query, conn)


conn.close()


print(df)
