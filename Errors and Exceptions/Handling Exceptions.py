# Hadling Exception:- It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user for input until a valid integer has been entered

# Example 1

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# In Above example what's happening, 
1. It will execute the statement b/w try and except
2. It no error occured inside the statement b/w try and except then it will come out of while loop
3. If error occured, first we will the check, which type of error is occured, if the error is "ValueError" then it will execute the

# A try statement may have more than one except clause

# Example

try:
	------------------
	--------CODE------
	------------------
except (RuntimeError, TypeError, NameError):
    pass

# In Above Example We can also check multiple error at same time


# Example 2

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")


# In Above Example We have define two error
# OSError:- It will come when file(myfile.txt) is not found
# ValueError:- It will come when integer value is not found

# Example 3

def this_fails():
     x = 1/0

try:
     this_fails()
except ZeroDivisionError as err:
     print('Handling run-time error:', err)


# Output:- Handling run-time error: division by zero