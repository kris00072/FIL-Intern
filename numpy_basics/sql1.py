from sqlalchemy import create_engine
import pandas as pd
import pymysql
data1=pd.read_csv('tips.csv')
from mysql.connector import connection

db={
    'name':'fil',
    'user':'root',
    'password':'chessChess2*2*',
    'host':'localhost',
    'port':3306

}
from sqlalchemy import create_engine
engine1 = create_engine("mysql+pymysql://root:chessChess2*2*@localhost/fil")

data1.to_sql(name="tips", con=engine1, if_exists="replace", index=False)
