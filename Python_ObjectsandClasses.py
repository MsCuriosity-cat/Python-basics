# The first lab assessment on objects and classes in Python
class Car(object):
    def __init__(self, make, model, colour):
        self.make = make
        self.model= model
        self.colour = colour
        self.owner_number = 0
    def car_info(self):
        print('make: ', self.make)
        print('model: ', self.model)
        print('colour: ', self.colour)
        print('number of car owners: ', self.owner_number)
    def sell(self):
        self.owner_number = self.owner_number+1        

# create a car object my_car
make = 'BMW'
model = 'M3'
colour = "red"
my_car = Car(make, model, colour)
# Use the method car_info to print out the data attributes
my_car.car_info()
# Call the method sell() in the loop
# then call the method car_info() again
for i in range(5):
    my_car.sell()
my_car.car_info()

# Creating a class
# Import the library
import matplotlib.pyplot as plt

# create a class circle
class Circle(object):
    
    # Constructor
    def __init__(self, radius = 3, colour = "green"):
        self.radius = radius
        self.colour = colour
    #Method
    def add_radius(self,r):
        self.radius = self.radius +r
        return(self.radius)
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius = self.radius, fc = self. colour))
        plt.axis('scaled')
        plt.show()   
# Creating an instance of a class Circle
# create an object RedCircle
RedCircle = Circle(10, 'red')  

# Find out the methods can be used on the object RedCircle
dir(RedCircle)
# Print the object attribute radius
RedCircle.radius
# Print the object attribute colour
RedCircle.colour
# Change the object's attributes
RedCircle.radius = 12
RedCircle.radius
# Draw the object by using the method draeCircle
RedCircle.drawCircle()
# Use the method add_radius to change the radius of the circle
print('Radius of object', RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Create a blue circle of given radius
BlueCircle = Circle(radius= 100, colour = 'Blue')
BlueCircle.radius
BlueCircle.colour
BlueCircle.drawCircle()

# Create a new Rectangle class for creating retangular object
class Rectangle(object):
    
    #Constructor
    def __init__(self, width = 2, height = 3, colour = 'Blue'):
        self.height = height
        self.width = width
        self.colour = colour
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc = self.colour))
        plt.axis('scaled')
        plt.show()

# Create skinnyblue rectangle
skinnybluerect = Rectangle()
skinnybluerect.height
skinnybluerect.width
skinnybluerect.drawRectangle()
FatYellowRect = Rectangle(20, 5, 'yellow')
FatYellowRect.height
FatYellowRect.width
FatYellowRect.drawRectangle()

# Objects and Classess assessment
# Text analysis
# Create a utility tool that can perform analysis on a given piece of text
class analysedText(object):
    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',','')
        # make text lowercase
        formattedText = formattedText.lower()
        self.fmtText = formattedText
    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')
    # Create dictionary
        freqMap = {}
        for word in set(wordList):
         # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        return freqMap  
    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0              


import sys

sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )
        
        
    



