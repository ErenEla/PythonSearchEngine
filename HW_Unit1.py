# Write Python code that prints out the number of hours in 7 weeks.
#(I wanted to take it one step further)

hour = 24 
day_hours = 1*hour
week_hours = 7*day_hours
print("How many weeks to calculate?")
week_amount = int(input())
print(week_hours*week_amount)


# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

# ENTER CODE BELOW HERE
keyword = "zip"
first_zip = text.find(keyword)
zip_len = len(keyword)
zip_x = first_zip+zip_len
answer = text.find(keyword,zip_x,)
print(answer)



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

###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1
#marker = "AFK"
#replacement = "away from keyboard"
#line = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###

marker_pos = line.find(marker)
rep_len = len(replacement)
marker_len = len(marker)
replaced = line[:marker_pos]+replacement+line[marker_pos+marker_len:]
print(replaced)

#Palindrome
###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. Make a program 
# that checks if a word is a palindrome. 
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

word = "madam"
palindrome = word[::-1]
# test case 2
word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###
is_palindrome = word.find(palindrome)

# TESTING
print (is_palindrome)
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"