"""
Computational Phylogenetics
1.15.15
Introduction to Python
J.M. Brown
"""

# Try working through the following line-by-line

# Assigning an int(eger) value to a variable
myInt = 3

# Printing to the standard output (screen)
print(myInt)

# Assigning a float value to a variable
myFloat = 3.0
print(myFloat)

# Performing mathematical operations with ints will always return an int
print(2+3)
print(2*3)
print(2/3)

# The same is true for floats
print(2.0+3.0)
print(2.0*3.0)
print(2.0/3.0)

# Assigning a boolean value to a variable
myBool = True
print(myBool)

# Assigning a string value to a variable
myString = "thisIsAString"
print(myString)

# Special characters are 'escaped' with a \ that change letter's meaning
myString2 = "thisIs\nAMultiLineString"
print(myString2)

# We can concatenate strings with a '+'
print(myString + "_I_love_Python!")

# The same operator can do different things, depending on the data type.
print(3+3)

# However, operators often don't know how to mix data types
print(myString+3)

# We can fix this by making them the same data type on the fly - typecasting
print(myString+str(3))

# Some functions take a string and give you something back, like its length
print(len(myString))

# Methods are like functions but belong to individual instances of objects
print(myString.lower())
# If you type the line above yourself and you're working in Spyder, pause after
#   typing "myString." and it should give you a list of all available methods.

# Another useful method allows you to find substrings. 
print(myString.find("string"))
print(myString.find("String"))
# Look carefully at the output from these statements.

# Since these methods and functions return new strings after they run, they can
#   be strung together in one line.
print(myString.startswith('T'))
print(myString.upper().startswith('T'))

# Strings are actually a series of individual variables treated as one. The
#   individual characters can also be accessed directly and extracted.
print(myString[1:4])
# Wait, what just happened there? How many characters were printed and what was
#   the first one? 

# Sometimes, we only want our code to do something if a certain condition is
#   met. In other words, something else must first be True. To do this, we can
#   use if...else statements.
if 1 < 3:
    print("One is less than 3!")
else:
    print("One is NOT less than 3!")

if myBool:
    print "myBool is True!"
else:
    print "myBool is False!"

# You can also add in some elif statements in the middle to evaluate multiple
#   conditions.

testVal = 3.3

if testVal >= 5:
    print("testVal >= 5.")
elif testVal >= 4:
    print("testVal >= 4, but < 5.")
elif testVal >= 3:
    print("testVal >= 3, but < 4.")
elif testVal >= 2:
    print("testVal >=2, but < 3.")
elif testVal >= 1:
    print("testVal >=1, but < 2.")
else:
    print("testVal < 1.")


"""
This is a multi-line comment.
Sometimes we need to use functions that aren't part of the standard Python.
In that case, we import functions from other packages. For our purposes, we
will often use numpy and scipy. The next line imports the scipy package, but
gives it the shorthand name 'sp'. When we import a package this way, we have to
preface all functions from that package with 'sp'.
"""
import scipy as sp

# The random() function from scipy's random package will allow us to draw 
#   pseudorandom numbers from between 0 and 1. 
print(sp.random.random(3))
