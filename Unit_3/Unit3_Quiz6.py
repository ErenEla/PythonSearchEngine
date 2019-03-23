#This code will create a list 
#that obtains all the links in the page 

def print_all_links(page):
    link_lists = []
    while True:
        #get_next_target method is in Unit2_Quiz12
        url,endpos = get_next_target(page)
        if url:
            link_lists.append(url)
            print(url)
            page = page[endpos:0]
        else:
            break
    return link_lists,endpos
print(print_all_links(text1))