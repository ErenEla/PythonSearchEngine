# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(nx):
    i = 1
    while i<=nx:
        print(i)
        i = i+1
    return(i)
print_numbers(5)

#print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.