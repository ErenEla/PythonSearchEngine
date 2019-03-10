# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function


# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

#ENTER CODE BELOW HERE

x = 3.14159
x_round = str(round(x))
x_point = x_round.find(".")
print(x_round[:x_point])

#Train Focus 

s = "CidatyUcityda"

print('1',s[6]+s[-2:]+s[7:12])

print('2',s[6]+s[-2:]+s[7:11])

print('3',s[6]+s[2:4]+s[7:13])

print('4',s[-7]+s[2:4]+s[7:11])

print('5',s[6]+s[-2]+s[3]+s[:-2]+s[4:6])

print('6',s[6]+s[2]+s[3]+s[7:11])