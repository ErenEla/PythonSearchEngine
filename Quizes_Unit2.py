# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def square_of_number(number):
    value = number*number
    return value

print(square_of_number(5))
print(square_of_number(10))

# To test your procedure, uncomment the print 
# statement below, by removing the hash mark (#) 
# at the beginning of the line.

# Do not remove the # from in front of the line 
# with the arrows (>>>). Lines which begin like 
# this (#>>>) are included to show the results
# you should see when run your procedure.

#print square(5)
#>>> 25



# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

def sum3(number1,number2,number3):
    value = number1+number2+number3
    return(value)
print(sum3(1,2,3))
print(sum3(93,53,70))

#print sum3(1,2,3)
#>>> 6

#print sum3(93,53,70)
#>>> 216

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


# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

danton = "De l'audace, encore de l'audace, toujours de l'audace"
twister = "she sells seashells by the seashore"

def find_second(text,keyword):
    first_pos=text.find(keyword)+1
    keyword_len = len(keyword)
    new_text = text[first_pos+keyword_len:]
    second_pos =new_text.find(keyword)+keyword_len+first_pos
    return(second_pos)
print(find_second(danton,"audace"))
print(find_second(twister,"she"))


#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#print find_second(danton, 'audace')
#>>> 25

#twister = "she sells seashells by the seashore"
#print find_second(twister,'she')
#>>> 13

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

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'


def is_friend(name):
    if name[0:1] == "D":
        return True
    return (False)
print(is_friend("Diane"))

#print is_friend('Diane')
#>>> True

#print is_friend('Fred')
#>>> False
# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_stillfriend(name):
    if name[0] == "D":
        return True
    elif name[0] == "N":
        return True
    else:
        return False
print(is_stillfriend("Ned"))

#print is_friend('Diane')
#>>> True

#print is_friend('Ned')
#>>> True

#print is_friend('Moe')
#>>> False

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return(num1)
    elif num2>num3:
        return(num2)
    else:
        return(num3)
print(biggest(3,6,9))
print(biggest(6,9,3))
print(biggest(9,3,6))

#print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9