3+2*2

name = "Lizz"
print(name[0:2])

var = "01234567"
print(var[::2])

# Create tuple and access the last element
A = (0,1,2,3)
A[-1]
A[3]

# create a list
B = ["a", "b", "c"]
B[1:]

# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
"R&B", "progressive rock", "disco") 
genres_tuple

## Code : creating list
# sample list
L = ["Tulip", 10.1, 1982, [1, 2], ("A", "1")]

# List slicing
L[3:5]
# Use append and extend to add elements to list
L.extend(["bell", 10])
L.append(['a', 'b'])
L
# change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:',A)

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space
'hard rock'.split()
# Split the string by comma
'A,B,C,D'.split(',')

# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]', B[0])
# Clone (clone by value) the list A
B = A[:]
B # here B is a new copy of A, not the original list
# so if A is now changed, B will not
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

S = {'A', 'B','C'}
U = {'A', 'Z', 'C'}
U.union(S)

# Data types assessment
# Obtain first element of the tuple
A = ('a', 'b', 'c')
A[0]

# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 
# what are the keys
soundtrack_dic.keys()
# what are the values
soundtrack_dic.values()
# create a dictionary where the keys are the album names
# and the sales in millions are the values
album_sales_dict = {'Back in Black': '50', 'The Bodyguard': '50', 'Thriller':'65'}
# Find total sales for Thriller
album_sales_dict['Thriller']
# Find the name of the albums
album_sales_dict.keys()
# Find the values of the recording sales
album_sales_dict.values()