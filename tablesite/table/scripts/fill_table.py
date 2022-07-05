import json
import sys
from psycopg2 import connect, Error
from psycopg2.extras import RealDictCursor
import time

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

host = 'localhost'
db_name = 'market_data'
user = 'postgres'
password = '154326'

# connecting to database
while True:
    try:
        conn = connect(host=host, database=db_name,
                        user=user, password=password,
                        cursor_factory=RealDictCursor)
        # cursor_factory will give a column name with value
        # (it will return dicitonary "column":"value")
        cursor = conn.cursor()
        print("Database connected")
        break
    except Exception as error:
        print("Connecting to Database failed")
        print("Error: ", error)
        time.sleep(2)


def fill_table():
    table_name = "public.market_data"

    with open('table/templates/table/db.json', 'r') as json_data:

        data = json.load(json_data)

    columns = list(data[0].keys())

    row_data = []
    for row in data:
        for value in row.values():
            row_data.append(value)
        cursor.execute("""INSERT INTO %s (%s, %s, %s, %s) VALUES (%s, %s, %s, %s)""",
                       (table_name, columns[0],  columns[1],  columns[2],  columns[3],
                        row_data[0], row_data[1], row_data[2], row_data[3]))
        conn.commit()
        row_data.clear()


fill_table()
