# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(x):
    result = 0
    for N in x:
        if N[0] == "U":
            result = result+1
        else:
            result
    return result

print (measure_udacity(['Dave','Sebastian','Katy']))
#>>> 0

print (measure_udacity(['Umika','Umberto']))
#>>> 2