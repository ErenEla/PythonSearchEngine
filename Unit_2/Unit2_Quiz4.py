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