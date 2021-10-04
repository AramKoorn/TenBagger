# Example Python program to serialize a pandas DataFrame
# into a PostgreSQL table

from sqlalchemy import create_engine
import psycopg2
import pandas as pd

# Connect to PostgreSQL DBMS
conn = psycopg2.connect(host="localhost", 
        database="portfolio", user="morty",
        password="1234")

engine = create_engine('postgres://morty:1234@localhost:5432/portfolio')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
df = pd.DataFrame([1, 2, 3], columns=["col"])
df.to_sql("hoiditwerk", con=engine, if_exists="replace")
