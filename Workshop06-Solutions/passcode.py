#----------------------------------------------------------------
#
# PASSCODE
#
# In this challenging exercise you will will develop a GUI
# program using tkinter that comprises:
#
# 1) a ten digit keypad;
# 2) an 'OK' button; and
# 3) a text field.
#
# The program should allow numerical passcodes to be entered
# after which the OK button can be pressed.  If the passcode
# entered is a valid one then appropriate feedback should
# be provided, and similarly for invalid passcodes.
#
# The valid passcodes in this case should be your
# eight digit student numbers (with a leading zero).
#
# It is suggested that you develop this program in several
# steps:
#
# a) Write the 'back-end' function that recognises valid
#    passcodes.
# b) Develop a simple GUI 'front-end' for communicating
#    between the user and the back end, without worrying
#    about how the GUI widgets are laid out.
# c) Make the GUI look nice by laying out the widgets in
#    a natural format.
#
# Observation: To recognise the ten different digits we need
# ten separate functions attached to the buttons, meaning
# that some code will be duplicated 10 times.  Cleverer
# solutions which avoid this duplication are possible, but
# are too sophisticated for our current needs.  Brute
# force is acceptable here!
#

# Import the tkinter functions
from tkinter import *

# Create a window (and a default font)
passcode_window = Tk()
pass_font = ('Arial', 24)

# Give the window a title
passcode_window.title('Passcode')

# Back-end function to recognise valid passcodes.   In this case
# we assume there are two valid passcodes consisting of student
# numbers 01234567 and 09876543.  NB: Since these numbers
# include a leading zero we assume they are represented as
# strings, not integers.
#
def valid_passcode(code):
    return code == '01234567' or code == '09876543'

# Global variable that keeps track of the passcode entered so far
passcode = ''

# Functions that record the fact that a particular digit has
# been pressed (brute force solution)
#
def add_digit(new_digit):
    global passcode
    passcode += new_digit
    display['bg'] = 'white'
    display.insert(END, '*')
def process_zero():
    add_digit('0')
def process_one():
    add_digit('1')
def process_two():
    add_digit('2')
def process_three():
    add_digit('3')
def process_four():
    add_digit('4')
def process_five():
    add_digit('5')
def process_six():
    add_digit('6')
def process_seven():
    add_digit('7')
def process_eight():
    add_digit('8')
def process_nine():
    add_digit('9')

# Create the numeric keypad (brute force solution)
zero_button =  Button(passcode_window, text = '0', width = 3,
                      font = pass_font, command = process_zero)
zero_button.grid(column = 2, row = 4)
one_button =   Button(passcode_window, text = '1', width = 3,
                      font = pass_font, command = process_one)
one_button.grid(column = 1, row = 1)
two_button =   Button(passcode_window, text = '2', width = 3,
                      font = pass_font, command = process_two)
two_button.grid(column = 2, row = 1)
three_button = Button(passcode_window, text = '3', width = 3,
                      font = pass_font, command = process_three)
three_button.grid(column = 3, row = 1)
four_button =  Button(passcode_window, text = '4', width = 3,
                      font = pass_font, command = process_four)
four_button.grid(column = 1, row = 2)
five_button =  Button(passcode_window, text = '5', width = 3,
                      font = pass_font, command = process_five)
five_button.grid(column = 2, row = 2)
six_button =   Button(passcode_window, text = '6', width = 3,
                      font = pass_font, command = process_six)
six_button.grid(column = 3, row = 2)
seven_button = Button(passcode_window, text = '7', width = 3,
                      font = pass_font, command = process_seven)
seven_button.grid(column = 1, row = 3)
eight_button = Button(passcode_window, text = '8', width = 3,
                      font = pass_font, command = process_eight)
eight_button.grid(column = 2, row = 3)
nine_button =  Button(passcode_window, text = '9', width = 3,
                      font = pass_font, command = process_nine)
nine_button.grid(column = 3, row = 3)

# Function to process an entire passcode
#
def process_passcode():
    global passcode
    # Clear the text display
    display.delete(0.0, END)
    # Set the background colour depending on the passcode entered
    if valid_passcode(passcode):
         display['bg'] = 'green'
    else:
        display['bg'] = 'red'
    # Reset the passcode
    passcode = ''

# Create the OK button
okay_button = Button(passcode_window, text = 'OK', width = 10,
                     font = pass_font, command = process_passcode)
okay_button.grid(column = 1, row = 5, columnspan = 3)

# Create the text field for providing feedback to the
# user
display = Text(passcode_window, font = pass_font, width = 8,
               height = 1, borderwidth = 2, relief = 'groove')
display.grid(row = 6, column = 1, columnspan = 3)

# Start the event loop
passcode_window.mainloop()
