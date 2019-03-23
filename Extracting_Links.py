#ExtractingLinks 

# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

#page = '''<div id="top_bin"> <div id="top_content" class="width960">
#   <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a>>'''
#   
#ref = '<a href='
#
##assign a variable named quote to find the quotes, and find the length of ref to spot the link between two marks
#
#quote = '"'
#ref_len = len(ref)
#
##find first quote and last quote to print out the exact link for any html code 
#
#start_link = page.find(ref)
#first_quote = page.find(quote,start_link+ref_len)+1
#last_quote = page.find(quote,first_quote)
#url = page[first_quote:last_quote]
#
#print(url) 

text1 = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a>>'''

text2 = ("https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python")

def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if start_link == -1:
        return None,0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
print(get_next_target(text1)) 

def print_all_links(page):
    link_lists = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            link_lists.append(url)
            print(url)
            page = page[endpos:0]
        else:
            break
    return link_lists,endpos
print(print_all_links(text1))

