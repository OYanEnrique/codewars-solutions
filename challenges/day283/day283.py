'''
Indexed capitalization:
Given a string of lowercase letters and an array of integer indices, capitalize all letters at the given indices. If an index is beyond the string, it should be ignored.

Examples:
"abcdef", [1,2,5]     ==> "aBCdeF"
"abcdef", [1,2,5,100] ==> "aBCdeF" // There is no index 100.
Good luck!
'''
def capitalize(s, ind):
    s=[w for w in s]
    for i in ind:
        if i <= len(s)-1:
            s[i]=s[i].upper()
    return ''.join(s)