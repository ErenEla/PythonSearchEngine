# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [1,2,2]

def replace_spy(x):
    x[0] = x[0]
    x[1] = x[1]
    x[2] = x[2]+1
    return x
   
# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.

print(replace_spy(spy)) 
#>>> [0,0,8]
