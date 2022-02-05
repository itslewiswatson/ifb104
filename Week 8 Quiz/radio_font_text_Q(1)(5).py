
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task I agree that it represents my own work.
#  I am aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  Student no: n10221131
#  Student name: Lewis Watson
#
#--------------------------------------------------------------------#

#----------------------------------------------------------------
#
# 1 label, 3 radiobuttons (as per diagram) 
# Initially, the Label text "Resize Me" is displayed.
# When one of the Radiobuttons is selected by the user,
# the Label text is displayed in either a small (Arial 10),
# medium (Arial 25) or large (Arial 40) font
# according to the Radiobutton selected.
# Initially, the Label text will use the medium font specifications.

#----------------------------------------------------------------

# Import the Tkinter functions
from tkinter import *

# Create a window
the_window = Tk()

# Give the window a title
the_window.title('Resize')

# PUT YOUR CODE HERE-------------------------------------------------#

label = Label(the_window, background='orange', text='Resize Me', font=('Arial', 25), bd=2, relief=GROOVE, width=12, height=2)
label.pack(side=TOP, padx=2, pady=2, expand=True)

padding_values = [0, 8, 25];

def change_padding(val: int):
	for rad_button in buttons:
		rad_button.pack(side=LEFT, padx=padding_values[val])		

def on_select_size():
	selected = selected_rad_button.get()
	if selected == 1:
		label.config(bg='yellow', font=('Arial', 10), width=10, height=2)
		change_padding(selected - 1)	
	elif selected == 2:
		label.config(bg='orange', font=('Arial', 25), width=12, height=2)
		change_padding(selected - 1)
	elif selected == 3:
		label.config(bg='red', font=('Arial', 40), width=12, height=2)
		change_padding(selected - 1)	

selected_rad_button = IntVar()

size_small = Radiobutton(the_window, text='small', variable=selected_rad_button, value=1, command=on_select_size)
size_small.pack(side=LEFT, padx=padding_values[1])
size_medium = Radiobutton(the_window, text='medium', variable=selected_rad_button, value=2, command=on_select_size)
size_medium.pack(side=LEFT, padx=padding_values[1])
size_large = Radiobutton(the_window, text='large', variable=selected_rad_button, value=3, command=on_select_size)
size_large.pack(side=LEFT, padx=padding_values[1])

buttons = [size_small, size_medium, size_large]

# -------------------------------------------------------------------#

# Start the event loop
the_window.mainloop()
