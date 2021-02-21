# ----- Example Python program to create a database in PostgreSQL using Psycopg2 -----

# import the PostgreSQL client for Python
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# Connect to PostgreSQL DBMS
conn = psycopg2.connect(host="localhost", 
        database="financials", user="akoorn", 
        password="1234")

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE financials(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)
conn.commit()

print("Table created successfully........")

#Closing the connection
conn.close()


