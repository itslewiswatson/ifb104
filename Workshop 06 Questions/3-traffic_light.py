#----------------------------------------------------------------
#
# TRAFFIC LIGHT
#
# In this exercise you must create a Graphical User
# Interface using tkinter.  The program should create
# a window containing a drawing canvas and three buttons.
# Each time one of the buttons is pressed a red, yellow
# or green circle should be drawn on the canvas, in
# imitation of a traffic light.  Note that the "create_oval"
# method can be applied to a "canvas" object to draw a circle.
#
# As an additional feature, you should enable and
# disable the buttons so that the lights can only follow
# the usual green-yellow-red-green sequencing.  (There is no
# yellow between red and green in real traffic lights!)
# This can be done by changing the "state" of the buttons
# to "normal" or "disabled" as appropriate.
#

# Import the necessary tkinter functions
from tkinter import Tk, Button, Canvas

# Create a window
traffic_window = Tk()

# Give the window a title
traffic_window.title('Traffic Light')


###### PUT YOUR CODE HERE

# 1. Define functions to be called when one of the buttons
#    is pressed which will create appropriately coloured
#    ovals on the drawing canvas, using the "create_oval"
#    "Canvas" method with an appropriate "fill" colour
#    parameter

# 2. Create the three Button widgets and pack them into
#    the main window

# 3. Create the drawing Canvas widget and pack it into the
#    main window


# Start the event loop to react to user inputs
traffic_window.mainloop()
