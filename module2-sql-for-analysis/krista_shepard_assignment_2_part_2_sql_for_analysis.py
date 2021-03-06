# Import pkg and explore its directory
import pandas as pd
import psycopg2
dir(psycopg2)

# Pull necessary information from the elephantSQL website
dbname = 'zvineetb'
user = 'zvineetb'
password = 'TO DO' # Hide password before uploading to github
host = 'raja.db.elephantsql.com'

# Connect to the postgres connection that connects to elephantSQL
pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password,
                           host = host)

# Created Cursor
pg_curs = pg_conn.cursor()

# Now you can use the cursor to execute commands, this and the cell below selects all the rows from
# selects all the rows from a previously made table to make sure it is working.
pg_curs.execute('SELECT * FROM  test_table;')

pg_curs.fetchall()

# Pull the titanic csv from github and use sqlite to look at it
df = pd.read_csv('https://raw.githubusercontent.com/KryssyCo/'
                'DS-Unit-3-Sprint-2-SQL-and-Databases/master/'
                'module2-sql-for-analysis/titanic.csv')

# Replaced ' with an open str throughout df and used regex to pull information
# from the repo
df = df.replace("'", " ", regex=True)

# Listed all files including hidden files
!ls -alh

# Used !wget to pull data into python from, github
!wget https://raw.githubusercontent.com/KryssyCo/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv

# List all files again (inc. hidden files)
!ls -alh

# Take a look at first row
df.loc[0]

!wget https://github.com/KryssyCo/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module2-sql-for-analysis/titanic.sqlite3?raw=true

!ls -alh

# Rename database 
!mv 'titanic.sqlite3?raw=true' titanic.sqlite3

import sqlite3

# Established connection
sl_conn = sqlite3.connect('titanic.sqlite3')

# Create cursor
sl_curs = sl_conn.cursor()

# Execute command from cursor to count how many rows in the table
sl_curs.execute('SELECT COUNT (*) FROM titanic;').fetchall()

passengers = sl_curs.execute('SELECT * FROM titanic;').fetchall()

# Look at first row to see if it matches above
passengers[1]

# Look at the last row in the database
passengers[-1]

# Used sqkite3 ti grab the scema for the table from titanic db
sl_curs.execute('PRAGMA table_info(titanic);').fetchall()

# Change types for the move to postgres
create_titanic_table = """
  CREATE TABLE titanic (
    passenger_id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(90),
    sex VARCHAR(10),
    age FLOAT,
    siblings_spouses_aboard INT,
    parents_children INT,
    fare FLOAT
  );
"""

# Switch back to elephantSQL and create an empty table in called titanic
pg_curs.execute(create_titanic_table)

# Insert passengers into the table
passengers[1]

# Slice it and take off the id before we ass it into the postgres
str(passengers[1][1:])

# Prepping a single character to be moved to postgres
example_insert = """
INSERT INTO create_titanic_table
(field)
VALUES """ + str(passengers[1][1:]) + ';'

print(example_insert)

# But I want to insert all 888 characters from sqlite3 to elephantSQL
# I can do this by using a for loop
for index,row in df.iterrows():
  insert_record =  """ 
    INSERT INTO titanic
    (survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children, fare)
    VALUES """ + str(tuple(row.values)) + ';'
  pg_curs.execute(insert_record)

pg_curs.execute('SELECT * FROM titanic;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()
