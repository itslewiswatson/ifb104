#----------------------------------------------------------------
#
# ALTERNATIVE SHOPPING LIST
#
# In this exercise you will develop a Graphical User
# Interface using tkinter.  In another workshop exercise
# you created a "shopping list" application using tkinter's
# Listbox and Text widgets.  Apart from selecting pre-defined
# grocery items from the Listvox, it was also possible to
# manually type items into the Text area.  In this exercise
# you will provide a different user interface for doing this
# job, this time using the ttk module's Combobox widget.
#
# WARNING: This exercise relies on the "ttk" package
# which offers some extra widgets beyond those provided
# by tkinter, including the Combobox widget needed
# here.  It's possible that the ttk module may not be
# installed in some older Python installations.  If you
# get an error when trying to import from ttk you will
# not be able to complete this exercise.
#
# In this version of the "shopping list" application you
# must create a window containing a Text box, a Combobox and
# a Button widget. The options in the Combobox are typical
# grocery items.  Each time the user selects a grocery
# item in the Combobox and presses the Button the item
# should be displayed in the Text box, to create
# a shopping list.  Users can also enter items not in
# the default shopping list into the Combobox manually.
#

# Import the necessary tkinter functions
from tkinter import Tk, Text, Button, END
from tkinter.ttk import Combobox

# Create a window
window = Tk()

# Give the window a title
window.title('Shopping list')

# Create a list of choices
groceries = ['Eggs', 'Milk', 'Bread', 'Coffee', 'Tea', 'Lettuce',
             'Tomatoes', 'Onions', 'Chicken', 'Cheese', 'Fish',
             'Sugar', 'Rice', 'Pasta', 'Soup', 'Cereal', 'Yogurt']

# Function to display the current choice when the button is pushed
def display_choice():
    shopping_list.insert(END, choices.get() + '\n')
    
# Create a text area to display the user's choice
shopping_list = Text(window, width = 30, height = 10,
                     font = ('Arial', 20),
                     borderwidth = 2, relief = 'groove')

# Create a combo box widget whose parent container is the
# window
choices = Combobox(window, values = groceries)

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
