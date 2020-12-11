# Create your first tuple
tuple1 = ("disco", 10, 1.2)
tuple1

# print the type of tuple you created
type(tuple1)

# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Use negative index to get the value of the last element
tuple1[-1]

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
tuple2

# Slice from index 0 to index 2
tuple2[0:3]
# Slice from index 3 to index 4
tuple2[3:5]
# Get the length of tuple
len(tuple2)

# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple
RatingsSorted = sorted(Ratings)
RatingsSorted

# create a nest tuple
NestedT = (1,2, ("pop", "rock"), (3,4), ("disco", (1,2)))

# print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ", NestedT[2][0])
print("Element 2, 1 of Tuple: ", NestedT[2][1])
print("Element 3, 0 of Tuple: ", NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

# Print the first element in the second nested tuples
NestedT[2][1][0]
# Print the second element in the second nested tuples
NestedT[2][1][1]
# Print the first element in the second nested tuples
NestedT[4][1][0]
# Print the second element in the second nested tuples
NestedT[4][1][1]

# sets 
# Cast the following list to a set
['A','B','C','A','B','C']
set(['A','B','C','A','B','C'])

# Add an element to the set
S = {'A', 'B', 'C'}
S.add('D')
S
# Find the intersection of sets A and B
A = {1,2,3,4,5}
B ={1,3,9,12}
A & B
# convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_list = set(album_list)
album_list

music_genres = set(['pop', 'pop','rock', 'soul', 'hard rock', 'progressive rock'])
music_genres

# sample set
A = set(['Thriller', 'Back in Black', 'AC/DC'])
A

# add element to set
A.add('NSYNC')
A
# Try to add duplicate element to the set
A.add('NSYNC')
A
# remove element from the set
A.remove('NSYNC')
A

# Verify the element is in the set
'AC/DC' in A
'NSYNC' in A

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
album_set1, album_set2 # makes a tuple 

# Find the intersections
intersection = album_set1 & album_set2
intersection

# Find difference in set1 but not set2
album_set1.difference(album_set2)
# difference in set2 but not set1
album_set2.difference(album_set1)

# Find the union of two sets
album_set1.union(album_set2)

# Check if superset
set(album_set1).issuperset(album_set2)

# Check if subset
set(album_set2).issubset(album_set1)

# Dictionaries
# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict

# Access to the value by the key
Dict["key1"]

# Access to the value by tuple
Dict[(0,1)]

# Create a sample disctionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",  "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict

# Get value by keys
release_year_dict['Thriller']
release_year_dict['The Bodyguard']

# Get all the keys in the dictionaries
release_year_dict.keys()
# Get all the values in the dictionary
release_year_dict.values()
# Append value with key in dictionary
release_year_dict['Graduation'] = '2007'
release_year_dict
# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict
# Verify if an element is in the dictionary
'The Bodyguard' in release_year_dict
