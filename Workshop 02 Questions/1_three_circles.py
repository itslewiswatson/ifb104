# Three non-overlapping circles
#
# As a simple exercise in using the Turtle package you are
# required to draw three circles on the screen.  Each circle
# must be of a different size and colour.  Most importantly,
# the circles must not touch or overlap at any point, nor
# can one circle appear inside another.
#
# NB: We want unfilled circles, so you can't use Turtle's
# "dot" function for this purpose.  Also, you must ensure that
# lines are not drawn between or connecting the circles.
#
# The basic strategy for drawing each circle is to lift
# up the pen, move to a suitable location on the screen,
# choose a colour, put the pen down and walk in a circle.
# Having done this once you can copy your code (with minor
# changes) three times.
#
# Observation: Turtle's "circle" function does NOT draw a
# circle centred at the current location.  Instead it causes
# the turtle to walk in a circle, ending up back where
# it started.

from turtle import *

setup()
title('Three non-overlapping circles')
speed('fastest')
delay(0)

# Initial position
penup()
left(90)
forward(50)

# First circle
color('green', 'yellow')
pendown()
setheading(0)
for x in range(360):
	forward(2)
	setheading(x)
penup()

# Move down the screen
right(90)
forward(180)

# Second circle
color('blue', 'pink')
pendown()
setheading(0)
for x in range(360):
	forward(1.3)
	setheading(x)
penup()

# Move down the screen
right(90)
forward(180)

# Third circle
color('red', 'orange')
pendown()
setheading(0)
for x in range(360):
	forward(1.5)
	setheading(x)
penup()

hideturtle()
done()
