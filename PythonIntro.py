"""
Computational Phylogenetics
1.15/20/22.15
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


# Lists are compound variables. They simultaneously store the values of several
# variables of a particular type. Here's an example of a list of strings:

amniotes = ["Homo_sapiens","Gallus_gallus","Chrysemys_picta","bison_Bison"]

# Here's a list of integers:

hapChromNum = [23,39,25,30]

# Lists are nice because they are flexible in size, store many values and can
# be queried and sliced. For starters, if we want the first amniote species in
# our list, we would type:

print(amniotes[0]) 

# Remember that indices start at 0 in Python!

# Let's say we have a long list and can't remember where the painted turtle 
# (Chrysemys picta) is in the list. However, we have stored the haploid
# chromosome numbers in a separate list that has the same order as the taxon
# names. First, we can lookup where turtles are:

turtIndex = amniotes.index("Chrysemys_picta")

# Then, we can print out the corresponding haploid chromosome number:

print(hapChromNum[turtIndex])

# We could also skip creating another variable and combine this into one line.

print(hapChromNum[amniotes.index("Chrysemys_picta")])

# We can also extract a subset of elements from a list:

print(amniotes[1:3])
print(amniotes[-1])

# Negative indices start at the end and work forwards.

# A nice feature of lists is that they can also be manipulated. Elements can
# be individually changed or removed, and new elements can be added.

# Correcting the capitalization of the species name for bison:

print(amniotes[-1])

amniotes[-1] = "Bison_bison"

print(amniotes[-1])

# Removing chickens from the list of names and chromosome numbers:

print(amniotes)
print(hapChromNum)

amniotes.pop(1)
hapChromNum.pop(1)

print(amniotes)
print(hapChromNum)

# The .pop() method of a list removes individual elements and returns the
# associated value.

# Adding new elements to the end of a list:

amniotes.append("Mus_musculus")
hapChromNum.append(20)

print(amniotes)
print(hapChromNum)

# Lists can be concatenated with the + operator:

amphibs = ["Pseudacris_fouquettei","Pseudotriton_ruber"]
tetrapods = amniotes + amphibs
print(tetrapods)

# Very often, we would like to do something individually to all members of a
# list. For loops are very powerful for this. Here is a very simple example:

for species in tetrapods:
    print(species)

# In this case, species is our loop variable and iteratively takes the values
# of all the elements in the list tetrapods. The keywords "for" and "in" should
# always be used as shown in the example and that line should always end with a
# colon. All statements to be executed inside the for loop must follow on 
# subsequent lines and be indented identically. Python uses indentation to
# assign statements to loops.

# Here's a slightly more complicated example:

for species in amniotes:
    print(species + " has " + str(hapChromNum[amniotes.index(species)]) + " chromosomes.")

# If we would like a list of consecutive integers, we can use the range()
# function to make things more concise. range(x) returns a list of the integers
# 0 to x-1. 

for num in range(4):
    print num

# Your turn. How might we use list slicing to return the integers 1 to x?




# range also allows more complicated patterns of integers. To go from x to y in
# steps of z, use three arguments:

print(range(4,12,3)) # Goes from 4 to 12 in steps of 3


# Tuples are another complex data structure similar to lists. The differences 
# between them are minor, but can sometimes be important. Tuples are defined 
# using parentheses and can be indexed in the same manner as lists. However,
# they are immutable. Elements cannot be changed, nor can they be added or 
# removed. 

a = (1,5,10,7)
print(a[1])
a[1] = 3        # This will throw an error

# Dictionaries are another complex data type that allow the storage of paired
# data. The elements of these pairs are referred to as keys and values. To 
# define a dict, we use curly braces around the outside. The elements are the 
# key/value pairs. Individual pairs are separated by commas, and the keys and
# values in each pair are separated by colons.

myDict = {
    "key1" : "valOne",
    "key2" : "valTwo",
    "key3" : "valThree",
    "key4" : "valFour"
}

# The values stored in dictionaries can be accessed by using their corresponding
# keys. The syntax is identical to that used for accessing the individual
# elements of a list, string, or tuple.

print(myDict["key3"])

# Dictionaries do have some restrictions. Keys can only be strings or numbers
# and all of them must be unique.

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


# One of the main skills you'll need to write code that is compact and readable
# is the ability to write your own functions. First, think of an informative 
# name for the function. Next, define what it will take as input (arguments). 
# Lastly, think about the value it will return.

# Name: getChromNum
# Input argument: a species name
# Return value: an integer

def getChromNum(species):
    spIndex = amniotes.index(species)
    chromNum = hapChromNum[spIndex]
    return chromNum
    
getChromNum("Homo_sapiens")    

# Note that executing this function in the line above printed the output, but
# didn't allow us to do anything with this value. To do that, we need to assign
# the output to a variable. We've now captured the function's output and can
# do what we want with it after that.
    
hsChromNum = getChromNum("Homo_sapiens")
print(hsChromNum)    
    
# An IMPORTANT note on naming variables! If multiple variables are detected
# with the same name, Python uses a set of priority rules to determine which 
# one you're asking for. These rules determine the "scope" of a variable. Names
# assigned in function definitions (e.g., species above) are always given the
# highest priority. Therefore, any references to the variable called species in
# the getChromNum() function will use the value of species passed as an
# argument when getChromNum() is called. Also, variables defined just in a
# function (e.g., spIndex) will disappear when that function is done executing.
# Their scope is strictly 'local' to the function. Variables defined in the main
# body of a program are referred to as 'global'. Always strive to write functions
# that ONLY act on local variables, passed as arguments.
    
# For more information on scoping, see: 
# http://stackoverflow.com/questions/291978/short-description-of-python-scoping-rules

# Functions don't have to take an argument or return a value:

def printTwo():
    print(2)

# Functions can also take multiple arguments:

def twoFavSpecies(spOne,spTwo):
    print("My two favorite species are "+spOne+" and "+spTwo+".")

twoFavSpecies(amniotes[1],amniotes[2])

# If you explicitly name the arguments when you call the function, you can 
# supply them in whatever order you prefer:

twoFavSpecies(spTwo=amniotes[1],spOne=amniotes[2])

# We can also assign default values to some variables in the function definition.
# In that case, the user can choose whether or not to specify an alternative
# value for that variable.

def favSpecies(spOne,spTwo="Pituophis_catenifer"):
    print("My favorite species are "+spOne+" and "+spTwo+".")

favSpecies("Homo_sapiens")
favSpecies("Homo_sapiens","nothing else")

# Lists can also be passed as arguments to a function:

def allFavSpecies(speciesList):
    print("I like "),
    for sp in speciesList:
        if sp != speciesList[-1]:
            print(sp+" and "),
        else:
            print(sp),
    print(".")
        
allFavSpecies(amniotes)        
        
# Note that you can print statements without adding a newline by placing a comma
# after the print command. These print statements still add a space, though.
# You can even avoid spaces by importing the sys library and using
# sys.stdout.write() in place of print().

"""
Sometimes we need to use functions that aren't part of the standard Python.
In that case, we import functions from other packages. For our purposes, we
will often use numpy and scipy. The next line imports the scipy package, but
gives it the shorthand name 'sp'. When we import a package this way, we have to
preface all functions from that package with 'sp'.
"""
import scipy

# The random() function from scipy's random package will allow us to draw 
#   pseudorandom numbers from between 0 and 1. 
print(scipy.random.random(3))
