# Exception:- Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal

# Example 1

10 * (1/0)

# We can not divide any number by Zero

# Error: ZeroDivisionError: division by zero

# Example 2

4 + spam*3

# Error: NameError: name 'spam' is not defined

# Example 3

'2' + 2

# We can not add string with integer, we can only add same datatype like string with string, or integer with integer or float with integer etc..

# Error: TypeError: Can't convert 'int' object to str implicitly


# In Python there are many Built-in Exceptions

# More Details:- https://docs.python.org/3/library/exceptions.html