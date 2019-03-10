# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

def abbaize(string1,string2):
    newst=string1+string2+string2+string1
    return(newst)
print(abbaize("a","b"))
print(abbaize("dog","cat"))

#print abbaize('a','b')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'