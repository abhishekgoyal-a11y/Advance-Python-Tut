# Raising Exceptions:- The raise statement allows the programmer to force a specified exception to occur

# Example 1

raise NameError('HiThere')

# Output:- NameError: HiThere

# Example 2

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

# Output:- NameError: HiThere

# more details about raise "https://docs.python.org/3/reference/simple_stmts.html#raise"