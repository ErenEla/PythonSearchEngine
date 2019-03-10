# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(n1,n2):
    if n1>n2:
        big_num = n1
    else:
        big_num=n2
    return(big_num)
print(bigger(2,7))
print(bigger(3,2))
print(bigger(3,3))

#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3