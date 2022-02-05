#-----Description----------------------------------------------------#
#
#  Definition Finder (Step 2)
#
#  Given a word, this program displays the corresponding definition
#  from "The Foolish Dictionary" by Gideon Wurdz (1904).  This is
#  the complete system, integrating the front-end GUI with the
#  back-end search function.  To integrate the results of the
#  previous steps you must do the following.
#
#  a) Modify the back-end function so that instead of accepting
#     the word as a parameter it gets the word from the text Entry
#     widget.
#
#  b) Modify the back-end function so that instead of printing the
#     definition it inserts it into the appropriate GUI Text widget.
#
#  Time permitting you may also want to make other improvements to
#  the integrated system, such as the following.
#
#  c) Make the back-end function robust to the possibility that
#     the text file containing the dictionary can't be opened.
#
#  d) Extend the GUI so that the user can initiate a search by
#     hitting the 'Enter' key, as well as pushing the button.
#
#--------------------------------------------------------------------#


# Import the necessary regular expression functions
from re import findall, sub

# Import the Tkinter functions
from tkinter import *


#--------------------------------------------------------------------#
# Back-end function to find and display the definition, if any. 
# (The optional 'event' parameter allows this function to be
# the target of a key binding.)
#
def show_definition():
    pass
    ##### PUT THE BACK-END FUNCTION PRODUCED BY TEAM A HERE AND
    ##### CONNECT IT TO THE GUI

        
#----------------------------------------------------------------#
# The GUI front end
#

# Create a window
dictionary_window = Tk()

# Give the window a title
dictionary_window.title('The Foolish Dictionary')


##### PUT THE WIDGETS CREATED BY TEAM B HERE


# Start the event loop
dictionary_window.mainloop()

#
#--------------------------------------------------------------------#

