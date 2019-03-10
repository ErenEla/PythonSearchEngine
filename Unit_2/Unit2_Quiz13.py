#Method for printing all the links in the page 
#Importing earliest Quiz_Answers to be able to use method "get_next_target"

import Unit2_Quiz12

def print_all_links(page):
    while True:
        url,endpos = Unit2_Quiz12.get_next_target(page)
        if url:
            print(url)
            page = page[endpos:0]
        else:
            break
print_all_links(Unit2_Quiz12.text1)
