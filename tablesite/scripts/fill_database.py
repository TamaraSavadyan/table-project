import json, sys
from psycopg2 import connect, Error
from psycopg2.extras import RealDictCursor
import time

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

with open('tablesite/table/templates/table/db.json', 'r') as json_data:

    data = json.load(json_data)


# connecting to database
while True:
    try:
        conn = connect(host='localhost', database='market_data',
                                user='postgres', password='154326',
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


# #!/usr/bin/python3
# # -*- coding: utf-8 -*-

# # import the psycopg2 database adapter for PostgreSQL
# from psycopg2 import connect, Error

# # import Python's built-in JSON library
# import json

# # import the JSON library from psycopg2.extras
# from psycopg2.extras import Json

# # import psycopg2's 'json' using an alias
# from psycopg2.extras import json as psycop_json

# # import Python's 'sys' library
# import sys

# # accept command line arguments for the Postgres table name
# if len(sys.argv) > 1:
#     table_name = '_'.join(sys.argv[1:])
# else:
#     # ..otherwise revert to a default table name
#     table_name = "json_data"

# print ("\ntable name for JSON data:", table_name)

# # use Python's open() function to load the JSON data
# with open('postgres-records.json') as json_data:

#     # use load() rather than loads() for JSON files
#     record_list = json.load(json_data)

# print ("\nrecords:", record_list)
# print ("\nJSON records object type:", type(record_list)) # should return "<class 'list'>"

# # concatenate an SQL string
# sql_string = 'INSERT INTO {} '.format( table_name )

# # if record list then get column names from first key
# if type(record_list) == list:
#     first_record = record_list[0]

#     columns = list(first_record.keys())
#     print ("\ncolumn names:", columns)

# # if just one dict obj or nested JSON dict
# else:
#     print ("Needs to be an array of JSON objects")
#     sys.exit()

# # enclose the column names within parenthesis
# sql_string += "(" + ', '.join(columns) + ")\nVALUES "

# # enumerate over the record
# for i, record_dict in enumerate(record_list):

#     # iterate over the values of each record dict object
#     values = []
#     for col_names, val in record_dict.items():

#         # Postgres strings must be enclosed with single quotes
#         if type(val) == str:
#             # escape apostrophies with two single quotations
#             val = val.replace("'", "''")
#             val = "'" + val + "'"

#         values += [ str(val) ]

#     # join the list of values and enclose record in parenthesis
#     sql_string += "(" + ', '.join(values) + "),\n"

# # remove the last comma and end statement with a semicolon
# sql_string = sql_string[:-2] + ";"

# print ("\nSQL string:")
# print (sql_string)