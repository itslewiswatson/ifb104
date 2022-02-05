# Change Calculator
#
# THE PROBLEM
#
# You need to calculate how much change is due when you go shopping.
# You have a $20 note and buy the following:
#   2 cartons of milk @ $2.50
#   5 Mars bars @ $1.20 each
#   1 pkt indigestion tablets @ $3.50
#
# Write an expression to calculate the change you should be given
# from $20, after buying those groceries.  Display the value of the
# change in a message to the screen.

# HINTS:
# * You will need to use built-in mathematical operators: *, + and -
# * You may like to introduce variables to accumulate and store values
# * The Python function call "print(E)" will print the value of expression E

initial = 20

milk_price = 2.5
milk_quant = 2

mars_price = 1.2
mars_quant = 5

tblt_price = 3.5
tblt_quant = 1

total_cost = (milk_price * milk_quant) + (mars_price * mars_quant) + (tblt_price * tblt_quant)
print("Total cost comes to $" + str(total_cost))

change_leftover = initial - total_cost
print("There is $" + str(change_leftover) + " in change left over")