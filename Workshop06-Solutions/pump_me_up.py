#----------------------------------------------------------------
#
# PUMP ME UP
#
# In this exercise you must create a Graphical User
# Interface using tkinter.  The program should create
# a window containing a progress bar and a button.  When
# pressed, the button must advance the progress bar by
# a small, fixed amount.  (The progress bar will 'wrap
# around' to zero when it reaches its maximum value.
# By default progress bars show values from 0 to 99.)
#
# Hint: The Progressbar widget has a method called "step"
# that advances the bar by a given amount.
#
# WARNING: This exercise relies on the "ttk" package
# which offers some extra widgets beyond those provided
# by tkinter, including the Progressbar widget needed
# here.  It's possible that the ttk module may not be
# installed in some older Python installations.  If you
# get an error when trying to import from ttk you will
# not be able to complete this exercise.
#

# Import the necessary Tkinter functions
from tkinter import Tk, Button, VERTICAL
from tkinter.ttk import Progressbar

# Percentage to advance "progress" at each button push
step_size = 10

# Create a window
the_window = Tk()

# Give the window a title
the_window.title('Pump me up!')

# Function to execute when the button is pressed
def advance():
    the_bar.step(step_size)

# Create a button widget whose parent container is the
# window
the_button = Button(the_window, text = ' Push ',
                    font = ('Arial', 24), command = advance)

# Create a progress bar widget in the parent window (making the
# maximum value displayable 101% because the bar's value
# returns to zero when 100 is reached, i.e., it displays values
# from 0 to 99, inclusive, by default)
the_bar = Progressbar(the_window, orient = VERTICAL,
                      length = 300, maximum = 101)

# Call the geometry manager to "pack" the widgets onto
# the window (with a blank margin around the widgets)
margin_size = 5
the_button.pack(padx = margin_size, pady = margin_size)
the_bar.pack(pady = margin_size)

# Start the event loop to react to user inputs
the_window.mainloop()
