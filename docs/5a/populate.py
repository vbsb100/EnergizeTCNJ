import csv
import datetime
from dateutil.parser import parse

# METERS TABLE
# reads data from CSV file into a list
with open("meters.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    rows = []
    for row in reader:
        rows.append(row)
    # removes the column headers from the list
    del rows[0]

# writes the code into the sql file
with open("stageVa.sql", "a") as file:
   for row in rows:
      file.write("\nINSERT INTO meters VALUES (\'{}\', \'{}\', \'{}\');".format(row[0],row[1],row[2]))

# METRICS TABLE
# reads data from CSV file into a list
with open("metrics.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    rows = []
    for row in reader:
        rows.append(row)
    # removes the column headers from the list
    del rows[0]

# writes the code into the sql file
with open("stageVa.sql", "a") as file:
   for row in rows:
       date = row[2]
       str = parse(date)
       d = str.date()
       file.write("\nINSERT INTO metrics VALUES (\'{}\', \'{}\', \'{}\', {}, {});".format(row[0],row[1],d, row[3], row[4]))

# EMISSIONS TABLE
# reads data from CSV file into a list
with open("emissions.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    rows = []
    for row in reader:
        rows.append(row)
    # removes the column headers from the list
    del rows[0]

# writes the code into the sql file
with open("stageVa.sql", "a") as file:
   for row in rows:
      file.write("\nINSERT INTO emissions VALUES (\'{}\', \'{}\', {});".format(row[0],row[1],row[2]))

# fuelOil TABLE
# reads data from CSV file into a list
with open("fuelOil.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    rows = []

    for row in reader:
        rows.append(row)
    # removes the column headers from the list
    del rows[0]

# writes the code into the sql file
with open("stageVa.sql", "a") as file:
   for row in rows:
       date = row[4]
       str = parse(date)
       s = str.date()
       file.write("\nINSERT INTO fuelOil VALUES (\'{}\', \'{}\', {}, {}, \'{}\');".format(row[0],row[1],row[2], row[3], s))
