# Write a function that divides the first input by the second
def divides(a, b):
    c = a/b
    return(c)
divides(8,5)    
# Use the con function for the following question
def con(a, b):
    return(a + b)

con(450, 2103) # yes can be used to add integers
con('My age is :', 14) # no cannot be used to add strings
con(['a', 1], ['b', 2]) # yes can be used to concatenate lists or tuples

def fillBag(**balls):
    global bag 
    bag = balls
     

def totalBalls():
    total = 0
    for color in bag:
        total += bag[color]
    return total
    
def probOf(colour):
    return bag[colour]/totalBalls()

def probAll():
    probDict = {}
    for colour in bag:
        probDict[colour] = probOf(colour)
    return probDict

testBag = dict(red = 12, blue = 20, green = 14, grey = 10)
total = sum(testBag.values())
prob={}
for colour in testBag:
    prob[colour] = testBag[colour]/total

def testMsg(passed):
    if passed:
        return 'Test passed'
    else:
        return 'Test failed'

print("fillBag: ")
try:
    fillBag(**testBag)
    print(testMsg(total == totalBalls()))
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")



print("totalBalls : ")
try:
    totalBalls()
    print(testMsg(total == totalBalls()))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probOf")
try:
    probOf
    passed = True
    for color in testBag:
           if probOf(color) != prob[color]:
                passed = False
        
    print(testMsg(passed) )
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probAll")
try:
    probAll()
    print(testMsg(probAll() == prob))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
