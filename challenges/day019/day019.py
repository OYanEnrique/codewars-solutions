'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
'''
def abbrev_name(name):
    name = name.split()
    initials = ""
    for initial in name:
    	initials += initial[0].capitalize()
    	initials += '.'	
    return initials[:-1]