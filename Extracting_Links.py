#ExtractingLinks 

# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a>>'''
   
ref = '<a href='

#assign a variable named quote to find the quotes, and find the length of ref to spot the link between two marks

quote = '"'
ref_len = len(ref)

#find first quote and last quote to print out the exact link for any html code 

start_link = page.find(ref)
first_quote = page.find(quote,start_link+ref_len)+1
last_quote = page.find(quote,first_quote)
url = page[first_quote:last_quote]

print(url) 