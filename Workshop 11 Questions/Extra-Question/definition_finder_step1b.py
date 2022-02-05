#-----Description----------------------------------------------------#
#
#  Definition Finder - GUI Mock Up (Step 1b)
#
#  In this step your team will create a mock-up of the Graphical
#  User Interface for the definition finder.  It should have all
#  the necessary widgets and GUI functionality, but the back-end
#  search function will be just a stub.
#
#  The stub function has been provided below.  When called all it
#  does is print a message to the Python shell window to remind
#  the development team that this stub needs to be replaced.
#
#  Your team needs to implement the GUI front-end that calls this
#  stub.  The GUI must have at least the following features:
#
#  a) A Text widget to display the dictionary definition (or error
#     messages.
#
#  b) A text Entry widget to allow the user to type in the word
#     they want defined.
#
#  c) A Button widget which, when pressed, calls the back-end
#     "show_definition" function to search for and display the
#     definition from the dictionary (which, of course, won't
#     work until the stub is replaced).
#
#--------------------------------------------------------------------#


#--------------------------------------------------------------------#
# Back-end function to find and display the definition, if any. 
# TODO: This is just a stub!
#
def show_definition():
    print('FIXME: This is a stub for the back-end search function')

        
#----------------------------------------------------------------#
# The GUI front end
#

# Import the Tkinter functions
from tkinter import *

# Create a window
dictionary_window = Tk()

# Give the window a title
dictionary_window.title('The Foolish Dictionary')


######## CREATE YOUR WIDGETS HERE


# Start the event loop
dictionary_window.mainloop()

#
#--------------------------------------------------------------------#

