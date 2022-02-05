#---------------------------------------------------------
#
# Print a sorted database table
#
# As a more sophisticated example of querying a database,
# here you must write a Python function that prints the
# city code, city name and country name from the "cities"
# and "countries" tables of the Airline database.  The result
# should appear in alphabetical order by city name first, then
# by country name (which ensures that Brisbane, Australia
# comes before Brisbane, USA!).
#
# Your function should produce the following output when
# called.  NB: This assumes you have already completed
# all the steps in the Insert City exercise, so that
# cities like Denver, which were not in the original tables,
# appear below.  Also notice that cities such as
# Amsterdam, whose countries are not listed in the
# "countries" table, do NOT appear below because we
# cannot get their corresponding country name from the
# database.
#
#     ADL: Adelaide, Australia
#     ANT: Atlanta, United States of America
#     AKL: Auckland, New Zealand
#     BNE: Brisbane, Australia
#     BRI: Brisbane, United States of America
#     CBR: Canberra, Australia
#     DEN: Denver, United States of America
#     HNL: Honolulu, United States of America
#     CGK: Jakarta, Indonesia
#     LAX: Los Angeles, United States of America
#     MEL: Melbourne, Australia
#     PER: Perth, Australia
#     SFO: San Francisco, United States of America
#     SYD: Sydney, Australia
#
# Do this in two steps:
#
# 1) First devise an appropriate SELECT query in the
# database's graphical interface.
#
# 2) Using this query, then develop corresponding
# Python code to access the database, run the query,
# and display the results.
#


#---------------------------------------------------------

# Import the SQL functions
from sqlite3 import *

# Connect to the airline database and print the city code,
# city name and country code from the cities table.

# 1. Make a connection to the airline database
connection = connect(database = "airline.db")

# 2. Get a cursor on the database
airline = connection.cursor()

# 3. Construct the SQL query
sql = "SELECT CityCode, CityName, CountryName \
       FROM cities, countries \
       WHERE cities.CountryCode = countries.CountryCode \
       ORDER BY CityName, CountryName"

# 4. Execute the query
airline.execute(sql)

# 5. Get the result set and print it out
rows = airline.fetchall()
for row in rows:
    print(row[0] + ': ' + row[1] + ', ' + row[2])

# 6. Close the cursor and connection
airline.close()
connection.close()
