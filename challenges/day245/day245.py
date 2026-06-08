'''
ASCII Total:
You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all printable ASCII characters.

Examples:

uniTotal("a") == 97
uniTotal("aaa") == 291
'''
def uni_total(char):
    x = 0
    for c in char:
        if len(char) > 1:
            x += ord(c) 
        elif len(char) == 1:
            return ord(char)  
        else:
            return 0
    return x