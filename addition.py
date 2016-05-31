# This is an extension of Exercise 13.

from sys import argv

script, first, second = argv

print "This script is called:", script
print "Now we'll add up your numbers."

# Uh oh, looks like argv is passing them in as strings.
first = int(first)
second = int(second)

print "Your first number is %i," %first
print "Your second number is %i," %second
print "And %i plus %i is %i." %(first, second, first+second)

# Potential problems:
# This script will fail w/ floats.
# This script will fail w/ non-digit strings.
# This thing can ONLY handle integer arguments.
