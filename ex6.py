# sets new x var equal to a string, including formatting a number for display.
x = "There are %d types of people." % 10

# sets new binary var equal to a string
binary = "binary"

# sets new do_not var equal to a string 
do_not = "don't"

# sets new y var equal to a string that includes binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# displays the value of string x
print x

# displays the value of string y
print y

# displays a string including the reproduced value of x 
print "I said: %r." % x

# displays a string including y
print "I also said: '%s'." % y

# declares and sets hilarious value to a boolean
hilarious = False

# declares joke_evaluation string value and includes a placeholder for it to take an argument
joke_evaluation = "Isn't that joke so funny?! %r"

# displays joke_evaluation and uses hilarious as the argument
print joke_evaluation % hilarious

# initiates w as a string variable
w = "This is the left side of..."

# initiates e as a string variable
e = "a string with a right side."

# concatenates w and e variables and displays their combination
print w + e
