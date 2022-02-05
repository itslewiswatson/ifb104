#
# -----Statement of Authorship--------------------------------------- #
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10221131
#    Student name: Lewis Watson
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# ------------------------------------------------------------------ #



#-----Task Description-----------------------------------------------#
#
#  TESSELLATION
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "tessellate".  You are required to
#  complete this function so that when the program is run it fills
#  a rectangular space with differently-shaped tiles, using data
#  stored in a list to determine which tiles to place and where.
#  See the instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

cell_size = 100 # pixels (default is 100)
grid_width = 10 # squares (default is 10)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', 18, 'normal') # font for the coords
big_font = ('Arial', 24, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

#
#--------------------------------------------------------------------#

#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                        line_colour = 'slate grey',
                        draw_grid = True, mark_legend = True):
    
    # Set up the drawing canvas with enough space for the grid and
    # legend
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = 27 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(15)

    # Optionally mark the spaces for drawing the legend
    if mark_legend:
        # Left side
        goto(-(grid_width * cell_size) // 2 - 75, -25)
        write('Put your\nlegend here', align = 'right', font = big_font)    
        # Right side
        goto((grid_width * cell_size) // 2 + 75, -25)
        write('Put your\nlegend here', align = 'left', font = big_font) 

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the "tesselate" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_pattern" function appearing below.
# Your program must work correctly for any data set that can be
# generated by the random_pattern function.
#
# Each of the data sets is a list of instructions, each specifying
# where to place a particular tile.  The general form of each
# instruction is
#
#     [squares, mystery_value]
#
# where there may be one, two or four squares in the grid listed
# at the beginning.  This tells us which grid squares must be
# filled by this particular tile.  This information also tells
# us which shape of tile to produce.  A "big" tile will occupy
# four grid squares, a "small" tile will occupy one square, a
# "wide" tile will occupy two squares in the same row, and a
# "tall" tile will occupy two squares in the same column.  The
# purpose of the "mystery value" will be revealed in Part B of
# the assignment.
#
# Note that the fixed patterns below assume the grid has its
# default size of 10x7 squares.
#

# Some starting points - the following fixed patterns place
# just a single tile in the grid, in one of the corners.

# Small tile
fixed_pattern_0 = [['A1', 'O']]
fixed_pattern_1 = [['J7', 'X']]

# Wide tile
fixed_pattern_2 = [['A7', 'B7', 'O']]
fixed_pattern_3 = [['I1', 'J1', 'X']]

# Tall tile
fixed_pattern_4 = [['A1', 'A2', 'O']]
fixed_pattern_5 = [['J6', 'J7', 'X']]

# Big tile
fixed_pattern_6 = [['A6', 'B6', 'A7', 'B7', 'O']]
fixed_pattern_7 = [['I1', 'J1', 'I2', 'J2', 'X']]

# Each of these patterns puts multiple copies of the same
# type of tile in the grid.

# Small tiles
fixed_pattern_8 = [['E1', 'O'],
                   ['J4', 'O'],
                   ['C5', 'O'],
                   ['B1', 'O'],
                   ['I1', 'O']] 
fixed_pattern_9 = [['C6', 'X'],
                   ['I4', 'X'],
                   ['D6', 'X'],
                   ['J5', 'X'],
                   ['F6', 'X'],
                   ['F7', 'X']]

# Wide tiles
fixed_pattern_10 = [['A4', 'B4', 'O'],
                    ['C1', 'D1', 'O'],
                    ['C7', 'D7', 'O'],
                    ['A7', 'B7', 'O'],
                    ['D4', 'E4', 'O']] 
fixed_pattern_11 = [['D7', 'E7', 'X'],
                    ['G7', 'H7', 'X'],
                    ['H5', 'I5', 'X'],
                    ['B3', 'C3', 'X']]

# Tall tiles
fixed_pattern_12 = [['J2', 'J3', 'O'],
                    ['E5', 'E6', 'O'],
                    ['I1', 'I2', 'O'],
                    ['E1', 'E2', 'O'],
                    ['D3', 'D4', 'O']] 
fixed_pattern_13 = [['H4', 'H5', 'X'],
                    ['F1', 'F2', 'X'],
                    ['E2', 'E3', 'X'],
                    ['C4', 'C5', 'X']]

# Big tiles
fixed_pattern_14 = [['E5', 'F5', 'E6', 'F6', 'O'],
                    ['I5', 'J5', 'I6', 'J6', 'O'],
                    ['C2', 'D2', 'C3', 'D3', 'O'],
                    ['H2', 'I2', 'H3', 'I3', 'O'],
                    ['A3', 'B3', 'A4', 'B4', 'O']] 
fixed_pattern_15 = [['G2', 'H2', 'G3', 'H3', 'X'],
                    ['E5', 'F5', 'E6', 'F6', 'X'],
                    ['E3', 'F3', 'E4', 'F4', 'X'],
                    ['B3', 'C3', 'B4', 'C4', 'X']]

# Each of these patterns puts one instance of each type
# of tile in the grid.
fixed_pattern_16 = [['I5', 'O'],
                    ['E1', 'F1', 'E2', 'F2', 'O'],
                    ['J5', 'J6', 'O'],
                    ['G7', 'H7', 'O']]
fixed_pattern_17 = [['G7', 'H7', 'X'],
                    ['B7', 'X'],
                    ['A5', 'B5', 'A6', 'B6', 'X'],
                    ['D2', 'D3', 'X']]

fixed_pattern_18 = [['G7', 'H7', 'X']]

# If you want to create your own test data sets put them here,
# otherwise call function random_pattern to obtain data sets
# that fill the entire grid with tiles.
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a
# tessellation to draw.  Your program must work for any data set that
# can be returned by this function.  The results returned by calling
# this function will be used as the argument to your "tessellate"
# function during marking.  For convenience during code development
# and marking this function also prints the pattern to be drawn to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
# This function attempts to place tiles using a largest-to-smallest
# greedy algorithm.  However, it randomises the placement of the
# tiles and makes no attempt to avoid trying the same location more
# than once, so it's not very efficient and doesn't maximise the
# number of larger tiles placed.  In the worst case, only one big
# tile will be placed in the grid (but this is very unlikely)!
#
# As well as the coordinates for each tile, an additional value which
# is either an 'O' or 'X' accompanies each one.  The purpose of this
# "mystery" value will be revealed in Part B of the assignment.
#
def random_pattern(print_pattern = True):
    # Keep track of squares already occupied
    been_there = []
    # Initialise the pattern
    pattern = []
    # Percent chance of the mystery value being an X
    mystery_probability = 8

    # Attempt to place as many 2x2 tiles as possible, up to a fixed limit
    attempts = 10
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are all free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there) and \
           (not [column + 1, row] in been_there) and \
           (not [column + 1, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1],
                                       [column + 1, row], [column + 1, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            chr(column + ord('A') + 1) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 1x2 tiles as possible, up to a fixed limit
    attempts = 15
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 1)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 2x1 tiles as possible, up to a fixed limit
    attempts = 20
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 1)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column + 1, row] in been_there):
            been_there = been_there + [[column, row], [column + 1, row]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Fill all remaining spaces with 1x1 tiles
    for column in range(0, grid_width):
        for row in range(0, grid_height):
            if not [column, row] in been_there:
                been_there.append([column, row])
                # Append the tile's coords to the pattern, plus the mystery value
                pattern.append([chr(column + ord('A')) + str(row + 1),
                                'X' if randint(1, 100) <= mystery_probability else 'O'])

    # Remove any residual structure in the pattern
    shuffle(pattern)
    # Print the pattern to the shell window, nicely laid out
    print('Draw the tiles in this sequence:')
    print(str(pattern).replace('],', '],\n'))
    # Return the tessellation pattern
    return pattern

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "tessellate" function.
#

# Global variables
current_tile = ''
current_tile_type = ''

# Constants
tile_types = ['1x1', '2x1', '1x2', '2x2']
fairy_bread_sprinkle_colours = ['red', 'green', 'pink', 'gold', 'goldenrod', 'cornflower blue', 'medium purple']
sprinkle_count = 49
draw_function_prefix = 'draw_' # Dynamic function calling
legend = [
    ['L1'],
    ['L2'],
    ['L3'],
    ['L4'],
]

# Outline side lengths for each type
# [y, x, y, x]
outline_steps = {
    '1x1': [100, 100, 100, 100],
    '1x2': [200, 100, 200, 100],
    '2x1': [100, 200, 100, 200],
    '2x2': [200, 200, 200, 200]
}

# Repetitive turtle movement instructions
bread_curve_instructions = [
    ['right', 10],
    ['forward', 5],
    ['right', 5],
    ['forward', 5],
    ['right', 15],
    ['forward', 5],
    ['right', 20],
    ['forward', 5],
    ['right', 15],
    ['forward', 5],
    ['right', 25]
]

vegemite_jar_curve_instructions = [
    ['right', 30],
    ['forward', 5],
    ['right', 30],
    ['forward', 5],
    ['left', 20],
    ['forward', 5],
    ['left', 40],
    ['forward', 10],
    ['right', 90]
]

# Measurements
vegemite_logo_shape = {
    'side': 40,
    'inner': 70,
	'outer': 110
}
assert((vegemite_logo_shape['inner'] + vegemite_logo_shape['outer']) == 180) ## Validate that sides sum to 180

# ------------------------------ UTILITY FUNCTIONS ------------------------------ #

# Call functions via their string names
def call_function(func: str, args: list):
    # If it exists in the global scope
    if func in globals():
        # Call function
        globals()[func](*args)
        return True
    
    print('Fatal error: could not find specified function')
    return False

# Execute an array of instructions (that resolve to a function)
def execute_instructions(instructions: list):
    for instruction in instructions:
        function_name, args = instruction[0], instruction[1]
        call_function(function_name, [args])

# Resolve tiles to 1x1, 2x2, etc
def get_tile_type(pattern: list) -> str:
    pattern_length = len(pattern)
    if (pattern_length == 1):
        # Custom override for the legend
        return 'LEGEND'
    elif (pattern_length == 2):
        return '1x1'
    elif (pattern_length == 3):
        # Share the same letter (vertical)
        if (pattern[0][0] == pattern[1][0]):
            return '1x2'
        # Share the same number (horizontal)
        elif (pattern[0][1] == pattern[1][1]):
            return '2x1'
        else:
            return ''
    elif (pattern_length == 5):
        return '2x2'
    else:
        return ''

def is_tile_broken(tile_pattern: list) -> bool:
    tile_pattern_length = len(tile_pattern)

    # Legend tiles cannot be broken
    if (tile_pattern == 1):
        return False
    
    if (tile_pattern[tile_pattern_length - 1] == 'X'):
        return True
    
    return False

# Decode a tile's coordinates
def decode_tile(tile_string: str) -> dict:
    # Reject invalid tile strings
    if (len(tile_string) != 2):
        print('Invalid tile string')
    
    letter, number = tile_string[0], int(tile_string[1])

    # Override for legend
    if (tile_string[0] == 'L'):
        return detailed_legend[tile_string]

    return {
        'x': convert_to_x_coordinate(letter),
        'y': convert_to_y_coordinate(number)
    }

# Draw an outline for a specified tile
def draw_outline(outline_type: str):
    # Don't draw outline for legend
    if (current_tile[0] == 'L'):
        return

    goto_tile(current_tile)
    pencolor('black')
    pensize(2)
    setheading(90)
    pendown()
    for steps in outline_steps[outline_type]:
        forward(steps)
        right(90)
    penup()
    
    goto_tile(current_tile)

# Go to cartesian origin (-500, -350)
def goto_custom_origin():
    penup()
    home() # Go to absolute 0, 0

    # Go to bottom (A1) tile
    setheading(270)
    forward(350)
    setheading(180)
    forward(500)
    setheading(0)

# Convert x coordinate to cartesian form
def convert_to_x_coordinate(letter: str) -> int:
    assert(ord('A') == 65) # Test we get correct values
    ordinary = ord(letter) - 65
    adjusted = ordinary * 100
    adjusted -= 500 # account for negative coordinate
    return adjusted

# Convert y coordinate to cartesian form
def convert_to_y_coordinate(num: int) -> int:
    assert(num >= 1) # Test for positive int
    adjusted = (num * 100) - 350 # account for negative coordinates
    adjusted -= 100 # account for zero-indexing
    return adjusted

# Go to a specified tile
def goto_tile(tile_coordinate: str):
    decoded_tile = decode_tile(tile_coordinate) # Decode for coordinates
    tile_origin_x, tile_origin_y = decoded_tile['x'], decoded_tile['y']
	# Go to coordinates and reset heading
    goto(tile_origin_x, tile_origin_y)
    setheading(0)

# ------------------------------ DRAWING TYPES ------------------------------ #
draw_types = {
    '1x1': 'fairy_bread',
    '2x1': 'australian_flag',
    '1x2': 'vegemite',
    '2x2': 'uluru',
    'LEGEND': 'legend'
}

detailed_legend = {
    'L1': {
        'x': -750,
        'y': 200,
        'type': '2x1',
        'info': 'Australian Flag'
    },
    'L2': {
        'x': -700,
        'y': -200,
        'type': '1x2',
        'info': 'Vegemite'
    },
    'L3': {
        'x': 550,
        'y': 50,
        'type': '2x2',
        'info': 'Uluru'
    },
    'L4': {
        'x': 600,
        'y': -200,
        'type': '1x1',
        'info': 'Fairy Bread'
    }
}

def draw_fairy_bread():    
    draw_fairy_bread_background()
    draw_fairy_bread_crust()
    draw_fairy_bread_sprinkes()

def draw_australian_flag():
    draw_australian_flag_background()
    draw_union_jack()
    draw_flag_stars()

def draw_vegemite():
    draw_vegemite_background()
    draw_vegemite_jar()
    draw_vegemite_lid()

def draw_uluru():
    draw_uluru_sky()
    draw_uluru_ground()
    draw_uluru_rock()

# ------------------------------ TESSELLATION ------------------------------ #
# Fill the grid with tiles as per the provided dataset
def tessellate(given_pattern: list):
    goto_custom_origin()

    # Concat with legend so they are all drawn with same consideration
    given_pattern += legend

    for pattern in given_pattern:
        # Get the tile type
        tile_type = get_tile_type(pattern)

        # Store the current tile globally
        global current_tile
        global current_tile_type
        current_tile = pattern[0]
        current_tile_type = tile_type

        # Go to the bottom left tile in given pattern
        goto_tile(current_tile)

        # Draw the current tile's content
        drawing_function = draw_function_prefix + draw_types[tile_type]
        call_function(drawing_function, [])

        # Draw 'broken' overlay if applicable
        if (is_tile_broken(pattern)):
            break_current_tile()
        
        # Draw the current tile's outline
        draw_outline(tile_type)

# ------------------------------ LEGEND ------------------------------ #
def draw_legend():
    # Draw as normal
    current_tile_info = detailed_legend[current_tile]
    tile_type = current_tile_info['type']
    to_execute = draw_function_prefix + draw_types[tile_type]
    call_function(to_execute, [])

    # Go below the tile and write what it is
    goto_tile(current_tile)
    setheading(270)
    forward(25)
    setheading(0)
    color('black')
    write(detailed_legend[current_tile]['info'], font=('Arial', '14', 'normal'))

# ------------------------------ TILE BREAKAGE  ------------------------------ #
def draw_tile_break(height: int, width: int):
    # Pen settings
    pencolor('grey')
    fillcolor('grey')
    pensize(3)

    # Move to offset
    setheading(90)
    height_offset_1 = height * 0.4
    forward(height_offset_1)

    # Work out some useful measurements
    hypo = sqrt(height ** 2 + width ** 2)
    angle_1 = degrees(atan2(height, width))
    adjusted_angle_1 = 90 - angle_1

    begin_fill() # Fill 1/2
    # First grouping
    right(adjusted_angle_1)
    distance_1 = hypo * 0.6
    forward(distance_1)

    # Second groupig
    penup()
    goto_tile(current_tile)
    setheading(0)
    forward(width)
    pendown()

    # Third grouping
    setheading(90)
    left(45)
    distance_2 = 50
    forward(distance_2)
    width_elapsed = (distance_2) * cos(radians(45))
    height_elapsed = width_elapsed
    end_fill()

    # Store this so we can come back to it
    intersect_x, intersect_y = xcor(), ycor()

    begin_fill() # Fill 2/2
    setheading(90)
    penup()
    forward(height - height_elapsed)

	# Complete grouping
    goto(intersect_x, intersect_y)
    pendown()
    setheading(45)
    forward(50)
    setheading(90)
    forward(height - 2 * height_elapsed)
    end_fill()

    penup()
    pensize(1)

# Break the current tile
def break_current_tile():
    # use current_tile_type to determine which to draw
    goto_tile(current_tile)

    tile_dimensions = outline_steps[current_tile_type]
    tile_height = tile_dimensions[0]
    tile_width = tile_dimensions[1]

    draw_tile_break(tile_height, tile_width)

# ------------------------------ AUSTRALIAN FLAG ------------------------------ #

def draw_australian_flag_background():
    # Navy background
    pencolor('navy')
    color('navy')

    setheading(90)
    pendown()
    begin_fill()
    for side_length in outline_steps['2x1']:
        forward(side_length)
        right(90)
    end_fill()
    penup()
    setheading(0)

def draw_union_jack():
    # Function-scoped local variables
    hypotenuse = 100
    y_axis_change = hypotenuse * sin(radians(25))
    x_axis_change = hypotenuse * cos(radians(25))

    def move_to_union_jack_position():
        left(90)
        forward(95)
        right(115)
        forward(5)
    
    def draw_union_jack_diagonal_stripes():
        # Draw downwards trending stripe
        pendown()
        forward(hypotenuse)
        penup()

        # Move to next one
        setheading(0)
        left(90)
        forward(y_axis_change)

        # Draw upwards trending stripe
        pendown()
        left(115)
        forward(hypotenuse)
        penup()

    def draw_union_jack_horizontal_stripe():
        # Move to position
        setheading(90)
        forward(y_axis_change / 2)

        # Draw
        pendown()
        right(90)
        forward(x_axis_change)
        penup()

    def draw_union_jack_vertical_stripe():
        # Move to position
        left(90)
        forward(y_axis_change / 2)
        left(90)
        forward(x_axis_change / 2)
        left(90)

        # Draw
        pendown()
        forward(y_axis_change)
        penup()

    def draw_partial_union_jack(smallpen: int, bigpen: int, pcol: str):
        move_to_union_jack_position()

        pencolor(pcol)
        pensize(smallpen)
        draw_union_jack_diagonal_stripes()

        pensize(bigpen)
        draw_union_jack_horizontal_stripe()
        draw_union_jack_vertical_stripe()

        goto_tile(current_tile)
        setheading(0)
    
    draw_partial_union_jack(10, 12, 'white')
    draw_partial_union_jack(4, 6, 'red')

# Star utility function
def draw_star(size: int, sides: int):
    angle = 144
    pendown()
    begin_fill()
    for side in range(sides):
        forward(size)
        right(720 / sides)
    end_fill()
    penup()
    setheading(0)

# List of flag stars and their properties
flag_stars = [
    # Commonwealth Star
    {
        'steps': [
            ['forward', 44],
            ['left', 90],
            ['forward', 18]
        ],
        'options': {
            'size': 15,
            'sides': 7
        }
    },
    # Southern cross stars
    {
        'steps': [
            ['forward', 145],
            ['left', 90],
            ['forward', 12]
        ],
        'options': {
            'size': 9,
            'sides': 7
        }
    },
    {
        'steps': [
            ['forward', 175],
            ['left', 90],
            ['forward', 60]
        ],
        'options': {
            'size': 9,
            'sides': 7
        }
    },
    {
        'steps': [
            ['forward', 165],
            ['left', 90],
            ['forward', 40]
        ],
        'options': {
            'size': 5,
            'sides': 5
        }
    },
    {
        'steps': [
            ['forward', 145],
            ['left', 90],
            ['forward', 80]
        ],
        'options': {
            'size': 9,
            'sides': 7
        }
    },
    {
        'steps': [
            ['forward', 120],
            ['left', 90],
            ['forward', 50]
        ],
        'options': {
            'size': 9,
            'sides': 7
        }
    }
]

def use_star_pen_settings():
    color('white')
    pencolor('white')
    pensize(1)

def draw_flag_stars():
    use_star_pen_settings()

    for star in flag_stars:
        goto_tile(current_tile)
        execute_instructions(star['steps'])
        draw_star(star['options']['size'], star['options']['sides'])

# ------------------------------ VEGEMITE ------------------------------ #

def use_vegemite_logo_pen_settings():
    pencolor('red')
    color('red')
    
def use_vegemite_jar_pen_settings():
    pencolor('saddlebrown')
    color('saddlebrown')

def use_vegemite_label_pen_settings():
    pencolor('gold')
    color('gold')

def use_vegemite_bg_pen_settings():
    pencolor('green')
    color('green')

def draw_vegemite_background():
    use_vegemite_bg_pen_settings()
    setheading(90)
    pendown()
    begin_fill()
    for side_length in outline_steps['1x2']:
        forward(side_length)
        right(90)
    end_fill()
    penup()
    setheading(0)

def draw_vegemite_logo():
    use_vegemite_logo_pen_settings()

    # Move into position
    right(90)
    forward(40)
    left(90)
    forward(20)

    right(vegemite_logo_shape['outer'] / 2) # Get into position
    pendown()
    begin_fill()
    forward(vegemite_logo_shape['side'])
    left(vegemite_logo_shape['outer'])
    forward(vegemite_logo_shape['side'])
    left(vegemite_logo_shape['inner'])
    forward(vegemite_logo_shape['side'])
    left(vegemite_logo_shape['outer'])
    forward(vegemite_logo_shape['side'])
    end_fill()
    penup()
    goto_tile(current_tile)

def draw_vegemite_label():
    use_vegemite_label_pen_settings()
    right(90)
    begin_fill()
    forward(80)
    right(90)
    forward(81)
    right(90)
    forward(80)
    right(90)
    forward(81)
    right(90)
    end_fill()
    penup()
    
def draw_vegemite_jar_bottom():
    # Move into position
    forward(10)
    left(90)
    forward(40)

    use_vegemite_jar_pen_settings()

    pendown()
    begin_fill()
    setheading(270)
    left(30)
    forward(10)
    left(30)
    forward(10)
    setheading(0)
    forward(55)
    left(30)
    forward(10)
    left(30)
    forward(10)
    setheading(180)
    forward(81)
    end_fill()
    penup()

def draw_vegemite_jar_top():
    # Move to position
    forward(10)
    left(90)
    forward(120)

    use_vegemite_jar_pen_settings()

    pendown()
    begin_fill()
    execute_instructions(vegemite_jar_curve_instructions)
    forward(60)
    execute_instructions(reversed(vegemite_jar_curve_instructions))
    setheading(180)
    forward(81)
    end_fill()
    penup()

def draw_vegemite_jar():
    draw_vegemite_jar_bottom()
    draw_vegemite_label()
    draw_vegemite_logo()
    draw_vegemite_jar_top()  
      
def draw_vegemite_lid():
    # Move into position
    right(90)
    forward(20)

    use_vegemite_label_pen_settings()

    pendown()
    begin_fill()
    forward(30)
    right(90)
    forward(81)
    right(90)
    forward(30)
    right(90)
    forward(81)
    end_fill()
    penup()

# ------------------------------ FAIRY BREAD ------------------------------ #

def get_sprinkle_count():
    return sprinkle_count

def use_fairy_bread_gb_pen_settings():
    color('violet')
    pencolor('violet')

def use_fairy_bread_pen_settings():
    color('linen')
    pencolor('wheat')
    pensize(5)

def draw_fairy_bread_background():
    use_fairy_bread_gb_pen_settings()
    pendown()
    begin_fill()
    for times in range(4):
        forward(100)
        left(90)
    end_fill()
    penup()

def move_to_fairy_bread_position():
    forward(10)
    left(90)
    forward(10)

def draw_fairy_bread_crust():
    move_to_fairy_bread_position()
    use_fairy_bread_pen_settings()
    draw_fairy_bread_middle()

def draw_fairy_bread_middle():
    pendown()
    begin_fill()

    forward(65)
    execute_instructions(bread_curve_instructions)
    forward(55)
    execute_instructions(reversed(bread_curve_instructions))
    forward(65)
    right(90)
    forward(80)

    end_fill()
    penup()

def draw_fairy_bread_sprinkes():
    # Move to position
    right(135)
    forward(15)
    right(45)

    # Add extra one to account for last sprinkle ;)
    for sprinkle in range(1, get_sprinkle_count() + 1):
        dot(5, choice(fairy_bread_sprinkle_colours))

        # Alternating row rotation based on row count
        if (sprinkle % 7 == 0):
            rotation = 90
            if (sprinkle % 14 == 0):
                rotation = 270
            left(rotation)
            forward(10)
            left(rotation)
            continue
        forward(10)

# ------------------------------ ULURU ------------------------------ #
def use_uluru_sky_pen_settings():
    pencolor('dodger blue')
    color('dodger blue')

def use_uluru_ground_pen_settings():
    pencolor('sandy brown')
    color('sandy brown')

def use_uluru_rock_pen_settings():
    pencolor('chocolate')
    color('chocolate')

def draw_uluru_sky():
    use_uluru_sky_pen_settings()

    pendown()
    begin_fill()
    for steps in outline_steps['2x2']:
        forward(steps)
        left(90)
    end_fill()
    penup()

def draw_uluru_ground():
    use_uluru_ground_pen_settings()

    pendown()
    begin_fill()
    left(90)
    forward(95)
    right(90)
    forward(200)
    right(90)
    forward(95)
    right(90)
    forward(200)
    end_fill()
    penup()

    setheading(0)

def draw_uluru_rock():
    use_uluru_rock_pen_settings()

    # Move to position
    forward(12)
    left(90)
    forward(80)

    pendown()
    begin_fill()

    # Left side
    right(20)
    forward(40)
    right(20)
    forward(5)

    # Top
    right(45)
    forward(60)
    setheading(0)
    right(10)
    forward(15)
    setheading(0)
    left(10)
    forward(5)
    setheading(0)
    
    # Right side
    right(10)
    forward(70)
    setheading(0)
    right(70)
    forward(35)
    right(20)
    forward(10)
    setheading(180)
    forward(175)

    end_fill()
    penup()

#--------------------------------------------------------------------#


#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and mark the places for the
# ***** legend, by providing arguments to this function call
create_drawing_canvas('light grey', 'slate grey', True, False)

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tiles
title("Iconic Australian Things: Tile Edition")

### Call the student's function to follow the path
### ***** While developing your program you can call the tessellate
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_pattern()" as the
### ***** argument.  Your tessellate function must work for any data
### ***** set that can be returned by the random_pattern function.
#tessellate(fixed_pattern_17) # <-- used for code development only, not marking
tessellate(random_pattern()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
