# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.
#from Unit_2 import Unit2_Quiz5

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

#from unit2_quiz5

def bigger(n1,n2):
    if n1>n2:
        big_num = n1
    else:
        big_num=n2
    return(big_num)

def median(a,b,c):
    if biggest(a,b,c) == a:
        return(bigger(b,c))
    elif biggest(a,b,c) == b:
        return(bigger(a,c))
    else:
        return(bigger(a,b))
print(median(1,2,3))
print(median(9,3,6))
print(median(7,8,7))

#print(median(1,2,3))
#>>> 2

#print(median(9,3,6))
#>>> 6

#print(median(7,8,7))
#>>> 7