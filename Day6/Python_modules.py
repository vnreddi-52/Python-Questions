import os
import sys
import datetime
import math
from datetime import datetime
from pathlib import Path
from collections import Counter
import sqlite3

# print(math.sqrt(81))

# print(math.ceil(5.0))

# print(math.floor(5.6))

# print(math.factorial(5))

# now = datetime.now()
# print(now)

# files = Path(".").glob("main.py")

# for file in files:
#     print(file)

# print(sys.argv)

# nums=[1,2,3,4,4,5,6,]
# print(Counter(nums))


connection = sqlite3.connect("students.db")  # connect to the database

cursor = connection.cursor() # create the connection for me - connecting sqlite with server

cursor.execute("""
CREATE  TABLE IF NOT EXISTS students(
id INTEGER,
name TEXT
)
""")

connection.commit()
connection.close()

