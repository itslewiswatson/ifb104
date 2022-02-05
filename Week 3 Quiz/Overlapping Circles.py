
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task I agree that it represents my own work.
#  I am aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  Student no:      n10221131
#  Student name:    Lewis Watson
#
#--------------------------------------------------------------------#

# DEAR MARKER
# 	I'm using a Surface laptop which has a wacky screen DPI
# 	so the view in my Turtle window might be different and skew the
# 	widths and all of that

#-----Task Description-----------------------------------------------#




from turtle import *
delay(0)
pensize(2.5)

def draw_circle():
	pendown()
	begin_fill()
	circle(90)
	end_fill()
	penup()
	sety(ycor() - (90 * 0.85))

color("black", "blue")
draw_circle()
color("black", "red")
draw_circle()
color("black", "yellow")
draw_circle()
color("black", "green")
draw_circle()

hideturtle()
done()
