#---------------------------------------------------------
#
# Inserting data into a table
#
# In this exercise you will develop a Python program that
# accesses SQLite database tables.  We assume that you have
# already restored the Airline database.  (You can do so
# by running the airline.sql script.)
#
# Your tasks:
#
# 1) Using a graphical interface, insert the following city
# details into the "cities" table and examine the result,
# but don't write the details to the database.
#
#     CityCode: AMS
#     CityName: Amsterdam
#     CountryCode: NED
#
# 2) Revert the database back to its original state.
#
# 3) Using the graphical interface's SQL editor, write and
# execute an "INSERT" statement that does exactly the
# same thing.  Examine the result to confirm that your
# SQL statement adds a row just like you did interactively.
# 
# 4) Using this knowledge, write a Python function called
# "insert_city" that inserts a new entry into the cities
# table of the airline database.  Your function should
# return the number of rows inserted to confirm that the
# insertion worked.  Recall that after making a change to
# the database using a particular "cursor", that the
# attribute "cursor.rowcount" returns the number of rows
# that were affected by the change.  Some examples of
# how to call the function appear in the docstring below.
#


#---------------------------------------------------------
# The following tests will call your function
# automatically if you uncomment the main program below.
#
""" 
The following "tests" call your function to perform a series
of insertions into the database's cities table.  They check that
your function returns 1, which should mean that it has updated
one row in the table, but they don't actually check that the
database's contents have changed.  You should check this yourself
via the phpMyAdmin interface.

NB: These insertions will fail if these cities already appear
in the database, so if you run this program more than once you
may need to delete the rows from the table first.  Remember that
you can always restore the database back to its original state
by running the airline.sql script provided.

Observation: Your SQLite implementation may return integer values that
are stored using a different number of bits (binary digits) than your
Python implementation.  Therefore, the following tests all use the
built-in int function to convert the number returned to Python's
standard integer format, just in case.

>>> int(insert_city('HND', 'Tokyo', 'JAP'))
1

>>> int(insert_city('DEN', 'Denver', 'USA'))
1

>>> int(insert_city('ANT', 'Atlanta', 'USA'))
1

>>> int(insert_city('PER', 'Perth', 'AUS'))
1

>>> int(insert_city('CDG', 'Paris', 'FRA'))
1

"""


#---------------------------------------------------------

# Import the SQLite functions
from sqlite3 import *

# Connects to the airline database and inserts the city, city code
# and country into the cities table.
#
def insert_city(city_code, city, country_code):

    # 1. Make a connection to the airline database
    connection = connect(database = "airline.db")

    # 2. Get a cursor on the database
    airline = connection.cursor()

    # 3. Construct the SQLite insert statement (keeping in mind that the
    #    strings appearing in the SQLite statement must have single quotes
    #    around them)
    sql = "INSERT INTO cities VALUES('" + city_code + "', '" + city + "', '" \
          + country_code + "')"

    # 4. Execute the query
    airline.execute(sql)
    
    # 5. Get the count of the number of rows inserted
    rows_inserted = airline.rowcount

    # 6. Commit the changes to the database
    connection.commit()
    
    # 7. Close the cursor and connection
    airline.close()
    connection.close()

    # 8. Return the number of rows inserted
    return rows_inserted

    
#---------------------------------------------------------
# Uncomment this main program if you want to call your
# function automatically as per the docstring above.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))

    
