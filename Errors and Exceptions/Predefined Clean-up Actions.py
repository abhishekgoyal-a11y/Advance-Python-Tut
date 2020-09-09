# Predefined Clean-up Actions:-

# Example1:-

for line in open("myfile.txt"):
    print(line, end="")


# Example2:-

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


# In both example output will same, but the diffrence is, in first example the file will not closed after doing the task and in second example file will closed after doing the task
# This is not an issue for smaller script or application but it can cause for big application or scripts