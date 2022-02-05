#---------------------------------------------------------------------
#
# Treasure Island cliches
#
# Robert Louis Stevenson's classic novel "Treasure Island" has been
# the subject of countless parodies ever since its publication.
# In this exercise you will put some of these cliches
# to the test using regular expressions to search for various
# phrases in the book's text.
#
# The program below opens a copy of the novel and reads it as a
# Python string.  Your task is to use regular expressions to search
# it for the patterns described below and print any matches found,
# one per line.
#

# Import the regex findall function
from re import findall

# Read the contents of the novel (assuming you have a copy of the
# file in the same folder as this program)
#
source = open('TreasureIsland.html')
text = source.read()
source.close()

# Do pirates really exclaim, "Aha!" a lot?  To find out, search
# the text for this four-letter pattern and print how many
# matches you get
#
print("There are", len(findall('Aha!', text)), "'Aha!'s in the novel.")
print("(So much for that cliche!)") # There are none!
print()

# We all know that "Jim" is the protagonist of the novel, as
# exemplified by the cliche "Aha, Jim lad!", but what's Jim's
# full name?  Find out by searching for the following pattern and
# printing all the matches you find:
#
# 'Jim' followed by a space followed by a capital letter followed
# by one or more lower-case letters
#
print("Possible surnames for the lad 'Jim':")
for match in findall('Jim [A-Z][a-z]+', text):
    print(match)
print()

# Pirates are notorious for their love of rum.  Find and print
# all occurrences of the word "rum", with and without an initial
# capital letter.  Also print the number of times the word occurs.
# Be careful to ensure that you are matching a whole word and not
# part of a larger word such as 'drum'.
#
matches = findall('\\b[Rr]um\\b', text)
print("There are", len(matches), "instances of 'rum':")
for match in findall('\\b[Rr]um\\b', text):
    print(match)
print()

# Something else we learned from Treasure Island is that
# pirate captains always have a parrot sitting on their shoulder.
# In this case the parrot is notorious for screeching
# the same phrase, over and over: "Pieces of X!".  Use your
# skills with regular expressions to find out what word X is.
#
print("Captain Flint, the parrot, always says, 'Pieces of ", end = "")
print(findall('Pieces of ([a-z]+)!', text)[0] + "!'") # we happen to know there is only one matching word in this case
print()

# In a novel about pirates it's inevitable that many ship's
# captains are mentioned.  Sometimes they're referred to as
# "Captain X" and sometimes as "Cap'n X".  Find all references
# to captains in either form and print them in alphabetical
# order and without duplicates.  Challenge: You must complete
# this task using only a single call to "findall".  You can't
# call the function twice for the two different patterns.
# (Observation: One of these "captains" is the parrot!)
#
print("Captains mentioned (including the parrot!):")
matches = findall("Cap(?:'|tai)n [A-Z][a-z]+", text)
for match in sorted(set(matches)): # NB: a set doesn't contain duplicates
    print(match)
print()
