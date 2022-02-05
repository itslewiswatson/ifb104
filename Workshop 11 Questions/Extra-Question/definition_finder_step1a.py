#-----Description----------------------------------------------------#
#
#  Definition Finder - Back-End Function (Step 1a)
#
#  In this step your team will implement the back end function
#  "show_definition" which, when given a word, prints the
#  corresponding definition from "The Foolish Dictionary" by Gideon
#  Wurdz (1904).  This version of the function prints the definition
#  found, if any, in the Python shell window, although the final
#  version of the function will be integrated into the GUI.  To test
#  your function we have provided a main program which calls
#  it several times. 
#
#  In this initial version, your function must perform the following
#  steps:
#
#  a) It must open the text file containing the book of interest and
#     read the contents.
#
#  b) It must get the word whose definition we want.  In this initial
#     version we assume the word is passed as a parameter to the
#     function, but in the final version we will get the word from
#     the appropriate GUI widget.
#
#  c) It must use a regular expression to find the definition
#     in the book corresponding to the word, if any.  Note that
#     each of the words defined in the dictionary appears in upper
#     case, with equals signs on either side.  The definition follows
#     this and ends with either an asterisk or another equals sign.
#     Thus a sufficient pattern to look for is an equals sign, the
#     word of interest, another equals sign, a space or a newline,
#     and then any number of characters which are NOT equals signs
#     or asterisks.  It is this last part that we want to return.
#
#  d) It should tidy up the definition retrieved ready for display,
#     e.g., by deleting newline characters and eliminating unnecessary
#     whitespace.
#
#  e) In this version of the function it should print the definition
#     in the Python shell window, but in the final version it will
#     insert this text into the appropriate GUI widget.
#
#  If no definition coresponding to the given word is found your
#  function should print an appropriate error message.
#
#--------------------------------------------------------------------#


# Import some helpful regular expression functions
from re import findall, sub


#--------------------------------------------------------------------#
# Back-end function to find and print the definition, if any.  This
# initial version accepts the word as a parameter and prints its
# results, rather than interacting with the GUI.
#
def show_definition(word):
    print('FIXME: Function has not been implemented')
    ##### DEVELOP YOUR CODE TO FIND AND PRINT WORD DEFINITIONS HERE


#--------------------------------------------------------------------#
# Here are some tests for your function, which should print
# the dictionary definition corresponding to each given word.
# Here the words have been provided in different mixtures of
# upper and lower case, so your function should convert them
# all to upper case before searching for their definitions.
#

show_definition('Flattery')
print()
show_definition('FISHING')
print()
show_definition('Gallantry')
print()
show_definition('globe')
print()
show_definition('sculptor')
print()
show_definition('Summer')
print()
show_definition('Internet')
