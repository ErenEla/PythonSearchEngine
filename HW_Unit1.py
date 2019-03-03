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