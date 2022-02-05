# Music download credits
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the cost in cents for downloading one
# music track, your original budget in dollars, and the number of tracks
# already downloaded:

track_cost = 120 # cost in cents for downloading one track
budget = 50 # dollars
num_downloaded = 15 # number of tracks already downloaded

# Write expressions to calculate how many more tracks you can afford
# to download and print that value to the screen.
#
# A problem solving strategy:
# 1. Calculate the amount spent so far by
#    multiplying the number downloaded by the track cost
# 2. Calculate the balance left by
#    deducting the amount spent so far from the budget
# 3. Divide the balance left by the track cost to a whole number
# 4. Print the number of tracks left
#
# Be careful to allow for the fact that one of the given values
# is expressed in cents and the other is in dollars, i.e., the
# units associated with the values are different.

# You cannot buy part of a track - use math library to round down
from math import floor

# Convert track_cost to dollars
track_cost = track_cost / 100

money_spent = track_cost * num_downloaded
print("You have currently spent $" + str(money_spent) + " of your $" + str(budget) + " budget")

money_remaining = budget - money_spent
num_tracks_can_afford = money_remaining / track_cost
print("So, you have $" + str(money_remaining) + " remaining, which means you can afford " + str(floor(num_tracks_can_afford)) + " more tracks")