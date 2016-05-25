# setting cars equal to integer 100
cars = 100

# setting space_in_a_car to floating point 4.0
space_in_a_car = 4.0

# setting drivers to integer 30
drivers = 30

# setting passengers to integer 90
passengers = 90

# setting variable equal to an equation. because cars and drivers are ints, so is cars_not_driven.
cars_not_driven = cars - drivers

# setting cars_driven equal to the value held in drivers, which is an int.
cars_driven = drivers

# setting carpool_capacity equal to the value of an equation including a float, which means carpool_capacity is also a float.  
carpool_capacity = cars_driven * space_in_a_car

# setting average_passengers_per_car equal to the value of an equation involving two int variables. average_passengers_per_car is an int, then.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
