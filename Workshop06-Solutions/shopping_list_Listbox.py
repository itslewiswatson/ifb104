#----------------------------------------------------------------
#
# SHOPPING LIST
#
# In this exercise you will develop a Graphical User
# Interface using tkinter.  The program must create a
# window containing a text box, a list box and
# a button. The options in the list box are typical
# grocery items.  Each time the user selects a grocery
# item in the list and presses the button it
# should be displayed in the text box, to create
# a personalised shopping list.
#

# Import the necessary tkinter functions needed to create
# the window and the three widgets
from tkinter import Tk, Text, Button, Listbox

# Import the tkinter constant END which is useful when
# we want to add text to the end of a Text area or an
# item to the end of a Listbox
from tkinter import END

# Our list of choices
groceries = ['Eggs', 'Milk', 'Bread', 'Coffee', 'Tea', 'Lettuce',
             'Tomatoes', 'Onions', 'Chicken', 'Cheese', 'Fish',
             'Sugar', 'Rice', 'Pasta', 'Soup', 'Cereal', 'Yogurt']

# Create a window
window = Tk()

# Give the window a title
window.title('Shopping list')

# Function to display the current choice when the button is pushed
# (this version first checks to ensure than an item has been selected
# before doing anything)
def display_choice():
    if choices.curselection() != ():
        shopping_list.insert(END, choices.get(choices.curselection()) + '\n')

# Create a text area to display the user's choices
shopping_list = Text(window, width = 30, height = 10,
                     font = ('Arial', 20),
                     borderwidth = 2, relief = 'groove')

# Create a listbox widget which displays the grocery list
# in alphabetical order
choices = Listbox(window, font = ('Arial', 20), height = len(groceries))
for item in sorted(groceries):
    choices.insert(END, item)

# Create a button to push when the user is happy with their choice
add_to_list = Button(window, text = ' Add to list ',
                     font = ('Arial', 20), command = display_choice)

# Use the geometry manager to "pack" the widgets onto
# the window (with a margin around the widgets for neatness)
margin_size = 5
shopping_list.pack(padx = margin_size, pady = margin_size)
choices.pack(pady = margin_size)
add_to_list.pack(pady = margin_size)

# Start the event loop to react to user inputs
window.mainloop()
