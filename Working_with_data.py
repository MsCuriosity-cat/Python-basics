# Download data
import urllib.request

url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

# Download Example file
!wget -O /resources/data/Example1.txt https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt

# read the example1.txt
example1 = 'Example1.txt'
file1 = open(example1, 'r')
# print the path of the file
file1.name
# print the mode of the file, either 'r' or 'w'
file1.mode
# read the file
FileContent = file1.read()
FileContent
# Print the file with '\n' as a new line
print(FileContent)
# Type of file content
type(FileContent)
# Close the file after finish
file1.close()

# A better way to open a file - using with statement
with open(example1, 'r') as file1:
    FileContent = file1.read()
    print(FileContent)

# verify if the file is closed
file1.closed
# see the content of file
print(FileContent)
# read first four characters 
with open(example1, 'r') as file1:
    print(file1.read(4))

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

# read one line
with open(example1, 'r') as file1:
    print('first line:' + file1.readline())

with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars

# use loop to iterate through the lines
with open(example1, 'r') as file1:
    i = 0
    for line in file1:
        print('Iteration', str(i), ':', line)
        i = i+1

# Read all lines and save as a list
with open(example1, 'r') as file1:
    FileasList = file1.readlines()

# Each element of the list corresponds to a line of text
# print the first line
FileasList[0]
FileasList[1]
FileasList[2]

## Write and save files in Python
# Write line to file
exmp2 = '/resources/data.Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write('This is line A')

# We can read the file to see if it worked:
# read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# We can write multiple lines:
# write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write('This is line A\n')
    writefile.write('This is line B\n')

# Check whether write to file has worked
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# We can write a list of text as follows
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines

# Write the strings in the list to text file
with open('Example2.txt', 'w')  as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
# Verify if writing to file is successfully carried out
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())  

# setting the mode to w overwrites
# all the existing data in file
with open('Example2.txt', 'w') as writefile:
    writefile.write('Overwrite\n')
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read()) 

# Write a new line to text file 
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write('This is line C\n')
    testwritefile.write('This is line D\n')
    testwritefile.write('This is line E\n')
# Verify if the new line is in the text file
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# let's try out the a+ mode:
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write('This is line E\n')
    print(testwritefile.read())
# revisiting a+ after learning about 'cursor'
with open('Example2.txt', 'a+') as testwritefile:
    print('Initial Location: {}'.format(testwritefile.tell())) 

    data = testwritefile.read()
    if (not data): #empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())
    
    testwritefile.seek(0,0) # move 0 bytes from beginning

    print('\nNew Location : {}'.format(testwritefile.tell()))      
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)

    print('Location after read: {}'.format(testwritefile.tell()))        

    # using r+ with truncate
    with open('Example2.txt', 'r+') as testwritefile:
        data = testwritefile.readlines()
        testwritefile.seek(0,0) #erite at the beginning of file

        testwritefile.write('Line 1' + '\n')
        testwritefile.write('Line 2' + '\n')
        testwritefile.write('Line 3' + '\n')
        testwritefile.write('finished\n')

        # uncomment the line below
        testwritefile.truncate()
        testwritefile.seek(0,0)
        print(testwritefile.read())

    # Copy a file
    # Copy file to another
    with open('Example2.txt', 'r') as readfile:
        with open('Example3.txt', 'w') as writefile:
            for line in readfile:
                writefile.write(line)  
# Verify if the copy is successfully executed
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())            