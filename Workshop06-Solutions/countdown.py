#----------------------------------------------------------------
#
# COUNTDOWN
#
# In this exercise you must create a Graphical User
# Interface using tkinter.  The program should create
# a window containing a label and a button.  The label
# displays a number and each time the button is pressed
# the number in the label should decrease by 1 until
# it reaches zero, at which some other value can be
# displayed.  This will give you practice at both
# creating widgets and getting them to interact.
#

# Import the necessary tkinter functions
from tkinter import Tk, Button, Label

# Create a window
countdown_window = Tk()

# Give the window a title
countdown_window.title('Countdown')

# Global variable to remember the number
label_value = 10

# Function to execute when the button is pressed
def decrement():
    global label_value
    if label_value == 1:
        the_label['text'] = 'Go!'
    else:
        label_value = label_value - 1
        the_label['text'] = str(label_value)

# Create a button widget whose parent container is the
# window
the_button = Button(countdown_window, text = ' Push ',
                    font = ('Arial', 24), command = decrement)

# Create a label
the_label = Label(countdown_window, text = str(label_value),
                  font = ('Arial', 34))

# Call the geometry manager to "pack" the widgets onto
# the window (with a blank margin around the widgets)
margin_size = 5
the_button.pack(padx = margin_size, pady = margin_size)
the_label.pack(pady = margin_size)

# Start the event loop to react to user inputs
countdown_window.mainloop()
