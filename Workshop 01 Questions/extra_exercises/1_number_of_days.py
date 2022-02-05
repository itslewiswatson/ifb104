# Days calculator
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, representing the number of days in each
# month of a given (non-leap) year.

january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31

year = [
	january, february, march,
	april, may, june,
	july, august, september,
	october, november, december
]

# PART 1
#
# Write an expression, or expressions, to calculate the number of days
# in each quarter (three month period) of the year, using the values
# introduced above, and print the result.
print("PART 1:")
Q1 = sum(year[:3])
Q2 = sum(year[3:6])
Q3 = sum(year[6:9])
Q4 = sum(year[9:12])
print("Q1: " + str(Q1))
print("Q2: " + str(Q2))
print("Q3: " + str(Q3))
print("Q4: " + str(Q4))
print()

# PART 2
#
# Write an expression, or expressions, to calculate the number of days
# in each half of the calendar year, and print the result.  NB: Your
# solution to Part 2 should use your solution to Part 1.
print("PART 2:")
first_half = Q1 + Q2
second_half = Q3 + Q4
print("Days in first half: " + str(first_half))
print("Days in second half: " + str(second_half))
print()

# PART 3
#
# Write an expression, or expressions, to calculate the number of days
# in the year, and print the result  NB: Your solution to Part 3
# should use your solution to Part 2.
print("PART 3:")
days_per_year = first_half + second_half
print("Days in a year: " + str(days_per_year))