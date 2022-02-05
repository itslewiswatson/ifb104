# Average speed
#
# Imagine that you get on your bicycle and travel from
# your home to QUT at 30 km/hr.  After a hard day's
# study you cycle home again more slowly at 20 km/hr.
#
# Quickly now, what is your average speed for the whole
# round trip?  Be careful - most people get this
# wrong!  (Thanks to Professor Julius Sumner Miller for
# this brainteaser.)
#
# To check the correct answer, complete the code below.
# We have chosen an arbitrary distance of 6 km between
# your house and the university but the result is the
# same regardless of the distance.


# Given values:

distance_from_home_to_uni = 6 # km

speed_from_home_to_uni = 30 # km/hr

speed_from_uni_to_home = 20 # km/hr


# Complete the following code by replacing the zeros:

time_to_get_to_uni = distance_from_home_to_uni / speed_from_uni_to_home # hours

time_to_get_home = distance_from_home_to_uni / speed_from_home_to_uni # hours

total_travelling_time = time_to_get_home + time_to_get_to_uni # hours

total_distance_travelled = distance_from_home_to_uni * 2 # km

speed_for_round_trip = (2 * speed_from_home_to_uni * speed_from_uni_to_home) / (speed_from_home_to_uni + speed_from_uni_to_home) # km/hr

print ('The average speed for the round trip was', speed_for_round_trip, 'km/hr')
