'''
Reverse every other word in the string:
Reverse every other word in a given string, then return the string. 
Throw away any leading or trailing whitespace, while ensuring there is exactly one 
space between each word. 
Punctuation marks should be treated as if they are a part of the word in this kata.
'''
def reverse_alternate(st):
    st = st.strip().split()
    final_st = ""
    for i in range(len(st)):
        if i % 2 != 0:
            final_st += st[i][::-1]
            final_st += " "
        else:
            final_st += st[i]
            final_st += " "
    return final_st[:-1]