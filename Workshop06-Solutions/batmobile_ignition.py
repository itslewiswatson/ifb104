#----------------------------------------------------------------
#
# BATMOBILE IGNITION 
#
# In this exercise you will use radio buttons to control the
# text in a label.
#
# The scenario: Here you will emulate part of the Batmobile's
# dashboard display from the 1966 "Batman" television show.
# In each episode Batman and Robin would leap into the
# nuclear-powered Batmobile and Robin would read the ignition
# status from the dashboard:
#
#     "Atomic batteries to 'Power'. Turbines to 'Speed'."
#
# Upon hearing this, Batman would always reply:
#
#     "Roger. Ready to move out."
#
# The Batmobile would then roar out of the Batcave for the
# 14 mile journey from stately Wayne Manor to Gotham City.
#
# In this exercise you will create two pairs of radio buttons,
# one for the atomic batteries' status and one for the turbines'
# status.  A text label will display the state of the Batmobile,
# which should be "Ready" only when the buttons are in the
# configuration described by Robin above.  See the instructions
# accompanying this file for full details.
#
# Notes:
# 1) For neatness we have put the radio buttons into LabelFrame
#    widgets in our final version, but you need not bother
#    with the frames in your first attempt.
# 2) Only one radio button from a group can be selected at a time.
#    All buttons that refer to the same variable are part of
#    the same group.
# 3) The LabelFrame widget has an optional 'text' parameter which
#    can be used to give a name to the frame.
#

# Import the necessary tkinter functions
from tkinter import Tk, LabelFrame, Label, BooleanVar, Radiobutton

# 1. Create a Tk window (and a default font)
dashboard = Tk()
bat_font = ('Arial', 22)

# 2. Give the window a title
dashboard.title('Batmobile Ignition')

# 3. Create a Label widget to displays the Batmobile's
# ignition status (initially "Waiting...")
ignition_status = Label(dashboard, text = 'Waiting...', fg = 'red',
                        font = ('Times', 42), width = 8)

# 4. Introduce two Boolean variables, whose values will be changed
# by selecting radio buttons, for the atomic batteries' and turbines'
# statuses, respectively
atomic_batteries_status = BooleanVar()
turbines_status = BooleanVar()

# 5. Define a function to change the label's text when the right
# radio buttons are selected
def update_dashboard():
    if atomic_batteries_status.get() and turbines_status.get():
        ignition_status['text'] = 'Ready!'
        ignition_status['fg'] = 'green'
    else:
        ignition_status['text'] = 'Waiting...'
        ignition_status['fg'] = 'red'

# 6. Create two LabelFrame widgets to hold the pairs of radio
# buttons (unlike Frames, LabelFrames have a 'text' attribute)
atomic_batteries_buttons = LabelFrame(dashboard, relief = 'groove',
                                      font = bat_font,
                                      borderwidth = 2, text = 'Atomic Batteries')
turbines_buttons = LabelFrame(dashboard, relief = 'groove',
                              font = bat_font,
                              borderwidth = 2, text = 'Turbines')

# 7. Create two radio button widgets within the batteries frame,
# labelled 'Charging' and 'Power', both referring to the same
# Boolean variable
charging_button = Radiobutton(atomic_batteries_buttons, text = 'Charging',
                              variable = atomic_batteries_status, value = False,
                              font = bat_font, command = update_dashboard)
power_button = Radiobutton(atomic_batteries_buttons, text = 'Power',
                           variable = atomic_batteries_status, value = True,
                           font = bat_font, command = update_dashboard)

# 8. Create two radio button widgets within the turbines frame,
# labelled 'Idle' and 'Speed', both referring to the same
# Boolean variable
idle_button = Radiobutton(turbines_buttons, text = 'Idle',
                          variable = turbines_status, value = False,
                          font = bat_font, command = update_dashboard)
speed_button = Radiobutton(turbines_buttons, text = 'Speed',
                           variable = turbines_status, value = True,
                           font = bat_font, command = update_dashboard)

# 9. Use the grid geometry manager to put the four radio buttons
# into their frames (each on a separate row and sticking to the
# West border)
charging_button.grid(row = 1, sticky = 'w')
power_button.grid(row = 2, sticky = 'w')
idle_button.grid(row = 1, sticky = 'w')
speed_button.grid(row = 2, sticky = 'w')

# 10. Use the grid geometry manager to put the three main widgets
# into the root window
margin = 5 # pixels
ignition_status.grid(padx = margin, pady = margin, row = 1,
                     column = 1, columnspan = 2)
atomic_batteries_buttons.grid(padx = margin, pady = margin,
                              row = 2, column = 1)
turbines_buttons.grid(padx = margin, pady = margin,
                      row = 2, column = 2)

# 11. Start the event loop to react to user inputs
dashboard.mainloop()
