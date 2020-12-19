# Functions in Python
# First function example: Add 1 to a and store as b

def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)
# Get a help on add function
help(add)    
# Call the function add()
add(1)

# Define a function for multiplying two numbers 
def Mult(a,b):
    c = a*b
    return(c)
    print('This is not printed')

result = Mult(12, 2)
print(result)

# Use mult() multiply two integers
Mult(2, 3)
# Use mult() multiply two floats
Mult(10.0, 3.14)
# Use mult() multiply two different type values together
Mult(2, "Michael Jackson ")

# Function definition
def square(a):
    #Local variable b
    b = 1
    c = a * a+b
    print(a, 'if you sqaure +1', c)
    return(c)
# Initialises Global variable
x= 3
# Make functional call and return function a y
 y = square(x)
 y
 # Directly enter a number as parameter
 square(2)
# Define functions, one with return value None and other without return value
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None) 
# See the output
MJ()    
MJ1()
# See what functions returns are
print(MJ())
print(MJ1())
# Define the function for combining strings
def con(a,b):
    return(a+b)
# Test on the con() function
con('This ','is')

# Make a Function for the calculation of a equation
def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if (c < 0):
        c = 0
    else:
        c = 5
    return(c)   
# Pre-defined functions
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)   
# Use sum() to add every element in a list or tuple together
sum(album_ratings)    
# Show the length of the list or tuple
len(album_ratings) 

# Function example with if-else statement and loops
def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return 'Modern'
    else:
        return 'Oldie'  
x = type_of_album('Michael Jackson', 'Thriller', 1980)
print(x)          
# Print the list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)
# Implement the printlist function
PrintList(['1', 1, 'the man', 'abc'])

# Setting default values in your custom functions
def isGoodRating(rating = 4):
    if(rating < 7):
        print("this album sucks, it's rating is", rating)
    else:
        print("this album is good its rating is",rating)
# Test the value with default value and with input
isGoodRating()
isGoodRating(10)
# Global variables
# Example of global variable
artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
printer1(artist)
printer1(internal_var1)   

# Create global variable inside a function
artist = "Michael Jackson"

def printer(artist):
    global internal_var
    internal_var = "Whiteney Houston"
    print(artist, "is an artist")
printer(artist) 
printer(internal_var)   

# Example of gloabal varaible
myFavBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavBand:
        return 10.0
    else:
        return 0.0
   print("AC/DC's rating is:", getBandRating("AC/DC"))         
   print("Deep Purple's rating is:", getBandRating("Deep Purple"))
   print("My favourite band is :", myFavBand)

# A local variable is not acccessible from outside the function
def getBandRating(bandname):
    myFavBand = "AC/DC"
    if bandname == myFavBand:
        return 10.0
    else:
        return 0.0
print("AC/DC's rating is:", getBandRating("AC/DC"))  
print("Deep Purple's rating is:", getBandRating("Deep Purple"))
print("My favourite band is :", myFavBand)  

# Example of global variable and local variable with the same name
myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

# Collections and Functions
def printall(*args): # All the arguments are 'packed' into args which can be treated as a tuple
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)
# printall with 3 arguments
printall('Horsefeather', 'Adonis', 'Bone')
#printall with 4 arguments
printall('Sidecar','Long Island','Mudslide','Carriage')   

# The arguments can also be packed into a dictionary
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])
printDictionary(country = 'Canada', province = 'Ontario', city = 'Toronto')

# Functions can accept and return data types, objects and even other functions as arguments
def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One", "Two"]
addItems(myList)
myList
