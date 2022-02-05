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

# Functions to execute when the buttons are pressed (with
# restrictions to only allow buttons to be pressed if the
# green-yellow-red-green sequencing is followed)
def red_light():
    traffic_light.create_oval(10, 10, 190, 190, fill = 'red')
    red_button['state'] = "disabled"
    yellow_button['state'] = "disabled"
    green_button['state'] = "normal"
    
def yellow_light():
    traffic_light.create_oval(10, 10, 190, 190, fill = 'yellow')
    yellow_button['state'] = "disabled"
    green_button['state'] = "disabled"
    red_button['state'] = "normal"
    
def green_light():
    traffic_light.create_oval(10, 10, 190, 190, fill = 'green')
    green_button['state'] = "disabled"
    yellow_button['state'] = "normal"
    red_button['state'] = "disabled"

# Create the three button widgets
red_button = Button(traffic_window, text = 'Red',
                    width = 6, command = red_light)
yellow_button = Button(traffic_window, text = 'Yellow',
                       width = 6, command = yellow_light)
green_button = Button(traffic_window, text = 'Green',
                      width = 6, command = green_light)

# Create the drawing canvas
traffic_light = Canvas(traffic_window, width = 200,
                       height = 200, bg = 'white')

# Call the geometry manager to place the widgets onto
# the window (in a grid arrangement, with a margin)
margin_size = 5
traffic_light.grid(padx = margin_size, pady = margin_size,
                   row = 0, column = 0, columnspan = 3)
green_button.grid(pady = margin_size, row = 1, column = 2)
yellow_button.grid(pady = margin_size, row = 1, column = 1)
red_button.grid(pady = margin_size, row = 1, column = 0)

# Start the event loop to react to user inputs
traffic_window.mainloop()
