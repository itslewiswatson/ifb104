#----------------------------------------------------------------
#
# SAVEABLE SHOPPING LIST
#
# NB: To do this exercise you must have already completed one of
# the "shopping list" exercises.
#
# In the previous "shopping list" exercise you created a GUI
# which allowed the user to select grocery items and add them to
# a list of such items which was displayed in the user
# interface.  However, the list is lost when the GUI is closed
# down.  Extend your solution so that:
#
# a) It has a button labelled "Save" that can be pressed at
# any time; and
#
# b) When the "save" button is pressed the current contents of
# the list are written to a text file "shopping_list.txt".
#
# To do this you will need to use a list-valued variable to
# keep track of the current contents of the list.
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

# Introduce a list to keep track of the user's choices
items_chosen = []

# Function to display the current choice when the button is pushed
# and add to the list of items chosen
def display_choice():
    shopping_list.insert(END, choices.get() + '\n')
    items_chosen.append(choices.get())

# Function to write the contents of the user's shopping list
# to a text file
def save_list():
    output_file = open('shopping_list.txt', 'w')
    for item in items_chosen:
        output_file.write(item + '\n')
    output_file.close()
    
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

# Create the "save" button
save_button = Button(window, text = ' Save list ',
                     activeforeground = 'red',
                     font = ('Arial', 20), command = save_list)

# Use the geometry manager to "pack" the widgets onto
# the window (with a margin around the widgets for neatness)
margin_size = 5
shopping_list.pack(padx = margin_size, pady = margin_size)
choices.pack(pady = margin_size)
add_to_list.pack(pady = margin_size)
save_button.pack(pady = margin_size)

# Start the event loop to react to user inputs
window.mainloop()
