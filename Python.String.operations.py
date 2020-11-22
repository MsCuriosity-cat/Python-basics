# Use quotations marks for defining string
"Michael Jackson"

# Use single quotation marks for defining string
'Michael Jackson'

# Digitals and spaces in string
'1 2 3 4 5 6 '

# Special characters in string
'@#2_#]&*^%$'

# Print the string
print("hello!")

# Assign string to variable
name = "Michael Jackson"
name

# Print the first element in the string
print(name[0])

# Print the element on the index 6 in the string
print(name[6])
# Print the element on the index 6 in the string
print(name[13])

# Print the last element in the string
print(name[-1])

# Print the first element in the string
print(name[-15])

# Find the length of string
len("Michael Jackson")

# Take the slice on variable name with only 0 to index 3
name[0:4]
# Take the slice on the variable name with only 8 to index 11 
name[8:12]

# Get every second element. The elements on index 1, 3, 5,....
name[::2]

# Get every second element in the range from index 0 to index 4
name[0:5:2]

# Concatenate two strings
statement = name + " is the best"
statement

# Print the string for 3 times
3* "Michael Jackson "

# Concatenate strings
name = "Michael Jackson "
name = name + "is the best"
name

# New line escape sequence
print("Michael Jackson \n is the best")

# Tab escape sequence
print(" Michael Jackson \t is the best")

# Include back slash in string
print(" Michael Jackson \\ is the best")

# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best")

# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Replace the old substring with the  new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
b

# Find the substring in the string. 
# Only the index of the first element of substring in string will be output
name = "Susmita Aown"
name.find('own')

# Find the substring in the string
name.find('tim') # if cannot find the substring in the string, then output is negative

