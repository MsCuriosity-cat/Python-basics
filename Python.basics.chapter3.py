# Conditional Statements
# Comparison operators

# coditional equal
a = 5
a == 6
# Greater than sign
i = 6
i >5
i = 2
i >5
# Inequality sign
i = 6
i!= 6
# Use Equality sign to compare the strings
"ACDC" == "Michael Jackson"
# Use Inequality sign to compare the strings
"ACDC" != "Michael Jackson"
# Compare characters
'B' > 'A'
# Compare multiple characters
'BA' > 'AB'

# Branching
# If statement example
age = 19
age = 18

# expression that can be true or false
if age > 18:
   # within indet we have the exression that is run if the condition is true
    print("you can enter")
#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

# Else statement example
age = 18
#age = 19
if age > 18:
    print("you can enter")
else:
    print("go see Meat Loaf")

    print("move on")

# Elif statement example
    age = 18
    age
if age > 18:
    print("you can enter")
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf")
print("move on")                
# Condition statement example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')
# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

# checking if an album was released after 1979
# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

# Check if an album was released before 1980
# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

# The not statement checkes if the statement is false
# Condition statement example
album_year = 1983

if not (album_year == '1984'):
    print("Album year is not 1984")

# Loops
