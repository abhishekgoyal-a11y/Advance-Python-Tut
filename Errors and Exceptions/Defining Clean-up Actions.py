# Defining Clean-up Actions:- The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances.

# Example1:- 

try:
    print(2+'a')
except Exception as e:
	print(e)
finally:
    print('Goodbye, world!')

# Output:- unsupported operand type(s) for +: 'int' and 'str'
		   # Goodbye, world!

# Example2:- 

try:
    print(2+2)
except Exception as e:
	print(e)
finally:
    print('Goodbye, world!')

# Output:- 4
		   # Goodbye, world!


# In both example 1 and 2 you can see there is only one thing is common in output is, it is printing "Goodbye, world!"

# Example3:-

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())

# Output:- False

# Example4:-

def bool_return():
    try:
        return True
    except:
        return False

print(bool_return())

# Output:- True

# In both example 3 and 4 there are diffrent output comes
# Why diffrent output?, let's check

# In Example3

# In bool_return function first we are executing the try statement, till try executing statement bool_return function is True but after finally statement execute the bool_return function changing to False

# In Example4

# In this we are not executing the except statement, we are only executing try statement, that's why bool_return function return True



# Example5(More complicated)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

# divide(2, 1)

# Output:- result is 2.0 executing finally clause

# divide(2, 0)

# Output:- division by zero! executing finally clause

# divide("2", "1")

# Output:- executing finally clause TypeError: unsupported operand type(s) for /: 'str' and 'str'

# Common thing is:- finally statement always executing