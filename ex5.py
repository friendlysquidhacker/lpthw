name = "Zed A. Shaw"
age = 35 # not a lie
height_in = 74 # inches
weight_lb = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_cm = height_in * 2.54
weight_kg = weight_lb / 2.2

print "Let's talk about %s." % name
print "He's %d inches or %d cm tall." % (height_in, height_cm)
print "He weighs %d pounds or %d kilos." % (weight_lb, weight_kg)
print "That's not so heavy -- he's probably human."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age, height_in, weight_lb, age + height_in + weight_lb)
