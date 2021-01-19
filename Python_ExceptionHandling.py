# Try Except
# potential code before try catch
try:
    # code to try to execute
except:
    # code to execute if there is an exception  

# code that will still execute if there is an exception

# try except example
a = 1

try:
    b = int(input('Please enter a number to divide a'))
    a = a/b
    print('Success a =',a)
except:
    print('There was an error')  

# illustrating the try specific exception handling
# potential code before try catch

try:
    # code to try to execute
except (ZeroDivisionError, NameError):
    # code to execute if there is an exception of the given types
    
# code that will execute if there is no exception or a one that we are handling

# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
    
# code that will execute if there is no exception or a one that we are handling

# there can also be an empty except at the end
# to catch an unexpected exception
# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
    
# code that will execute if there is no exception or a one that we are handling

# try Except specific Example
# same example as before but with additional messsages to let the user know 
# what is wrong with the input
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print('Success a =', a)
except ZeroDivisionError:
    print('The number you provided cant divide because it is 0')
except ValueError:
    print('You did not provide a number')
except:
    print('Something went wrong')    

# Illustrating the try except else and finally
# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling

# Try except else and finally example
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("Success a =", a)    

# use finally to let the user know that we are 
# done processing thier answer
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")