#---------------------------------------------------------
#
# Print a table of the elements
#
# In this exercise you will develop a Python program that
# accesses an SQLite database.  We assume that you have
# already created a version of the Elements database using
# the a graphical user interface.  You can do so by executing
# the elements.sql script provided.
#
# Your tasks:
#
# 1) Browse the database's contents in an interactive interface
# to ensure that you're familiar with its two tables and
# their columns.
#
# 2) In your interactive interface, develop a SELECT query which
# prints all available details of the elements in the database.
# The result set should be ordered by atomic number as follows:
#
#   No   Name         Symbol
#   1    Hydrogen     H
#   2    Helium       He
#   3    Lithium      Li
#   4    Beryllium    Be
#   5    Boron        B
#   6    Carbon       C
#   7    Nitrogen     N
#   8    Oxygen       O
#   9    Fluorine     F
#   10   Neon         Ne
#   11   Sodium       Na
#   12   Magnesium    Mg
#   13   Aluminium    Al
#   14   Silicon      Si
#   15   Phosphorous  P
#   16   Sulphur      S
#   17   Chlorine     Cl
#   18   Argon        Ar
#   19   Potassium    K
#   20   Calcium      Ca
#   [There may be more entries here if you did the
#   first "elements" exercise]
#   121  Kryptonite   Kr
#   122  Dalekanium   Dk
# 
# 3) Using this SELECT query, write a Python program to print
# all the element details in the database.  Recall that after an
# SQLite query has been executed on a database "cursor", method call
# "cursor.fetchall()" will return a list of all rows in the
# result set, and you can then use a FOR-EACH loop to process each
# row in the list.
#


#---------------------------------------------------------

# Import the SQLite functions
from sqlite3 import *

# Connect to the elements database and print the atomic
# number, name and symbol for each element.

# 1. Make a connection to the elements database
connection = connect(database = "elements.db")

# 2. Get a cursor on the database
elements = connection.cursor()

# 3. Construct the SQLite query
query = "SELECT atomic_number, symbols.element_name, symbol \
         FROM atomic_numbers, symbols \
         WHERE atomic_numbers.element_name = symbols.element_name \
         ORDER BY atomic_number"

# 4. Execute the query
elements.execute(query)

# 5. Get the result set and print it out
print('No   Name         Symbol')
rows = elements.fetchall()
for no, name, symbol in rows:
    print(str(no).ljust(3) + '  ' + name.ljust(11) + '  ' + symbol.ljust(2))

# 6. Close the cursor and connection
elements.close()
connection.close()
