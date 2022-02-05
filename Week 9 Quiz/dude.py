comment = """
I don't understand why some folk's insist on 'incorrectly'
using apostrophe's for 'plural' words and for
'highlighting' word's as in the many errors in this
paragraph.  Apostrophes are used for quotation's, to
mark abbreviation's and to indicate possession, but
'never' for plurals or emphasis.
"""

from re import *

print(findall("'([a-z]+)'", comment))
print(findall("'([A-Za-z0-9]*)'", comment))